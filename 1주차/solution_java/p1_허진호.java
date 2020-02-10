import java.util.ArrayList;
import java.util.Scanner;

public class p1_허진호 {

    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        int a, b, c;
        int count = 0;

        a = scan.nextInt();
        b = scan.nextInt();
        c = scan.nextInt();

        while(a+b+c != 3) {
            a = a-1;
            b = b-1;
            c = c-1;

            if(a <= 0) {
                a = 15;
            }
            if(b <= 0) {
                b = 28;
            }
            if(c <= 0) {
                c = 19;
            }
            count++;
        }

        System.out.println(count + 1);
    }
}
