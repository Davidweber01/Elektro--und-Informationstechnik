/*
Name: David Weber
Matrikelnummer: 304305
 */
import java.io.Serializable;

public class SchellongTest extends GenericTest implements Serializable
{

    public SchellongTest(String name)
    {
        super(name);

    }

    @Override
    public String analyzeValues()
    {
        int mittelwertDiaStehen = (getMeasurements().get(0).getDia_blood() + getMeasurements().get(1).getDia_blood() + getMeasurements().get(2).getDia_blood())/3;
        int mittelwertSysStehen = (getMeasurements().get(0).getSys_blood() + getMeasurements().get(1).getSys_blood() + getMeasurements().get(2).getSys_blood())/3;
        if((mittelwertDiaStehen - getMeasurements().get(4).getDia_blood()) > 10 && (mittelwertSysStehen - getMeasurements().get(4).getSys_blood()) > 20)
        {
            return new String("Besuchen sie einen Arzt!");
        }
        return new String("Sie sind vermutlich gesund. Bei weiteren Fragen wenden Sie sich an einen Arzt!");
    }

    public void startTest()
    {
        super.startTest();
        new SchellongControl();
        analyzeValues();
    }

    public void createRandom()
    {
        readValues(6);
    }

    public String toString()
    {
        return new String(getName());
    }

}
