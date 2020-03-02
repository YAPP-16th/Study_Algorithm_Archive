package week3;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class p3_허진호 {
    private static Queue<Integer> queue = new LinkedList<Integer>();

    private static int[] com= new int[101];
    private static int[][] line = new int[101][101];

    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        int c_num = scan.nextInt();
        int l_num = scan.nextInt();

        // com 초기화
        for(int i=1; i<=c_num; i++){
            com[i] = i;
        }

        // line 초기화
        for(int i=0; i<l_num; i++){
            int x = scan.nextInt();
            int y = scan.nextInt();

            line[x][y] = 1;
            line[y][x] = 1;
        }

        // 1 컴퓨터 전파 시작
        for(int i=1; i<=c_num; i++){
            if(line[1][i] == 1){
                queue.add(i);
            }
        }

        // 큐에서 하나씩 빼서
        while(!queue.isEmpty()){
            int vi = queue.poll();

            // 전파된 컴퓨터가 1이면 생략
            if(com[vi] == 1){
                continue;
            }

            // 전파된 컴퓨터가 1이 아니면 1로 바꿔줌
            com[vi] = 1;

            // 전파된 컴퓨터가 다시 전파
            for(int i=1; i<=c_num; i++){
                if(line[vi][i] == 1 && com[i] != 1){
                    queue.add(i);
                }
            }

        }

        // 1로 감연된 컴퓨터 개수 카운트
        int count = 0;
        for(int i=1; i<=c_num; i++){
            if(com[i] == 1){
                count++;
            }
        }

        // 1을 제외한 컴퓨터 수 출력
        System.out.println(count-1);

    }
}
