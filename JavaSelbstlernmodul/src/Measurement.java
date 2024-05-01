/*
Name: David Weber
Matrikelnummer: 304305
 */
import java.io.PrintWriter;
import java.io.Serializable;
import java.util.Date;

public class Measurement implements Serializable
{
    private int pulse;
    private int sys_blood;
    private int dia_blood;
    private Date time;

    public Measurement(int pulse, int sys_blood, int dia_blood, Date time)
    {
        this.pulse = pulse;
        this.sys_blood = sys_blood;
        this.dia_blood = dia_blood;
        this.time = time;
    }

    public int getPulse()
    {
        return pulse;
    }

    public int getSys_blood()
    {
        return sys_blood;
    }

    public int getDia_blood()
    {
        return dia_blood;
    }

    public void print(PrintWriter p)
    {
        p.write(pulse + " " + sys_blood + " " + dia_blood + "\n");
    }
}
