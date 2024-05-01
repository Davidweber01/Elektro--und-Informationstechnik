/*
Name: David Weber
Matrikelnummer: 304305
 */
public class FitnessControl extends TestControl
{
    public FitnessControl()
    {
        super();
    }

    protected void stateMachine()
    {
        switch(state)
        {
            case 0:
                label.setText("Do 100 Push-Ups");
                state++;
                break;
            case 1:
                label.setText("Do 100 Sit-Ups");
                state++;
                break;
            case 2:
                label.setText("Do 100 Squats");
                state++;
                break;
            case 3:
                label.setText("Run 10 km");
                state++;
                break;
            default:
            setVisible(false);
            dispose();
        }
    }
}
