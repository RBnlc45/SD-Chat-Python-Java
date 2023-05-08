package controlador;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public class Controlador {
    private vista.Vista vista;
    private modelo.Modelo modelo;

    public Controlador() throws IOException, TimeoutException {
        this.vista= new vista.Vista(this);
        this.modelo= new modelo.Modelo(vista);
    }

    public void enviarMensaje(String mensaje, String ipAddress) throws IOException, TimeoutException{
        this.modelo.enviarMensaje(mensaje,ipAddress);
    }

    public void cerrarConexion() throws IOException, TimeoutException {
        this.modelo.cerrarConexion();
    }

    public void iniciar() {
    	vista.setSize(new java.awt.Dimension(400, 600));
        vista.iniciar();
    }

    
}
