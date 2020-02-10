import java.util.ArrayList;
import java.util.Scanner;

public class p2_허진호 {
    public static int solve(Integer num, int total){
        int temp = 0;

        if(num == 0){
            return 1;
        }

        if(num >= 1){
            temp += solve(num-1, total+1);
        }

        if(num >= 2){
            temp += solve(num-2, total+1);
        }

        if(num >= 3){
            temp += solve(num-3, total+1);
        }

        return temp;
    }
    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();

        ArrayList<Integer> number = new ArrayList<Integer>();

        for(int i=0; i<t; i++){
            Integer a = scan.nextInt();
            number.add(a);
        }

        for(int i=0; i<t; i++){
            System.out.println(solve(number.get(i), 0));
        }
    }
}
