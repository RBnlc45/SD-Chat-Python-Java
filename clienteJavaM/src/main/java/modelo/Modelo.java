package modelo;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Modelo {
	private String host, name, destinatario;
	private vista.Vista vista;
	private Channel canalRecibir, canalEnviar; 
	private Connection conexion;
	private ConnectionFactory factory;
	public Modelo(vista.Vista view) throws IOException, TimeoutException {
        this.vista = view;
    }
	public void setHost(String host) {
		this.host = host;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setDestinatario(String destinatario) {
		this.name = destinatario;
	}
	public void conectar(String host) throws IOException, TimeoutException {
		// Establecer una conexión con el servidor RabbitMQ
		factory = new ConnectionFactory();
        factory.setHost(this.host);
        this.conexion = factory.newConnection();
	}
	// name->cliente1, destinatario->cliente2
	public void crearCanal() throws IOException {
        this.canalRecibir = conexion.createChannel();  // Canal para recibir mensajes
        this.canalEnviar = conexion.createChannel();  // Canal para enviar mensajes

        // Declarar una cola recibir en el servidor RabbitMQ
        this.canalRecibir.queueDeclare(name, false, false, false, null);
        // Cola para enviar los mensajes a cliente 2
        this.canalEnviar.queueDeclare(destinatario, false, false, false, null);

        // Recibir los mensajes colocados en mi queue cliente1
        this.canalRecibir.basicConsume(name, true, (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            this.vista.agregarMensaje(message, 2);
        }, consumerTag -> {});
	}
	
	public void enviarMensaje(String mensaje, String ipAddress) throws IOException, TimeoutException {      
		// Publicar mensaje en cola chat
        this.canalEnviar.basicPublish("", destinatario, null, mensaje.getBytes("UTF-8"));
        this.vista.agregarMensaje(mensaje, 2);
    }
	
	public java.util.List<String> getUsuarios() {
	    String url = String.format("http://%s:%d/api/queues", host, 15672);
	    java.util.List<String> users = new java.util.ArrayList<String>();
	    try {
	        java.net.URLConnection connection = new java.net.URL(url).openConnection();
	        String authString = "guest:guest";
	        byte[] authEncBytes = org.apache.commons.codec.binary.Base64.encodeBase64(authString.getBytes());
	        String authStringEnc = new String(authEncBytes);
	        connection.setRequestProperty("Authorization", "Basic " + authStringEnc);
	        java.io.InputStream response = connection.getInputStream();
	        java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(response, java.nio.charset.StandardCharsets.UTF_8));
	        String line;
	        while ((line = reader.readLine()) != null) {
	        	org.json.JSONArray queues = new org.json.JSONArray(line);
	            for (int i = 0; i < queues.length(); i++) {
	            	org.json.JSONObject queue = queues.getJSONObject(i);
	                String user = queue.getString("name");
	                users.add(user);
	            }
	        }
	        reader.close();
	    } catch (java.io.IOException | org.json.JSONException e) {
	        e.printStackTrace();
	    }
	    return users;
	}


    public void cerrarConexion() throws IOException, TimeoutException {
    	if(conexion != null) this.conexion.close();
    }
	
	
}