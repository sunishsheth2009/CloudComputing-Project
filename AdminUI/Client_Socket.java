import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

import javax.swing.JOptionPane;

public class Client_Socket implements Runnable
{

	public Client_Socket()
	{

	}

	public void run()
	{
		try
		{
			String serverAddress = JOptionPane.showInputDialog("Enter IP Address of a machine that is\n" +"running the date service on port 9090:");
			Socket s = new Socket(serverAddress, 9090);
			BufferedReader input = new BufferedReader(new InputStreamReader(s.getInputStream()));
			String answer = input.readLine();
			JOptionPane.showMessageDialog(null, answer);
			System.exit(0);
		}
		catch(Exception e)
		{
			e.printStackTrace();


		}

	}
	public static void main(String[] args) throws IOException 
	{
		Client_Socket c = new Client_Socket();
		new Thread(c).start();
        
        
	}
}
