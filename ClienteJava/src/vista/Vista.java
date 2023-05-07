package vista;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public class Vista extends javax.swing.JFrame {

	private static final long serialVersionUID = 1L;                   
    public javax.swing.JButton btnEnviar;
    private javax.swing.JLabel jLabel1, jLabel2, jLabel3;
    public javax.swing.JPanel jPanelCentro, jPanelNorte, jPanelNorte1, jPanelSur;
    private javax.swing.JScrollPane jScrollPaneSur;
    public javax.swing.JTextField texIP, texNombre;
    public javax.swing.JTextArea txtMensaje;
    private javax.swing.JList<javax.swing.JPanel> listChat;
    private javax.swing.DefaultListModel<javax.swing.JPanel> chatModel;
    controlador.Controlador controlador;

	
	public Vista(controlador.Controlador controlador) {
		this.controlador = controlador;
		setAlwaysOnTop(true);
		initComponents();
		
	}
	private void initComponents() {

        jPanelNorte = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jPanelNorte1 = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();
        texNombre = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();
        texIP = new javax.swing.JTextField();
        jPanelCentro = new javax.swing.JPanel();
        jPanelSur = new javax.swing.JPanel();
        jScrollPaneSur = new javax.swing.JScrollPane();
        txtMensaje = new javax.swing.JTextArea();
        btnEnviar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Cliente Java");
        setMinimumSize(new java.awt.Dimension(350,500));

        jPanelNorte.setLayout(new java.awt.BorderLayout());

        jLabel1.setFont(new java.awt.Font("Segoe UI Historic", 3, 18)); // NOI18N
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("Chat Java");
        jPanelNorte.add(jLabel1, java.awt.BorderLayout.NORTH);

        jPanelNorte1.setLayout(new java.awt.GridLayout(1, 4));

        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        jLabel2.setText("Nombre:");
        jPanelNorte1.add(jLabel2);

        jPanelNorte1.add(texNombre);

        jLabel3.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        jLabel3.setText("Dirección IP:");
        jPanelNorte1.add(jLabel3);
        jPanelNorte1.add(texIP);

        jPanelNorte.add(jPanelNorte1, java.awt.BorderLayout.CENTER);

        getContentPane().add(jPanelNorte, java.awt.BorderLayout.PAGE_START);

        jPanelCentro.setBorder(javax.swing.BorderFactory.createTitledBorder("Chat"));
        jPanelCentro.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanelCentro, java.awt.BorderLayout.CENTER);
        
        listChat = new javax.swing.JList<javax.swing.JPanel>();
        listChat.setVisibleRowCount(10);
        
        chatModel = new javax.swing.DefaultListModel<javax.swing.JPanel>();
        listChat.setEnabled(false);
        listChat.setModel(chatModel);
        listChat.setCellRenderer(new ItemPanelRenderer());
        listChat.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);
        jPanelCentro.add(listChat, java.awt.BorderLayout.CENTER);

        jPanelSur.setBorder(javax.swing.BorderFactory.createTitledBorder("Mensaje"));
        jPanelSur.setLayout(new java.awt.BorderLayout());

        txtMensaje.setColumns(10);
        txtMensaje.setRows(2);
        jScrollPaneSur.setViewportView(txtMensaje);

        jPanelSur.add(jScrollPaneSur, java.awt.BorderLayout.CENTER);

        btnEnviar.setText("Enviar");
        btnEnviar.addActionListener(e -> {
			try {
				enviarMensaje();
			} catch (IOException | TimeoutException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		});
        
        jPanelSur.add(btnEnviar, java.awt.BorderLayout.EAST);
        

        getContentPane().add(jPanelSur, java.awt.BorderLayout.PAGE_END);

        pack();
    }
	
	public void agregarMensaje(String r, String v) {
		
        chatModel.addElement(createItemPanel(r, v));
        
    }
	
	private javax.swing.JPanel createItemPanel(String respuesta, String envio) {
		javax.swing.JPanel panel = new javax.swing.JPanel(new java.awt.GridLayout());
        
        javax.swing.JLabel r = new javax.swing.JLabel(respuesta);
        javax.swing.JLabel e = new javax.swing.JLabel(envio);
        r.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        e.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        panel.add(r);
        panel.add(e);
        return panel;
    }
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
	
	public String obtenerMensaje() {
        return txtMensaje.getText();
    }
	
	public void enviarMensaje() throws IOException, TimeoutException {
        String message = obtenerMensaje();
        if (!message.isEmpty()) {
        	controlador.enviarMensaje(message, texIP.getText());
            agregarMensaje("",message);
            
        }
    }
	public void iniciar() {
		this.setVisible(true);
	}

}
