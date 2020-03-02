package week2;

import java.util.Scanner;

public class p1_허진호 {
    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        String input = scan.next();
        input = input.replace("()", ".");

        int total = 0;
        int temp = 0;
        int temp_t = 0;

        for(int i=0; i<input.length(); i++){
            if(input.charAt(i) == '('){
                temp++;
            }
            else if(input.charAt(i) == ')'){
                temp--;
                temp_t++;
            }
            else{
                total += temp_t + temp;
                temp_t = 0;
            }
//            System.out.println("temp :" + temp);
//            System.out.println("total :" + total);
        }
        System.out.println(total + temp_t);
    }
}
