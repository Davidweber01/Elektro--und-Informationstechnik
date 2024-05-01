/*
Name: David Weber
Matrikelnummer: 304305
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;

public class Frame extends JFrame implements ActionListener
{
    private MainContent mainContent = new MainContent();
    private JMenuBar menuBar = new JMenuBar();
    private JMenu menu = new JMenu("Test");
    private JMenuItem newTest = new JMenuItem("New");
    private JMenuItem startTest = new JMenuItem("Start");
    private JMenuItem readValues = new JMenuItem("Read Values");
    private JMenuItem safeTest = new JMenuItem("Safe");
    private JMenuItem loadTest = new JMenuItem("Load");
    private JMenuItem changeTestName = new JMenuItem("Change Name");
    private JMenuItem printTestToFile = new JMenuItem("Print(to File)");
    private JMenuItem exit = new JMenuItem("Exit");

    public Frame()
    {
        newTest.addActionListener(this);
        startTest.addActionListener(this);
        safeTest.addActionListener(this);
        loadTest.addActionListener(this);
        changeTestName.addActionListener(this);
        readValues.addActionListener(this);
        printTestToFile.addActionListener(this);
        exit.addActionListener(this);
        menu.add(newTest);
        menu.add(startTest);
        menu.add(readValues);
        menu.add(safeTest);
        menu.add(loadTest);
        menu.add(changeTestName);
        menu.add(printTestToFile);
        menu.add(exit);
        menuBar.add(menu);
        add(menuBar, BorderLayout.NORTH);
        add(mainContent, BorderLayout.CENTER);


        setSize(1000, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        pack();
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e)
    {
        if(e.getSource() == newTest)
        {
            CreateTestDialog dialog = new CreateTestDialog(null);
            if(dialog.isClosedByOk())
            {
                String result = dialog.getResult();
                mainContent.create(result);
                repaint(mainContent.getDiagram().getX(), mainContent.getDiagram().getY(), mainContent.getDiagram().getWidth(), mainContent.getDiagram().getHeight());
            }
        }
        else if(e.getSource() == startTest)
        {
            mainContent.getCurrentTest().startTest();
        }
        else if(e.getSource() == changeTestName)
        {
            new CreateTestDialog(mainContent.getCurrentTest());
        }
        else if(e.getSource() == safeTest)
        {
            try(FileOutputStream fileOut = new FileOutputStream("Tests");
                ObjectOutputStream out = new ObjectOutputStream(fileOut);
            )
            {
                out.writeObject(mainContent.getGenericTests());
            }
            catch(FileNotFoundException ex)
            {
                throw new RuntimeException(ex);
            }
            catch(IOException ex)
            {

            }
        }
        else if(e.getSource() == loadTest)
        {
            JFileChooser fileChooser = new JFileChooser();
            int response = fileChooser.showOpenDialog(null);
            if(response == JFileChooser.APPROVE_OPTION)
            {
                try(FileInputStream fileIn = new FileInputStream(fileChooser.getSelectedFile().getAbsolutePath()); ObjectInputStream in = new ObjectInputStream(fileIn);)
                {
                    mainContent.load((ArrayList<GenericTest>) in.readObject());
                } catch(IOException ex)
                {
                    ex.printStackTrace();
                } catch(ClassNotFoundException ex)
                {
                    ex.printStackTrace();
                }
            }
        }
        else if(e.getSource() == printTestToFile)
        {
            JFileChooser fileChooser = new JFileChooser();
            int response = fileChooser.showOpenDialog(null);
            if(response == JFileChooser.APPROVE_OPTION)
            {
                try
                {
                    PrintWriter printWriter = new PrintWriter(fileChooser.getSelectedFile().getAbsolutePath());
                    for(Measurement measurement: mainContent.getCurrentTest().getMeasurements())
                    {
                        measurement.print(printWriter);
                    }
                    printWriter.close();
                }
                catch(FileNotFoundException ex)
                {
                    throw new RuntimeException(ex);
                }
            }
        }
        else if(e.getSource() == readValues)
        {
            mainContent.read();
        }
        else if(e.getSource() == exit)
        {
            System.exit(0);
        }

    }
}
