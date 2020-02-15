import java.util.ArrayList;
import java.util.Scanner;

public class p2_허진호 {
    public static int solve(Integer num){
        int count = 0;

        if(num == 0){
            return 1;
        }

        if(num >= 1){
            count += solve(num-1);
        }

        if(num >= 2){
            count += solve(num-2);
        }

        if(num >= 3){
            count += solve(num-3);
        }

        return count;
    }
    
    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();

        ArrayList<Integer> number = new ArrayList<Integer>();

        for(int i=0; i<t; i++){
            number.add(scan.nextInt());
        }

        for(int i=0; i<t; i++){
            System.out.println(solve(number.get(i)));
        }
    }
}
