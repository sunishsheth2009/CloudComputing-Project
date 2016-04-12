import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.*;
import java.util.*;
 
public class Master_Socket implements Runnable
{
 
   	public Master_Socket()
	{
	}
	private static Socket s;
	public static String [] ipaddresses = new String [50];
public static String [] port_nos = new String [50];
public static int number_of_ipaddresses=0;
	public void run()
	{
		
		try 
		{
			ServerSocket listener = new ServerSocket(25000);
			try
			{	
        			while (true) 
				{
                			Socket socket = listener.accept();
                			try 
					{
						BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
						String socket_address_str = input.readLine();

						System.out.println(socket_address_str);
						
						
							 //STORES THE IPADDRESSES OF THE CLIENTS WHO PING 
						String sss = socket.getRemoteSocketAddress().toString();
						String socket_address []= sss.split(":");
						ipaddresses[number_of_ipaddresses] = socket_address[0].substring(1,socket_address[0].length());
						port_nos[number_of_ipaddresses]  = "25000";
						System.out.println(ipaddresses[number_of_ipaddresses] +"    "+ port_nos[number_of_ipaddresses]);
					
						
						number_of_ipaddresses += 1;

					
					ping_Client(0,"HEY USER WHAT DO YOU WANT TO DO ? \n");
                			} 
					finally 
					{
                				socket.close();
                			}
           			}
			}
			finally
			{
				listener.close();
			}
		
        	}
        	catch(Exception e) 
		{
        	  	e.printStackTrace();
        	}

	}
	static public void ping_Client(int user_name,String messagea)
	{
		
	 try
        {
            String host = "node1";
            int port = 25000;
            InetAddress address = InetAddress.getByName(host);
		
            s = new Socket(ipaddresses[user_name], port);
 
            //Send the message to the server
            OutputStream os = s.getOutputStream();
            OutputStreamWriter osw = new OutputStreamWriter(os);
            BufferedWriter bw = new BufferedWriter(osw);
 
            String sendMessage = "\n";
            bw.write(messagea);
            bw.flush();
            System.out.println("Message sent to the server : "+messagea);		////WE SEND THE QUESTION TO THE SPECIFIC USER HERE 
 
            //Get the return message from the server
            InputStream is = s.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            String message = br.readLine();
            System.out.println("Message received from the server : " +message);	//WE GET THE REPLY BACK FROM THE CLIENT HERE , IF WE WANT TO SCALE OR MIGRATE OR WHATEVER
	
        }
        catch (Exception exception)
        {
            exception.printStackTrace();
        }
        finally
        {
            //Closing the socket
            try
            {
                s.close();
            }
            catch(Exception e)
            {
                e.printStackTrace();
            }
	}
	}
 
    public static void main(String[] args)
    {
        Master_Socket serv = new Master_Socket();
	new Thread(serv).start();
		
	}
}
