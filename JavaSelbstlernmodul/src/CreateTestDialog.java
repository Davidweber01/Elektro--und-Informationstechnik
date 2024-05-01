/*
Name: David Weber
Matrikelnummer: 304305
 */
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CreateTestDialog extends JDialog implements ActionListener
{
    private GenericTest test;
    private JPanel panel = new JPanel();
    private String result;
    private boolean closedByOk = false;
    private JLabel nameLabel = new JLabel("Name:");
    private JLabel typeLabel = new JLabel("Type:");
    private JTextField textField = new JTextField();
    private String[] options = {"Schellong", "Fitness"};
    private JComboBox comboBox = new JComboBox<>(options);
    private JButton buttonCreate = new JButton("Create");
    private JButton buttonCancel = new JButton("Cancel");
    private GroupLayout layout = new GroupLayout(panel);
    public CreateTestDialog(GenericTest test)
    {
        this.test = test;
        setSize(220, 140);
        panel.setLayout(layout);
        layout.setAutoCreateGaps(true);
        layout.setAutoCreateContainerGaps(true);
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.CENTER)
                .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup()
                                .addComponent(nameLabel, 50, 50, 50)
                                .addComponent(typeLabel, 50, 50, 50)
                                .addComponent(buttonCancel, 75, 75, 75)
                        )
                        .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                                .addComponent(textField, 100, 100, 100)
                                .addComponent(comboBox, 100, 100, 100)
                                .addComponent(buttonCreate,75, 75, 75)
                        )
                )
        );
        layout.setVerticalGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup()
                        .addComponent(nameLabel, 20, 20, 20)
                        .addComponent(textField, 20, 20, 20)
                )
                .addGroup(layout.createParallelGroup()
                        .addComponent(typeLabel, 20, 20, 20)
                        .addComponent(comboBox, 20, 20, 20)
                )
                .addGroup(layout.createParallelGroup()
                        .addComponent(buttonCancel, 25, 25, 25)
                        .addComponent(buttonCreate, 25, 25, 25)
                )

        );

        buttonCreate.addActionListener(this);
        buttonCancel.addActionListener(this);

        if(test != null)
        {
            if(test.getName().contains("Schellong"))
            {
                comboBox.setSelectedItem("Schellong");
            }
            else if(test.getName().contains("Fitness"))
            {
                comboBox.setSelectedItem("Fitness");
            }
            comboBox.setEnabled(false);
        }

        add(panel);

        setLocationRelativeTo(null);
        setModalityType(DEFAULT_MODALITY_TYPE);
        setVisible(true);
    }

    public String getResult()
    {
        return result;
    }

    public boolean isClosedByOk()
    {
        return closedByOk;
    }

    @Override
    public void actionPerformed(ActionEvent e)
    {
        if(e.getSource() == buttonCreate)
        {
            closedByOk = true;
            if(test == null)
            {
                result = textField.getText() + "(" + comboBox.getSelectedItem() + ")";
            }
            else
            {
                test.setName(textField.getText() + "(" + comboBox.getSelectedItem() + ")");
            }
            setVisible(false);
            dispose();
        }
        else if(e.getSource() == buttonCancel)
        {
            closedByOk = false;
            setVisible(false);
            dispose();
        }
    }
}
