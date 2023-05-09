package controlador;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public class Controlador {
    private vista.Vista vista;
    private modelo.Modelo modelo;

    public Controlador() throws IOException, TimeoutException {
        this.vista= new vista.Vista(this);
    }	
    

    public void enviarMensaje(String mensaje, String ipAddress) throws IOException, TimeoutException{
        this.modelo.enviarMensaje(mensaje,ipAddress);
    }
    
    public void mostrarMensaje(String m, int t) {
    	this.vista.agregarMensaje(m, t);
    }
    
    public boolean estaServerDisponible(String host) {
    	try {
    		this.modelo= new modelo.Modelo(this);
			this.modelo.conectar(host);
			return true;
		} catch (IOException | TimeoutException e) {
			// TODO Auto-generated catch block
			return false;
		}
    }
    
    public boolean estaUsuarioDisponible(String user) {
    	// En Prueba
    	if(this.modelo.isCanalUsado(user)) return false;
    	else return true;
    }
    
    public String[] usuariosDisponibles(String user) {
    	modelo.setName(user);
    	return this.modelo.getUsuarios().toArray(new String[0]);
    }

    public void cerrarConexion() throws IOException, TimeoutException {
        this.modelo.cerrarConexion();
    }

    public void iniciar() {
    	vista.setSize(new java.awt.Dimension(400, 600));
        vista.iniciar();
    }

    
}
