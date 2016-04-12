import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.concurrent.*;
import java.io.*;

public class node extends JFrame
{

	public static node frame;
	
	public JCheckBox memory_check;
	public JCheckBox io_check;
	public JCheckBox cputime_check;

	public JLabel memory_label;
	public JLabel io_label;
	public JLabel cputime_label;
	

	public ImagePanel memorya_panel;
	//public JPanel node_0_panel;
	public ImagePanel memoryb_panel;
	public ImagePanel memoryc_panel;

	public ImagePanel cpua_panel;
	//public JPanel node_0_panel;
	public ImagePanel cpub_panel;
	public ImagePanel cpuc_panel;
	public ImagePanel cpud_panel;
	
	//public JPanel node_0_panel;
	public ImagePanel diska_panel;
	public ImagePanel diskb_panel;




//, String cpu1, String cpu2, String cpu3, String cpu4, String mem1, String mem2, String mem3, String disk1, String disk2

	public node(String nodename, String cpu1, String cpu2, String cpu3, String cpu4, String mem1, String mem2, String mem3, String disk1, String disk2)
	{
		super(nodename);
		setSize(1800,1000);
		setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
			
			
		setLayout(null);	//TO AVOID THE DEFAULT BORDER LAYOUT MANAGER 


		memory_check = new JCheckBox("Memory");
		io_check = new JCheckBox("CPU");
		cputime_check = new JCheckBox("Disk");
			
		memory_label = new JLabel("Memory");
		cputime_label = new JLabel("CPU");
		io_label = new JLabel("Disk");
	
		//mem_panel = new JPanel();
		//cpu_panel = new JPanel();
		//input_panel = new JPanel();

		memorya_panel = new ImagePanel(mem1);
		memoryb_panel = new ImagePanel(mem2);
		memoryc_panel = new ImagePanel(mem3);

		cpua_panel = new ImagePanel(cpu1);
		cpub_panel = new ImagePanel(cpu2);
		cpuc_panel = new ImagePanel(cpu3);
		cpud_panel = new ImagePanel(cpu4);
		
		diska_panel = new ImagePanel(disk1);
		diskb_panel = new ImagePanel(disk2);

				

		//mem_panel.setSize(300,700);
		//cpu_panel.setSize(300,700);
		//input_panel.setSize(300,700);

		memorya_panel.setSize(400,300);
		memoryb_panel.setSize(400,300);
		memoryc_panel.setSize(400,300);
	
		cpua_panel.setSize(400,300);
		cpub_panel.setSize(400,300);
		cpuc_panel.setSize(400,300);
		cpud_panel.setSize(400,300);

		diska_panel.setSize(400,300);
		diskb_panel.setSize(400,300);

		memory_check.setSize(15,15);
		cputime_check.setSize(15,15);
		io_check.setSize(15,15);

		memory_label.setSize(100,40);
		cputime_label.setSize(100,40);
		io_label.setSize(100,40);

		memory_check.setLocation(50,15);
		cputime_check.setLocation(200,15);
		io_check.setLocation(350,15);

		memory_label.setLocation(70,0);
		cputime_label.setLocation(220,0);
		io_label.setLocation(370,0);

		//mem_panel.setLocation(20,60);
		//cpu_panel.setLocation(20,360);
		//input_panel.setLocation(20,720);

		memorya_panel.setLocation(20,60);
		memoryb_panel.setLocation(440,60);
		memoryc_panel.setLocation(880,60);

		cpua_panel.setLocation(20,360);
		cpub_panel.setLocation(440,360);
		cpuc_panel.setLocation(880,360);
		cpud_panel.setLocation(1300,360);

		diska_panel.setLocation(20,700);
		diskb_panel.setLocation(440,700);
		

		add(memory_check);
		add(cputime_check);
		add(io_check);	

		add(memory_label);
		add(cputime_label);
		add(io_label);

		//add(mem_panel);
		//add(cpu_panel);
		//add(input_panel);

		add(memorya_panel);
		add(memoryb_panel);
		add(memoryc_panel);

		add(cpua_panel);
		add(cpub_panel);
		add(cpuc_panel);
		add(cpud_panel);

		add(diska_panel);
		add(diskb_panel);

		//mem_panel.setVisible(true);
		//cpu_panel.setVisible(true);
		//input_panel.setVisible(true);	
	
		memorya_panel.setVisible(false);
		memoryb_panel.setVisible(false);
		memoryc_panel.setVisible(false);

		cpua_panel.setVisible(false);
		cpub_panel.setVisible(false);
		cpuc_panel.setVisible(false);
		cpud_panel.setVisible(false);

		diska_panel.setVisible(false);
		diskb_panel.setVisible(false);

		final int flag[] = new int[3];

		memory_check.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			
			if(flag[0]==0)
			{
				AbstractButton abstractButton = (AbstractButton) e.getSource();
        			boolean selected = abstractButton.getModel().isSelected();
       				 System.out.println(selected);
				memorya_panel.setVisible(true);
				memoryb_panel.setVisible(true);
				memoryc_panel.setVisible(true);
				flag[0]=1;
				
			}			
			else
			{ 
				memorya_panel.setVisible(false);
				memoryb_panel.setVisible(false);
				memoryc_panel.setVisible(false);
				flag[0]=0;
				
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

	cputime_check.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			
			if(flag[1]==0)
			{
				AbstractButton abstractButton = (AbstractButton) e.getSource();
        boolean selected = abstractButton.getModel().isSelected();
        System.out.println(selected);

				cpua_panel.setVisible(true);
				cpub_panel.setVisible(true);
				cpuc_panel.setVisible(true);
				cpud_panel.setVisible(true);
				flag[1]=1;
			}			
			else
			{ 
				cpua_panel.setVisible(false);
				cpub_panel.setVisible(false);
				cpuc_panel.setVisible(false);
				cpud_panel.setVisible(false);
				flag[1]=0;
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

	io_check.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e) 
		{
			
			if(flag[2]==0)
			{
				AbstractButton abstractButton = (AbstractButton) e.getSource();
        boolean selected = abstractButton.getModel().isSelected();
        System.out.println(selected);
				diska_panel.setVisible(true);
				diskb_panel.setVisible(true);
				flag[2]=1;
				
			}			
			else
			{ 
				diska_panel.setVisible(false);
				diskb_panel.setVisible(false);
				flag[2]=0;
				
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

	
	}

}
