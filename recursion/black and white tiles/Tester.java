import java.util.Scanner;

class Tester {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input = in.nextLine();
        in.close();
        String [] tileArr = input.split(",");
        int noOfSteps = Utility.countSteps(tileArr);
        System.out.println(noOfSteps);
    }    
}

class Utility {
    static int countSteps(String [] tileArr){
        int counter =0;
        int n = tileArr.length;
        if (n<=3) return 1;
        int i = 0;
        while(i<(n-2)){
            if (tileArr[i+1] == "B"){
                i +=2;
            } else{
                if (tileArr[i+2] =="B"){
                    i+=1;
                } else{
                    i+=2;
                }
            }
            System.out.println("i -> "+i);
            counter +=1;
        }
        return counter;
    }
}

// ['W','W'];   1
// W,B,W    1
// W,B,W,W
// ['W', 'W', 'W', 'B', 'W', 'B', 'W']; 3
// W,W,B,W,W,B,W
// 0,1,2,3,4,5,6