/*
Name: David Weber
Matrikelnummer: 304305
 */
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.Random;

public abstract class GenericTest implements Serializable
{
    private ArrayList<Measurement> measurements = new ArrayList<>();
    private Date time = new Date();
    private String name = new String();

    public GenericTest(String name)
    {
        this.name = name;
    }

    public String getName()
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public ArrayList<Measurement> getMeasurements()
    {
        return measurements;
    }

    public void readValues(int anzahl)
    {
        Random rnd = new Random();
        for(int i = 0; i < anzahl; i++)
        {
            int rndPulse = rnd.nextInt(100);
            int rndSysBlood = rnd.nextInt(100);
            int rndDiaBlood = rnd.nextInt(100);

            measurements.add(new Measurement(rndPulse, rndSysBlood, rndDiaBlood, time));
        }

    }

    public abstract String analyzeValues();

    public void startTest()
    {
        time = new Date();
    }

}
