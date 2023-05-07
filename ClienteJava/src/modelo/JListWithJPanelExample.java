package modelo;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;

import javax.swing.DefaultListModel;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.ListCellRenderer;
import javax.swing.ListSelectionModel;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.border.EmptyBorder;

public class JListWithJPanelExample extends JFrame {

    private static final long serialVersionUID = 1L;

    public JListWithJPanelExample() {
        super("JList with JPanel Example");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Crear el modelo de la lista
        DefaultListModel<JPanel> model = new DefaultListModel<JPanel>();

        // Agregar elementos al modelo
        model.addElement(createItemPanel("Item 1", "Description 1"));
        model.addElement(createItemPanel("Item 2", "Description 2"));
        model.addElement(createItemPanel("Item 3", "Description 3"));
        model.addElement(createItemPanel("Item 4", "Description 4"));
        model.addElement(createItemPanel("Item 5", "Description 5"));

        // Crear la lista con el modelo y el renderizador personalizado
        JList<JPanel> list = new JList<JPanel>(model);
        list.setCellRenderer(new ItemPanelRenderer());
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        // Agregar la lista a un JScrollPane y añadirlo al contenedor principal
        JScrollPane scrollPane = new JScrollPane(list);
        add(scrollPane, BorderLayout.CENTER);

        // Establecer tamaño y visibilidad de la ventana
        setSize(400, 300);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private JPanel createItemPanel(String title, String description) {
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(new EmptyBorder(5, 5, 5, 5));
        panel.setBackground(Color.WHITE);
        JLabel titleLabel = new JLabel(title);
        JLabel descriptionLabel = new JLabel(description);
        panel.add(titleLabel, BorderLayout.NORTH);
        panel.add(descriptionLabel, BorderLayout.SOUTH);
        return panel;
    }

    private class ItemPanelRenderer implements ListCellRenderer<JPanel> {

        @Override
        public Component getListCellRendererComponent(JList<? extends JPanel> list, JPanel value, int index,
                boolean isSelected, boolean cellHasFocus) {
            if (isSelected) {
                value.setBackground(UIManager.getColor("List.selectionBackground"));
                value.setForeground(UIManager.getColor("List.selectionForeground"));
            } else {
                value.setBackground(list.getBackground());
                value.setForeground(list.getForeground());
            }
            return value;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new JListWithJPanelExample();
            }
        });
    }
}

