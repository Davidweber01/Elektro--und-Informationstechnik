/*
Name: David Weber
Matrikelnummer: 304305
 */
import java.io.Serializable;

public class FitnessTest extends GenericTest implements Serializable
{

    public FitnessTest(String name)
    {
        super(name);
    }

    @Override
    public String analyzeValues()
    {
        return new String("Wenn sie den ganzen Test geschafft haben, sind sie vermutlich gesund.");
    }

    public void startTest()
    {
        super.startTest();
        new FitnessControl();
        analyzeValues();
    }

    public void createRandom()
    {
        readValues(4);
    }

    public String toString()
    {
        return new String(getName());
    }

}
