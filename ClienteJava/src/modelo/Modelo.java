package modelo;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Modelo {
	private vista.Vista vista;
	private Channel canalRecibir, canalEnviar; 
	private Connection conexion;
	private ConnectionFactory factory;
	public Modelo(vista.Vista view) throws IOException, TimeoutException {
        this.vista = view;
        

    }
	public void conectar(String host) throws IOException, TimeoutException {
		// Establecer una conexión con el servidor RabbitMQ
        factory = new ConnectionFactory();
        factory.setHost(host);
        this.conexion = factory.newConnection();
        this.canalRecibir = conexion.createChannel();  // Canal para recibir mensajes
        this.canalEnviar = conexion.createChannel();  // Canal para enviar mensajes

        // Declarar una cola recibir en el servidor RabbitMQ
        this.canalRecibir.queueDeclare("cliente1", false, false, false, null);
        // Cola para enviar los mensajes a cliente 2
        this.canalEnviar.queueDeclare("cliente2", false, false, false, null);

        // Recibir los mensajes colocados en mi queue cliente1
        this.canalRecibir.basicConsume("cliente1", true, (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            this.vista.agregarMensaje(message, "");
        }, consumerTag -> {});
	}
	
	public void enviarMensaje(String mensaje, String ipAddress) throws IOException, TimeoutException {
        if(factory == null) {
        	conectar(ipAddress);
        }
		// Publicar mensaje en cola chat
        this.canalEnviar.basicPublish("", "cliente2", null, mensaje.getBytes("UTF-8"));
        this.vista.agregarMensaje(mensaje, "");
    }

    public void cerrarConexion() throws IOException, TimeoutException {
        this.conexion.close();
    }
	
	
}
