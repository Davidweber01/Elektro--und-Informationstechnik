/*
Name: David Weber
Matrikelnummer: 304305
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TestControl extends JDialog implements ActionListener
{
    private JPanel panel = new JPanel();
    protected JLabel label = new JLabel("Zum Starten Continue Drücken");
    protected JButton cancelButton = new JButton("Cancel");
    protected JButton continueButton = new JButton("Continue");
    protected int state = 0;
    protected Timer timer = new Timer(6000, this);
    private GroupLayout layout = new GroupLayout(panel);
    public TestControl()
    {
        setSize(350, 140);
        panel.setLayout(layout);
        layout.setAutoCreateGaps(true);
        layout.setAutoCreateContainerGaps(true);
        layout.setHorizontalGroup(layout.createParallelGroup()
                .addComponent(label)
                .addGroup(layout.createSequentialGroup()
                        .addComponent(cancelButton)
                        .addComponent(continueButton)
                )
        );
        layout.setVerticalGroup(layout.createSequentialGroup()
                .addComponent(label)
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.CENTER)
                        .addComponent(cancelButton)
                        .addComponent(continueButton)
                )
        );

        cancelButton.addActionListener(this);
        continueButton.addActionListener(this);

        add(panel);

        setLocationRelativeTo(null);
        setModalityType(DEFAULT_MODALITY_TYPE);
        setVisible(true);

    }

    protected void stateMachine()
    {

    }

    @Override
    public void actionPerformed(ActionEvent e)
    {
        if(e.getSource() == cancelButton)
        {
            setVisible(false);
            timer.stop();
            dispose();
        }
        else if(e.getSource() == continueButton)
        {
            stateMachine();
        }
        else if(e.getSource() == timer)
        {
            Toolkit.getDefaultToolkit().beep();
            stateMachine();
            timer.stop();
        }
    }
}
