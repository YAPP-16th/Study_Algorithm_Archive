package week3;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class p2_허진호 {
    private static Queue<Pair> queue = new LinkedList<Pair>();

    private static int[][] box= new int[101][101];
    private static int[] dx= {1, -1, 0, 0};
    private static int[] dy= {0, 0, -1, 1};

    static class Pair{
        int x;
        int y;

        Pair(int x, int y){
            this.x = x;
            this.y = y;
        }

    }

    public static void main(String []args){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();
        int min = 100000000;

        // 미로 초기화
        for (int i = 0; i < N; i++) {
            String temp = scan.next();
            for (int j = 0; j < M; j++) {
                box[i][j] = Character.getNumericValue(temp.charAt(j));
            }
        }

        queue.add(new Pair(0, 0));

        // 큐에서 하나씩 빼서
        while(!queue.isEmpty()){
            Pair t_pair = queue.poll();

            // 도착 했을 때 최소 카운트 갱신
            if (t_pair.x == M - 1 && t_pair.y == N - 1) {
                break;
            }

            for(int i=0; i<4; i++){
                int t_x = t_pair.x + dx[i];
                int t_y = t_pair.y + dy[i];

                // 범위 내에서 상하좌우로 전파
                if( t_x < M && t_x >= 0 && t_y < N && t_y >= 0){
                    // 0일 경우 전파
                    if(box[t_y][t_x] == 1){
                        box[t_y][t_x] = box[t_pair.y][t_pair.x] + 1;
                        queue.add(new Pair(t_x, t_y));
                    }
                }
            }
        }

        System.out.println(box[N-1][M-1]);

    }
}
