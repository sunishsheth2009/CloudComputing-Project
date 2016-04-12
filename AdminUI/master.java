import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.concurrent.*;
import java.io.*;


//cd Desktop/DBDesign/Project/java


//----------------------------------Class extending JFrame--------------------
public class master extends JFrame
{
/*
public int numClicks=0;
public JLabel ;
public JLabel ;
public JLabel ;

public JTextField ;
public JTextField ;
public JTextField ;



public JLabel error_label;

static public Object rowData[][] = new Object[5000][5000];
Object columnNames[] = { "branch_id", "book_id", "Title","Author(s)","No_Of_Copies"};
Object selected_data[];

*/
public int table_length=0;
public String virtual_machine;
public String mig_source;
public String mig_dest;

public JLabel vcpu_label;
public JLabel memory_label;
public JLabel disk_label;

public JLabel parameter_label;

public JButton node_0_button;
public JButton node_1_button;
public JButton node_2_button;
public JButton node_3_button;
public JButton node_4_button;
public JButton node_5_button;

public JButton refresh_button;
public JButton users_button;

public JButton scale_button;

//ALSO REQUIRES SCALE UP + SCALE OUT + SCALE DOWN

public JRadioButton vcpu_radio;
public JRadioButton memory_radio;
public JRadioButton disk_radio;

public ButtonGroup scale_radio;

public JTextField parameter;

public JTextField migration_source_text;
public JTextField migration_destination_text;
public JButton migration_source_button;
public JButton migration_button;

public JLabel migration_source_label;
public JLabel migration_destination_label;

static public Object rowData[][] = new Object[5000][5000];
Object columnNames[] = { "Virtual Machines"};
Object selected_data[];

public ImagePanel node_0_panel;
//public JPanel node_0_panel;
public ImagePanel node_1_panel;
public ImagePanel node_2_panel;
public ImagePanel node_3_panel;
public ImagePanel node_4_panel;
public ImagePanel node_5_panel;


public static master frame;

public static node node_0_frame;
public static node node_1_frame;
public static node node_2_frame;
public static node node_3_frame;
public static node node_4_frame;
public static node node_5_frame;

/*
public JButton fine_button;

public static String author_name;
public static String book_id_name;
public static String title_name;
public static Newuser n;
public static Search frame;
public static Checkout c;
public static Checkin cin;
public static Fine cfine;
public static int populate_checkout_flag=0;
public static int populate_checkin_flag=0;

public static int Branch_id;
public static String Book_id;
public static int No_of_copies;
*/

public master(String header)
{
	super(header);
	setSize(1400,1000);
	setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			
			
	setLayout(null);	//TO AVOID THE DEFAULT BORDER LAYOUT MANAGER 

	final JTable table = new JTable(rowData, columnNames);

	JScrollPane scrollPane = new JScrollPane(table);

	vcpu_radio= new JRadioButton(" VCPU ");
	memory_radio= new JRadioButton(" Memory ");
	disk_radio =  new JRadioButton(" Disk ");

	scale_radio = new ButtonGroup();
	
	vcpu_label = new JLabel(" VCPU ");
	memory_label = new JLabel(" Memory ");
	disk_label = new JLabel(" Disk ");

	parameter_label = new JLabel("Parameter");

	scale_radio.add(vcpu_radio);
	scale_radio.add(memory_radio);
	scale_radio.add(disk_radio);


	parameter = new JTextField("");

	node_0_button = new JButton("NODE 0");
	node_1_button = new JButton("NODE 1");
	node_2_button = new JButton("NODE 2");
	node_3_button = new JButton("NODE 3");
	node_4_button = new JButton("NODE 4");
	node_5_button = new JButton("NODE 5");

	scale_button = new JButton("Scale");

	refresh_button = new JButton("REFRESH !");
	users_button = new JButton("USERS !");
	
	migration_source_text = new JTextField("");
	migration_destination_text = new JTextField("");

	migration_source_label = new JLabel("Enter Node ");
	migration_destination_label = new JLabel("Destination");

	migration_source_button = new JButton("SHOW VMS !");
	migration_button = new JButton("Migrate !");	

	node_0_frame = new node("NODE 0","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_idle.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_system.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_total.png");
	node_1_frame = new node("NODE 1","file:///var/lib/ganglia/graphs/cloud1/node1/cpu_idle.png","file:///var/lib/ganglia/graphs/cloud1/node1/cpu_system.png","file:///var/lib/ganglia/graphs/cloud1/node1/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node1/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node1/mem_free.png","file:///var/lib/ganglia/graphs/cloud1/node1/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node1/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node1/disk_free.png","file:///var/lib/ganglia/graphs/cloud1/node1/disk_total.png");
	node_2_frame = new node("NODE 2","file:///var/lib/ganglia/graphs/cloud1/node2/cpu_idle.png","file:///var/lib/ganglia/graphs/cloud1/node2/cpu_system.png","file:///var/lib/ganglia/graphs/cloud1/node2/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node2/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node2/mem_free.png","file:///var/lib/ganglia/graphs/cloud1/node2/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node2/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node2/disk_free.png","file:///var/lib/ganglia/graphs/cloud1/node2/disk_total.png");
	node_3_frame = new node("NODE 3","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_idle.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_system.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_total.png");
	node_4_frame = new node("NODE 4","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_idle.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_system.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_total.png");
	node_5_frame = new node("NODE 5","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_idle.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_system.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/mem_total.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_free.png","file:///var/lib/ganglia/graphs/cloud1/node0/disk_total.png");	

	node_0_panel = new ImagePanel("file:///var/lib/ganglia/graphs/cloud1/node0/cpu_wio.png");
	node_1_panel = new ImagePanel("file:///var/lib/ganglia/graphs/cloud1/node1/cpu_wio.png");
	node_2_panel = new ImagePanel("file:///var/lib/ganglia/graphs/cloud1/node2/cpu_wio.png");
	node_3_panel = new ImagePanel("file:///var/lib/ganglia/graphs/cloud1/node1/cpu_wio.png");
	node_4_panel = new ImagePanel("file:///var/lib/ganglia/graphs/cloud1/node1/cpu_wio.png");
	node_5_panel = new ImagePanel("file:///var/lib/ganglia/graphs/cloud1/node1/cpu_wio.png");

	vcpu_label.setSize(100,40);
	memory_label.setSize(100,40);
	disk_label.setSize(100,40);

	parameter_label.setSize(100,40);
	
	scrollPane.setSize(200,200);

	vcpu_radio.setSize(15,15);
	memory_radio.setSize(15,15);
	disk_radio.setSize(15,15);
	
	parameter.setSize(200,20);
	
		

	node_0_button.setSize(150,20);
	node_1_button.setSize(150,20);
	node_2_button.setSize(150,20);	
	node_3_button.setSize(150,20);	
	node_4_button.setSize(150,20);
	node_5_button.setSize(150,20);

	scale_button.setSize(150,20);

	refresh_button.setSize(150,20);
	users_button.setSize(150,20);	
	
	migration_source_text.setSize(200,20);
	migration_destination_text.setSize(200,20);

	migration_source_button.setSize(150,20);
	migration_button.setSize(150,20);
	
	migration_source_label.setSize(100,100);
	migration_destination_label.setSize(100,100);


	node_0_panel.setSize(300,300);
	node_1_panel.setSize(300,300);
	node_2_panel.setSize(300,300);
	node_3_panel.setSize(300,300);
	node_4_panel.setSize(300,300);
	node_5_panel.setSize(300,300);

	vcpu_label.setLocation(1060,450);
	memory_label.setLocation(1060,475);
	disk_label.setLocation(1060,500);

	parameter_label.setLocation(935,535);

	scale_button.setLocation(1035,570);

	node_0_button.setLocation(20,30);
	node_1_button.setLocation(170,30);
	node_2_button.setLocation(320,30);
	node_3_button.setLocation(470,30);
	node_4_button.setLocation(620,30);
	node_5_button.setLocation(770,30);

	vcpu_radio.setLocation(1035,460);
	memory_radio.setLocation(1035,490);
	disk_radio.setLocation(1035,520);
	
	parameter.setLocation(1035,540);



	refresh_button.setLocation(1035,390);
	users_button.setLocation(1035,430);

	migration_source_text.setLocation(1035,50);
	migration_source_label.setLocation(935,5);
	

	migration_source_button.setLocation(1035,80);
	scrollPane.setLocation(1035,110);
	
	migration_destination_label.setLocation(935,295);
	migration_destination_text.setLocation(1035,330);

	migration_button.setLocation(1035,360);

			

	node_0_panel.setLocation(20,60);
	node_1_panel.setLocation(320,60);
	node_2_panel.setLocation(620,60);
	node_3_panel.setLocation(20,360);
	node_4_panel.setLocation(320,360);
	node_5_panel.setLocation(620,360);


	add(node_0_button);
	add(node_1_button);
	add(node_2_button);
	add(node_3_button);
	add(node_4_button);
	add(node_5_button);
	
	add(parameter_label);
	add(scale_button);

	add(vcpu_radio);
	add(memory_radio);
	add(disk_radio);
	
	add(parameter);

	add(refresh_button);
	add(users_button);

	add(migration_source_text);
	add(migration_destination_text);
	add(migration_source_button);
	add(migration_button);	

	add(migration_source_label);
	add(migration_destination_label);

	add(vcpu_label);
	add(memory_label);
	add(disk_label);

	add(node_0_panel);
	add(node_1_panel);
	add(node_2_panel);
	add(node_3_panel);
	add(node_4_panel);
	add(node_5_panel);
	
	node_0_panel.setVisible(false);
	node_1_panel.setVisible(false);
	node_2_panel.setVisible(false);
	node_3_panel.setVisible(false);
	node_4_panel.setVisible(false);
	node_5_panel.setVisible(false);

	node_0_frame.setVisible(false);
	node_1_frame.setVisible(false);
	node_2_frame.setVisible(false);
	node_3_frame.setVisible(false);
	node_4_frame.setVisible(false);
	node_5_frame.setVisible(false);
	add(scrollPane);

	final int flag[] = new int[6];



	node_0_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			
			if(flag[0]==0)
			{
				node_0_panel.setVisible(true);
				flag[0]=1;
				node_0_frame.setVisible(true);
			}			
			else
			{ 
				node_0_panel.setVisible(false);
				flag[0]=0;
				node_0_frame.setVisible(false);
			}	
				
			/*try{
			Process p = Runtime.getRuntime().exec("python hello.py");
			 BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
			String ret = in.readLine();
			System.out.println("value is : "+ret);
			}
			catch(Exception ee)
			{
				ee.printStackTrace();
			}*/
			
			
			
		}
	});

	node_1_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			if(flag[1]==0)
			{
				node_1_panel.setVisible(true);
				flag[1]=1;
				node_1_frame.setVisible(true);
			}			
			else
			{ 
				node_1_panel.setVisible(false);
				flag[1]=0;
				node_1_frame.setVisible(false);
			}
			
			
			
		}
	});	

	node_2_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			if(flag[2]==0)
			{
				node_2_panel.setVisible(true);
				flag[2]=1;
				node_2_frame.setVisible(true);
			}			
			else
			{ 
				node_2_panel.setVisible(false);
				flag[2]=0;
				node_2_frame.setVisible(false);
			}
			
			
			
		}
	});	

	node_3_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			if(flag[3]==0)
			{
				node_3_panel.setVisible(true);
				flag[3]=1;
				node_3_frame.setVisible(true);
			}			
			else
			{ 
				node_3_panel.setVisible(false);
				flag[3]=0;
				node_3_frame.setVisible(false);
			}
			
			
		}
	});	

	node_4_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			if(flag[4]==0)
			{
				node_4_panel.setVisible(true);
				flag[4]=1;
				node_4_frame.setVisible(true);
			}			
			else
			{ 
				node_4_panel.setVisible(false);
				flag[4]=0;
				node_4_frame.setVisible(false);
			}
			
			
		}
	});	

	node_5_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			if(flag[5]==0)
			{
				node_5_panel.setVisible(true);
				flag[5]=1;
				node_5_frame.setVisible(true);
			}			
			else
			{ 
				node_5_panel.setVisible(false);
				flag[5]=0;
				node_5_frame.setVisible(false);
			}
			
			
		}
	});
	
	

	migration_source_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			
			String mig_source = migration_source_text.getText();
			
			if(mig_source.equals("node0") || mig_source.equals("node1") || mig_source.equals("node2"))
			{
				/*PYTHON CODE TO GET RUNNING VIRTUAL MACHINE LIST FROM virsh list*/
				try{
					Process p = Runtime.getRuntime().exec("ssh "+ mig_source+" cd /home/"+mig_source+"/Desktop/main && python migrate.py && scp Output.txt node0:/home/node0/Desktop/main && logout");
			 		BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
					String ret = in.readLine();
					System.out.println("value is : "+ret);
					Thread.sleep(2000);
				}
				catch(Exception ee)
				{
					ee.printStackTrace();
				}

							

				try{
					FileReader input = new FileReader("Output.txt");
					BufferedReader bufRead = new BufferedReader(input);
					String myLine = null;
				
					int i=0;
					/*RESETS THE TABLE*/
					for(int x=0;x<table_length;x++)
					{
					rowData[x][0]="";
			
					}
					table_length=0;	
					while ( (myLine = bufRead.readLine()) != null)
					{    
						System.out.println(myLine);
  						rowData[i][0]=myLine;
						i++;
						table_length++;
					}
					repaint();
				}
				catch(Exception ie)
				{
					ie.printStackTrace();
				} 
				//node_0_panel.validate();

			}
			else 
			{
				System.out.println("Enter the correct node !");
			}
			
		}
	});	

	

	migration_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e)
		{
			AbstractButton button = (AbstractButton)e.getSource();
			int row=0;
			int col=0;
        		if(e.getActionCommand().equals(button.getActionCommand()))
			{	
				 row = table.getSelectedRow();
            			 col = table.getSelectedColumn();
			}	
			virtual_machine=(String)table.getValueAt(row,0);
			mig_source=migration_source_text.getText();
			mig_dest=migration_destination_text.getText();
		
			System.out.println(virtual_machine+mig_source+mig_dest);
			try{
					Process p = Runtime.getRuntime().exec("ssh "+ mig_source+" virsh migrate --live "+virtual_machine+" qemu+ssh://"+mig_dest+"/system --unsafe && logout");
			 		BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
					String ret = in.readLine();
					System.out.println("value is : "+ret);
					Thread.sleep(2000);
				}
				catch(Exception ee)
				{
					ee.printStackTrace();
				}
			
			
			
		}

	});


	users_button.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e)
		{
	
	
		}

	});		
	








}

public static void main(String[] args)
	{
			frame = new master("MASTER DASHBOARD!");
			frame.setVisible(true);
	
			

	}

}
