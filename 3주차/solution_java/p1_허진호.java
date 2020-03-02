package week3;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class p1_허진호 {
    private static Queue<Pair> queue = new LinkedList<Pair>();

    private static int[][] box= new int[1001][1001];
    private static int[] dx= {1, -1, 0, 0};
    private static int[] dy= {0, 0, -1, 1};

    static class Pair{
        int x;
        int y;
        int count;

        Pair(int x, int y, int count){
            this.x = x;
            this.y = y;
            this.count = count;
        }

    }

    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        int M = scan.nextInt();
        int N = scan.nextInt();
        int count = 0;

        // 박스 초기화
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                box[i][j] = scan.nextInt();

                //box 요소 중 1이 있을 경우 큐에 삽입
                if(box[i][j] == 1){
                    queue.add(new Pair(j, i, 0));
                }

            }
        }

        // 큐에서 하나씩 빼서
        while(!queue.isEmpty()){
            Pair t_pair = queue.poll();
            int t_count = t_pair.count;

            for(int i=0; i<4; i++){
                int t_x = t_pair.x + dx[i];
                int t_y = t_pair.y + dy[i];

                // 범위 내에서 상하좌우로 전파
                if( t_x < M && t_x >= 0 && t_y < N && t_y >= 0){
                    // 0일 경우 전파
                    if(box[t_y][t_x] == 0){
                        box[t_y][t_x] = 1;
                        queue.add(new Pair(t_x, t_y, t_count+1));

                        // 최대 카운트 갱신
                        if(t_count+1 > count){
                           count = t_count + 1;
                        }
                    }
                }
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(box[i][j] == 0){
                    System.out.println(-1);
                    return;
                }

            }
        }

        System.out.println(count);

    }
}
