/*
Name: David Weber
Matrikelnummer: 304305
 */
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;
import java.util.Date;

public class MainContent extends JPanel implements ActionListener
{
    private ArrayList<GenericTest> genericTests = new ArrayList<>();
    private JLabel label = new JLabel("Test Ergebniss");
    private GenericTest currentTest;
    private Diagram diagram = new Diagram(this);
    private JButton startTestButton = new JButton("Start Test");
    private JButton readValuesButton = new JButton("Read Values");
    private JButton exitButton = new JButton("Exit");
    private JComboBox comboBox = new JComboBox<>();
    private GroupLayout layout = new GroupLayout(this);


    public MainContent()
    {
        setLayout(layout);
        layout.setAutoCreateGaps(true);
        layout.setAutoCreateContainerGaps(true);
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.CENTER)
                .addComponent(diagram)
                .addGroup(layout.createSequentialGroup()
                        .addComponent(startTestButton)
                        .addComponent(readValuesButton)
                        .addComponent(exitButton)
                        .addComponent(label)
                )
                .addComponent(comboBox, 100, 150, 150)

        );
        layout.setVerticalGroup(
                layout.createSequentialGroup()
                        .addComponent(diagram)
                        .addGroup(layout.createParallelGroup()
                                .addComponent(startTestButton)
                                .addComponent(readValuesButton)
                                .addComponent(exitButton)
                                .addComponent(label)
                        )
                        .addComponent(comboBox, 20, 30, 30)
        );

        startTestButton.addActionListener(this);
        exitButton.addActionListener(this);
        readValuesButton.addActionListener(this);
        comboBox.addActionListener(this);

        startTestButton.setEnabled(false);


    }

    public void create(String result)
    {
        GenericTest test;
        if(result.contains("Schellong"))
        {
            test = new SchellongTest(result);
            ((SchellongTest) test).createRandom();
            genericTests.add(test);
            currentTest = test;
            startTestButton.setEnabled(true);
            comboBox.addItem(currentTest);
            comboBox.setSelectedItem(currentTest);
        }
        else if(result.contains("Fitness"))
        {
            test = new FitnessTest(result);
            ((FitnessTest) test).createRandom();
            genericTests.add(test);
            currentTest = test;
            startTestButton.setEnabled(true);
            comboBox.addItem(currentTest);
            comboBox.setSelectedItem(currentTest);
        }
    }

    public GenericTest getCurrentTest()
    {
        return currentTest;
    }

    @Override
    public void actionPerformed(ActionEvent e)
    {
        if(e.getSource() == startTestButton)
        {
            currentTest.startTest();
            label.setText(currentTest.analyzeValues());
        }
        else if(e.getSource() == exitButton)
        {
            System.exit(0);
        }
        else if(e.getSource() == comboBox)
        {
            currentTest = (GenericTest) comboBox.getSelectedItem();
            repaint(getDiagram().getX(), getDiagram().getY(), getDiagram().getWidth(), getDiagram().getHeight());
        }
        else if(e.getSource() == readValuesButton)
        {
            read();
        }
    }

    public void read()
    {
        JFileChooser fileChooser = new JFileChooser();
        int response = fileChooser.showOpenDialog(null);
        if(response == JFileChooser.APPROVE_OPTION)
        {
            try
            {
                BufferedReader reader = new BufferedReader(new FileReader(fileChooser.getSelectedFile().getAbsolutePath()));
                LineNumberReader count = new LineNumberReader(new FileReader(fileChooser.getSelectedFile().getAbsolutePath()));
                while(count.skip(Long.MAX_VALUE) > 0)
                {}
                int result = count.getLineNumber();
                if(result == 4)
                {
                    FitnessTest test = new FitnessTest("(Fitness)");
                    String str;
                    while((str = reader.readLine() )!= null)
                    {

                        String[] strs = str.split(" ");
                        test.getMeasurements().add(new Measurement(Integer.parseInt(strs[0]), Integer.parseInt(strs[1]), Integer.parseInt(strs[2]), new Date()));
                    }
                    reader.close();
                    genericTests.add(test);
                    currentTest = test;
                    comboBox.addItem(test);
                    repaint(getDiagram().getX(), getDiagram().getY(), getDiagram().getWidth(), getDiagram().getHeight());
                    startTestButton.setEnabled(true);
                }
                else if(result == 6)
                {
                    SchellongTest test = new SchellongTest("(Schellong)");
                    String str;
                    while((str = reader.readLine() )!= null)
                    {

                        String[] strs = str.split(" ");
                        test.getMeasurements().add(new Measurement(Integer.parseInt(strs[0]), Integer.parseInt(strs[1]), Integer.parseInt(strs[2]), new Date()));
                    }
                    genericTests.add(test);
                    currentTest = test;
                    comboBox.addItem(test);
                    repaint(getDiagram().getX(), getDiagram().getY(), getDiagram().getWidth(), getDiagram().getHeight());
                    startTestButton.setEnabled(true);
                }

            }
            catch(FileNotFoundException ex)
            {
                throw new RuntimeException(ex);
            } catch(IOException ex)
            {
                throw new RuntimeException(ex);
            }
        }
    }

    public ArrayList<GenericTest> getGenericTests()
    {
        return genericTests;
    }

    public void load(ArrayList<GenericTest> genericTests)
    {
        comboBox.removeAllItems();
        this.genericTests = genericTests;
        currentTest = genericTests.get(0);
        for(GenericTest genericTest: genericTests)
        {
            comboBox.addItem(genericTest);
        }
        comboBox.setSelectedItem(currentTest);
    }

    public Diagram getDiagram()
    {
        return diagram;
    }
}
