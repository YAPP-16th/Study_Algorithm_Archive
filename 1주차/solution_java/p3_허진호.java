import java.util.ArrayList;
import java.util.Scanner;

public class p3_허진호 {
    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        int a;
        int count = 0;

        a = scan.nextInt();

        while(a >= 1) {
            int temp = a;
            int temp_count = 1;

            while(temp >= 10){
                temp /= 10;
                temp_count++;
            }
            a--;
            count = count + temp_count;
        }
        System.out.println(count);

    }
}
