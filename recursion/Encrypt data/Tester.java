
public class Tester {
    public static void main(String[] args) {
        char ch = '<';
        int a = (int) ch;
        System.out.println(a);

        char numberChar = '5'; // Character representing the number 5

        // Explicitly cast the character to an integer to get its ASCII value
        int asciiValue = (int) numberChar; 

        System.out.println("The ASCII value of '" + numberChar + "' is: " + asciiValue);
    }
}
