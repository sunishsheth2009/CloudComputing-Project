import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Random;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import javax.swing.Timer;

class ImagePanel extends JPanel {

        URL[] urls;
        BufferedImage[] images;
        Random rand = new Random();

	public String path_real;

        public ImagePanel(String path) {
            
            setBackground(Color.BLACK);

            Timer timer = new Timer(500, new ActionListener(){
                @Override
                public void actionPerformed(ActionEvent e) {
                    repaint();
                }
            });
            timer.start();
		path_real = path;	
		
        }
	
	 private int random() {
            int index = rand.nextInt(2);
            return index;
        }

        @Override
        protected void paintComponent(Graphics g) {
		
		urls = new URL[5];
            try {
                urls[0] = new URL(path_real);
		urls[1] = new URL(path_real);
                images = new BufferedImage[5];
                images[0] = ImageIO.read(urls[0]);
		images[1] = ImageIO.read(urls[1]);
		

            } catch (MalformedURLException ex) {
                ex.printStackTrace();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
		
            super.paintComponent(g);
            BufferedImage img = images[random()];
            g.drawImage(img, 0, 0, this.getWidth(), this.getHeight(), null);
        }

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(400, 400);
        }
    }
