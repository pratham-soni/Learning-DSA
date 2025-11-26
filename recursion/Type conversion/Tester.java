import java.util.Scanner;
public class Tester {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String name = scn.nextLine();

        String passwordGenerated = Utility.passGenerator(name);
        System.out.println(passwordGenerated);
        scn.close();
    }
}
class Utility {
    public static String passGenerator(String name){
        String password = "";
        int pl = name.length();
        char pe = name.charAt(pl -1);
        char fp = name.charAt(0);
        
        if (pl%2 == 0){
            password = ""+pe+pl+"@"+fp+"457"+pe;
        } else{
            password += ""+pe+pl+"!"+fp+"964"+pe;
        }
        return password;
    }
}