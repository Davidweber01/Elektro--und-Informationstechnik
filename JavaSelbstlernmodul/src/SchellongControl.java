/*
Name: David Weber
Matrikelnummer: 304305
 */
public class SchellongControl extends TestControl
{
    public SchellongControl()
    {
        super();
    }

    protected void stateMachine()
    {
        switch(state)
        {
            case 0:
                label.setText("Hinlegen und 1 Minute liegen bleiben");
                timer.setDelay(6000);
                timer.start();
                continueButton.setEnabled(false);
                state++;
                break;
            case 1:
                label.setText("Führen Sie eine Puls- und Blutdruckmessung aus!");
                continueButton.setEnabled(true);
                state++;
                break;
            case 2:
                label.setText("1 Minute liegen bleiben");
                timer.setDelay(6000);
                timer.start();
                continueButton.setEnabled(false);
                state++;
                break;
            case 3:
                label.setText("Führen Sie eine Puls- und Blutdruckmessung aus!");
                continueButton.setEnabled(true);
                state++;
                break;
            case 4:
                label.setText("1 Minute liegen bleiben");
                timer.setDelay(6000);
                timer.start();
                continueButton.setEnabled(false);
                state++;
                break;
            case 5:
                label.setText("Führen Sie eine Puls- und Blutdruckmessung aus!");
                continueButton.setEnabled(true);
                state++;
                break;
            case 7:
                label.setText("Aufstehen und Puls- und Blutdruckmessung ausführen!");
                continueButton.setEnabled(true);
                state++;
                break;
            case 8:
                label.setText("1 Minute stehen bleiben");
                timer.setDelay(6000);
                timer.start();
                continueButton.setEnabled(false);
                state++;
                break;
            case 9:
                label.setText("Führen Sie eine Puls- und Blutdruckmessung aus!");
                continueButton.setEnabled(true);
                state++;
                break;
            case 10:
                label.setText("1 Minute stehen bleiben");
                timer.setDelay(6000);
                timer.start();
                continueButton.setEnabled(false);
                state++;
                break;
            case 11:
                label.setText("Führen Sie eine Puls- und Blutdruckmessung aus!");
                continueButton.setEnabled(true);
                state++;
                break;
            default:
                setVisible(false);
                dispose();
        }
    }
}
