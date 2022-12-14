package BlockCypher;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;


public class BlockCypher {
    public String filenameToEncrypt;
    public String filenameEncrypted;
    public String filenameKey;

    BufferedImage img;

    public BlockCypher() throws Exception{
        this.filenameToEncrypt = System.getProperty("user.dir") + "\\EncryptionFiles\\plain.bmp";
        this.filenameKey = System.getProperty("user.dir") + "\\EncryptionFiles\\key.txt";
        this.filenameEncrypted = System.getProperty("user.dir") + "\\EncryptionFiles\\crypto.bmp";
        System.out.println(this.filenameToEncrypt);

        this.img  = ImageIO.read(new File(filenameToEncrypt));
        int height = img.getHeight();
        int width = img.getWidth();

        System.out.println(height + "  " + width + " ");

    }

    public byte bmpToByte(BufferedImage img){
        
       return blockArray;
    }
}
