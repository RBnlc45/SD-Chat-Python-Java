package vista;
import java.awt.Dialog.ModalExclusionType;
import java.io.IOException;
import java.util.concurrent.TimeoutException;
import javax.swing.JPanel;

public class Vista extends javax.swing.JFrame {

	private static final long serialVersionUID = 1L;                   
    public javax.swing.JButton btnEnviar, btnConectar, btnDesconectar;
    private javax.swing.JLabel jLabel2, lblUser, lblNewLabel;
    public javax.swing.JPanel jPanelCentro, jPanelNorte, jPanelDestinatrio, jPanelSur;
    public javax.swing.JTextField txtNombreU, txtServerIp;
    public javax.swing.JTextArea txtMensaje;
    private javax.swing.JList<javax.swing.JPanel> listChat;
    private javax.swing.DefaultListModel<javax.swing.JPanel> chatModel;
    private controlador.Controlador controlador;
    private javax.swing.JComboBox<String> cbxDestinatario;
    private javax.swing.JPanel panelTitulo, panelUsuario, panel_1, panel_2, panel_3;
    private javax.swing.JLabel lblClienteJava;
    private JPanel panel_4;
	
	public Vista(controlador.Controlador controlador) {
		setAutoRequestFocus(false);
		setModalExclusionType(ModalExclusionType.APPLICATION_EXCLUDE);
		this.controlador = controlador;
		setAlwaysOnTop(true);
		initComponents();
		addWindowListener(new java.awt.event.WindowAdapter() {
            @Override
            public void windowClosing(java.awt.event.WindowEvent e) {
                try {
                	al_cerrar();
				} catch (IOException | TimeoutException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
            }
        });
		
	}
	
	private void initComponents() {

        jPanelNorte = new javax.swing.JPanel();
        jPanelDestinatrio = new javax.swing.JPanel();
        jPanelDestinatrio.setBorder(javax.swing.BorderFactory.createTitledBorder("Datos Destinatario"));
        jLabel2 = new javax.swing.JLabel();
        jPanelCentro = new javax.swing.JPanel();
        jPanelSur = new javax.swing.JPanel();
        txtMensaje = new javax.swing.JTextArea();
        btnEnviar = new javax.swing.JButton();
        // Diseño interfaz
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Cliente Java");
        setMinimumSize(new java.awt.Dimension(400, 600));
        setResizable(false);
        jPanelNorte.setLayout(new java.awt.BorderLayout());
        jPanelDestinatrio.setLayout(new java.awt.GridLayout(1, 4));     
        panel_2 = new javax.swing.JPanel();
        jPanelDestinatrio.add(panel_2);
        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        jLabel2.setText("Nombre:");
        jPanelDestinatrio.add(jLabel2);      
        cbxDestinatario = new javax.swing.JComboBox<String>();
        cbxDestinatario.addActionListener(e -> {
        	setColaDestinatario();
        });
        cbxDestinatario.setEditable(false);
        jPanelDestinatrio.add(cbxDestinatario);
        jPanelNorte.add(jPanelDestinatrio, java.awt.BorderLayout.SOUTH);
        
        panel_4 = new JPanel();
        jPanelDestinatrio.add(panel_4);
        getContentPane().add(jPanelNorte, java.awt.BorderLayout.PAGE_START);       
        panelTitulo = new javax.swing.JPanel();
        panelTitulo.setBorder(javax.swing.UIManager.getBorder("FileChooser.listViewBorder"));
        jPanelNorte.add(panelTitulo, java.awt.BorderLayout.NORTH);
        panelTitulo.setLayout(new java.awt.BorderLayout(0, 0));
        
        lblClienteJava = new javax.swing.JLabel();
        lblClienteJava.setText("Cliente Java");
        lblClienteJava.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        lblClienteJava.setFont(new java.awt.Font("Segoe UI Historic", java.awt.Font.BOLD | java.awt.Font.ITALIC, 18));
        panelTitulo.add(lblClienteJava, java.awt.BorderLayout.CENTER);
        
        panelUsuario = new javax.swing.JPanel();
        panelUsuario.setBorder(javax.swing.BorderFactory.createTitledBorder("Datos Usuario"));
        jPanelNorte.add(panelUsuario, java.awt.BorderLayout.CENTER);
        panelUsuario.setLayout(new java.awt.BorderLayout(0, 0));
        
        panel_1 = new javax.swing.JPanel();
        panelUsuario.add(panel_1, java.awt.BorderLayout.NORTH);
        panel_1.setLayout(new java.awt.GridLayout(1, 4, 0, 0));
        
        lblUser = new javax.swing.JLabel("Nombre:");
        lblUser.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        panel_1.add(lblUser);
        
        txtNombreU = new javax.swing.JTextField();
        txtNombreU.setColumns(10);
        panel_1.add(txtNombreU);
        
        lblNewLabel = new javax.swing.JLabel("Server Ip:");
        lblNewLabel.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        panel_1.add(lblNewLabel);
        
        txtServerIp = new javax.swing.JTextField();
        panel_1.add(txtServerIp);
        txtServerIp.setColumns(10);
        
        panel_3 = new javax.swing.JPanel();
        panelUsuario.add(panel_3, java.awt.BorderLayout.SOUTH);
        
        btnConectar = new javax.swing.JButton("Conectar");
        btnConectar.addActionListener(e -> {
        	generarConexion();
        });
        panel_3.add(btnConectar);
        
        btnDesconectar = new javax.swing.JButton("Desconectar");
        btnDesconectar.addActionListener(e -> {
        	try {
				cerrarConexion();
			} catch (IOException | TimeoutException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
        });
        panel_3.add(btnDesconectar);

        jPanelCentro.setBorder(javax.swing.BorderFactory.createTitledBorder("Chat"));
        jPanelCentro.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanelCentro, java.awt.BorderLayout.CENTER);
        
        listChat = new javax.swing.JList<javax.swing.JPanel>();
        listChat.setVisibleRowCount(10);
        listChat.setDragEnabled(true);
        chatModel = new javax.swing.DefaultListModel<javax.swing.JPanel>();
        listChat.setAutoscrolls(false);
        
        listChat.setModel(chatModel);
        listChat.setCellRenderer(new ItemPanelRenderer());
        listChat.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);
        jPanelCentro.add(new javax.swing.JScrollPane(listChat), java.awt.BorderLayout.CENTER);

        jPanelSur.setBorder(javax.swing.BorderFactory.createTitledBorder("Mensaje"));
        jPanelSur.setLayout(new java.awt.BorderLayout());

        
        txtMensaje.setRows(4);
        txtMensaje.setAutoscrolls(false);
        jPanelSur.add(new javax.swing.JScrollPane(txtMensaje), java.awt.BorderLayout.CENTER);

        btnEnviar.setText("Enviar");
        btnEnviar.addActionListener(e -> {
			try {
				enviarMensaje();
			} catch (java.io.IOException | java.util.concurrent.TimeoutException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		});
        
        jPanelSur.add(btnEnviar, java.awt.BorderLayout.EAST);
        

        getContentPane().add(jPanelSur, java.awt.BorderLayout.PAGE_END);

        pack();
    }
	
	
	
	/*                         Funciones                                 */
	
	public void iniciar() {
		this.setVisible(true);
		habilitarMensajeria(false);
	}
	
	
	
	
	
	public void generarConexion()  {
		if(getIpServer().length() != 0 && getNameUser().length() != 0) {
			if(controlador.estaServerDisponible(getIpServer())) {
				if(controlador.estaUsuarioDisponible(getNameUser())) {
					cbxDestinatario.setModel(new javax.swing.DefaultComboBoxModel<String>(controlador.usuariosDisponibles(getNameUser())));
					if(cbxDestinatario.getItemCount()!=0) {
						habilitarMensajeria(true);
						habilitarDesconectar(true);
						javax.swing.JOptionPane.showMessageDialog(this, "Conexión exitosa");
						setColaDestinatario();
					}
					else {
						habilitarMensajeria(false);
						habilitarDesconectar(true);
						javax.swing.JOptionPane.showMessageDialog(this, "No hay usuarios disponibles, intente otra vez");
					}
				}else {
					javax.swing.JOptionPane.showMessageDialog(this, "El usuario ya está en uso");
					try {
						controlador.cerrarConexion();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (TimeoutException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				
			} else javax.swing.JOptionPane.showMessageDialog(this, "No se logró la conexión con el Servidor RabbitMq");
			
		}else javax.swing.JOptionPane.showMessageDialog(this, "Complete los Campos necesarios");
		
	}
	
	
	// Agregar mensaje en la interfaz
	public void agregarMensaje(String r, int v) {
		String u;
		if(v == 1)  u = "yo"; // si v=1 es el mensaje que envia 
		else u = getDestinatario(); // si v=2 el mensaje que recibe 
        chatModel.addElement(createItemPanel(r, v, u)); // agragar al jList un elemento de tipo JPanel
        
    }
	// Funcion para crear el panel
	private javax.swing.JPanel createItemPanel(String mensaje, int tipo, String usuario) {
		//Trabajar en el mensaje en unos espacios determinados
		String aux = contarCaracteres(mensaje, 38);
		// panel para agregar a la lista
		javax.swing.JPanel panel = new javax.swing.JPanel(new java.awt.BorderLayout()); 
		panel.setPreferredSize(new java.awt.Dimension(panel.getPreferredSize().width, 40+(16*(aux.split("\n").length - 1))));
		// panel para crear un espacio de para el chat      
        javax.swing.JPanel p1 = new javax.swing.JPanel();
        p1.setBackground(java.awt.Color.WHITE);
        p1.setPreferredSize(new java.awt.Dimension(75, 40+(16*(aux.split("\n").length - 1))));
        // crear text area para el mensaje
        javax.swing.JTextArea m = new javax.swing.JTextArea(aux);
    	m.setBorder(javax.swing.BorderFactory.createTitledBorder(usuario));
    	m.setFont(new java.awt.Font(java.awt.Font.MONOSPACED, java.awt.Font.ITALIC, 12));
    	// agregar paneles
        if(tipo == 1) panel.add(p1, java.awt.BorderLayout.WEST);
        else panel.add(p1, java.awt.BorderLayout.EAST);
        panel.add(m, java.awt.BorderLayout.CENTER);
        return panel;
    }
	// funcion que devuelve una string de espacios fijos para el mensaje a publicar
	public String contarCaracteres(String c, int n) {
		String[] lines = c.split("\n");
		java.util.List<String> substrings = new java.util.ArrayList<String>();
		for (String line : lines) {
		    if (line.length() <= n) {
		        substrings.add(line);
		    } else {
		        int startIndex = 0;
		        int endIndex = n;
		        while (endIndex < line.length()) {
		        	if(line.charAt(endIndex) != ' ' && line.charAt(endIndex-1) != ' ') substrings.add(line.substring(startIndex, endIndex)+"-");
		        	else substrings.add(line.substring(startIndex, endIndex));
		            startIndex = endIndex;
		            endIndex += n;
		        }
		        if (startIndex < line.length()) {
		            substrings.add(line.substring(startIndex));
		        }
		    }
		}
		String result = String.join("\n", substrings);
		return result;
	}
	// plase auxiliar para ingresar un jpanel en un jlist
	private class ItemPanelRenderer implements javax.swing.ListCellRenderer<javax.swing.JPanel> {
        @Override
        public java.awt.Component getListCellRendererComponent(javax.swing.JList<? extends javax.swing.JPanel> list, javax.swing.JPanel value, int index,
                boolean isSelected, boolean cellHasFocus) {
            if (isSelected) {
                value.setBackground(javax.swing.UIManager.getColor("List.selectionBackground"));
                value.setForeground(javax.swing.UIManager.getColor("List.selectionForeground"));
            } else {
                value.setBackground(list.getBackground());
                value.setForeground(list.getForeground());
            }
            return value;
        }
	}
	// Getters para los campos de texto
	public String getMensaje() {
        return txtMensaje.getText();
    }
	
	public String getDestinatario() {
		if(cbxDestinatario.getSelectedItem() == null) return null;
		else  return cbxDestinatario.getSelectedItem().toString();
	}
	
	public String getIpServer(){
		return txtServerIp.getText();
	}
	
	public String getNameUser() {
		return txtNombreU.getText();
	}
	// Termina Getters
	
	public void enviarMensaje() throws java.io.IOException, java.util.concurrent.TimeoutException {
        String message = getMensaje();
        if (!message.isEmpty()) {
        	controlador.enviarMensaje(message, getIpServer());
            agregarMensaje(message,1);
            txtMensaje.setText("");
            
        }
    }
	// funcion para el control de botones, textos y ComboBox.
	public void habilitarMensajeria(boolean b) {
		
		cbxDestinatario.setEnabled(b);
		txtMensaje.setEditable(b);
		btnEnviar.setEnabled(b);
		
		
		txtNombreU.setEditable(!b);
		txtServerIp.setEditable(!b);
		habilitarDesconectar(b);
		
		
	}
	public void habilitarDesconectar(boolean b) {
		btnDesconectar.setEnabled(b);
		btnDesconectar.setVisible(b);

		btnConectar.setEnabled(!b);
		btnConectar.setVisible(!b);
		
	}
	// cargar destinatarios en el JComboBox para las colas
	public void setColaDestinatario() {
		if(controlador.cambiarDestinatario(getDestinatario())) {
			javax.swing.JOptionPane.showMessageDialog(this, "Usted se conectó con "+ getDestinatario());
			chatModel.clear();
		}
	}
	
	
	// antes de cerrar la ventana al cerrar la interfaz
	public void al_cerrar() throws IOException, TimeoutException {
		controlador.cerrarConexion();
		dispose();
	}
	// funcion para cerrar la conexion
	public void cerrarConexion() throws IOException, TimeoutException {
		controlador.cerrarConexion();
		habilitarMensajeria(false);
		habilitarDesconectar(false);
		//0101001
	}

}
