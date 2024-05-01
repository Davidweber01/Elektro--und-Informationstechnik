/*
Name: David Weber
Matrikelnummer: 304305
 */
import javax.swing.*;
import java.awt.*;

public class Diagram extends JPanel
{
    private MainContent mainContent;
    public Diagram(MainContent content)
    {
        super();
        this.mainContent = content;
        setOpaque(false);
        setLayout(null);
    }

    public void paintComponent(Graphics g)
    {
        Graphics2D g2d = (Graphics2D)g;
        g2d.drawLine(20, getHeight() - 20, getWidth() - 20, getHeight() - 20);
        g2d.drawLine(20, 20, 20, getHeight() - 20);
        g2d.drawLine(20, 20, 25, 30);
        g2d.drawLine(20, 20, 15, 30);
        g2d.drawLine(getWidth() - 20, getHeight() - 20, getWidth() - 30, getHeight() - 15);
        g2d.drawLine(getWidth() - 20, getHeight() - 20, getWidth() - 30, getHeight() - 25);
        g2d.drawString("Messwerte", getWidth() - 60, getHeight());
        g2d.translate(5, 20);
        g2d.rotate(Math.toRadians(90));
        g2d.drawString("Puls/Blutdruck",0, 0);
        g2d.rotate(-Math.toRadians(90));
        g2d.translate(-5, -20);


        if(mainContent.getCurrentTest() != null)
        {
            if(mainContent.getCurrentTest().getMeasurements() != null)
            {
                for(int i = 0; i < mainContent.getCurrentTest().getMeasurements().size(); i++)
                {
                    Measurement measurement = mainContent.getCurrentTest().getMeasurements().get(i);
                    int test = getHeight() - 20 - (measurement.getPulse() * (getHeight()- 40)/200);
                    g2d.fillOval(20 + getWidth() * i/mainContent.getCurrentTest().getMeasurements().size(), getHeight() - 20 - (measurement.getPulse() * (getHeight()- 40)/200), 5, 5);
                    g2d.fillOval(20 + getWidth() * i/mainContent.getCurrentTest().getMeasurements().size(), getHeight() - 20 - (measurement.getSys_blood() * (getHeight()- 40)/200), 5, 5);
                    g2d.fillOval(20 + getWidth() * i/mainContent.getCurrentTest().getMeasurements().size(), getHeight() - 20 - (measurement.getDia_blood() * (getHeight()- 40)/200), 5, 5);
                }
            }
        }


        g2d.dispose();
    }

    @Override
    public Dimension getPreferredSize()
    {
        Dimension layoutSize = super.getPreferredSize();
        int max = Math.max(layoutSize.width, layoutSize.height);
        return new Dimension(800, 200);
    }

}
