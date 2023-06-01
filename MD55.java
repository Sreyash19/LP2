import java.security.*;
public class MD55 
{
   public static void main(String a[]) 
 {
      try
       {
	MessageDigest md = MessageDigest.getInstance("MD5"); 
         System.out.println("Message digest object info:");
         System.out.println("Algorithm=" + md.getAlgorithm());
         System.out.println(" Provider=" + md.getProvider());
         System.out.println(" ToString=" + md.toString());
         String input = "";
         md.update(input.getBytes()); 
         byte[] output = md.digest(); 
         System.out.println();
         System.out.println("MD5"+ bytesToHex(output)); 
         input = "abc";
         md.update(input.getBytes()); 
         output = md.digest();
         System.out.println();
         System.out.println("MD5" + bytesToHex(output)); 
         input = "abd";
	 md.update(input.getBytes()); 
         output = md.digest();
            System.out.println();
    System.out.println("MD5" + bytesToHex(output));
    input = "abcdefghijklmnopqrstuvwxyz";
 md.update(input.getBytes()); 
    output = md.digest(); 
    System.out.println();
    System.out.println("MD5" + bytesToHex(output)); 
    input = "ABCDEFGHIJKLMNOPQRSTUVVVXYZ"; 
    md.update(input.getBytes());
    output = md.digest(); 
    System.out.println();
    System.out.println("MD5" + bytesToHex(output)); 
    System.out.println();
    } 
   catch (Exception e) 
  { 
    System.out.println("Exception:" + e);
    }
}
private static String bytesToHex(byte[] b)
 {
  char hexDigit[] ={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
  StringBuffer buf = new StringBuffer();
  	for (int j = 0; j < b.length; j++) 
	{
	    buf.append(hexDigit[(b[j] >> 4) & 0x0f]);
	    buf.append(hexDigit[b[j] & 0x0f]);
	  }
	  return buf.toString();
 }
}