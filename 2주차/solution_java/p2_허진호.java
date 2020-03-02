package week2;

import java.util.ArrayList;
import java.util.Scanner;

public class p2_허진호 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int K = scan.nextInt();

        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<Integer> answer = new ArrayList<>();

        for(int i=0; i<N; i++){
            list.add(i+1);
        }

        int i = K-1;
        while(list.size() > 0){
            while(i >= list.size()){
                i = i - list.size();
            }

            answer.add(list.get(i));
            list.remove(i);
            i = i+K-1;

        }

        String temp = answer.toString();
        temp = temp.substring(1, temp.length()-1);

        System.out.println("<" + temp + ">");

    }
}
