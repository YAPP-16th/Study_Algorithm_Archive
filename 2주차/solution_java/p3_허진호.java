package week2;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class p3_허진호 {
    private static Queue<Pair> queue = new LinkedList<Pair>();
    private static int current = 1000000000;

    static class Pair{
        int num;
        int total;

        Pair(int num, int total){
            this.num = num;
            this.total = total;
        }

    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();

        queue.add(new Pair(num, 0));

        while(!queue.isEmpty()){
            Pair temp = queue.poll();
            solve(temp.num, temp.total);
        }

        System.out.println(current);
    }

    public static void solve(int num, int total){

        if(current <= total){
            return;
        }

        if(num == 0){
            if(current > total){
                current = total;
            }

            return;
        }

        int a = 1;
        int b = 2;

        while(true){
            if(a*a <= num && b*b > num){
                break;
            }
            a++;
            b++;
        }

        for(int i=a; i>=1; i--){
            queue.add(new Pair(num - i* i, total+1));
        }

    }
}
