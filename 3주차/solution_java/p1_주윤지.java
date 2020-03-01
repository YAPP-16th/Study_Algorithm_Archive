
import java.util.*;

class Pair {
    int x;
    int y;

    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public static class Main{
        static int n;
        static int m;
        static int[] dx = {1, -1, 0, 0};
        static int[] dy = {0, 0, 1, -1};
        //인접한 상,하,좌,우 칸을 순서쌍으로 이용하려고 정의
        static int[][] box;
        static int[][] value;

        static Queue<Pair> q = new LinkedList<Pair>();

        static void bfs(){
            while(!q.isEmpty()){
                Pair p = q.remove();
                int x = p.x;
                int y = p.y;

                for(int i = 0; i < 4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if(nx >= 0 && ny >= 0 && nx < n && ny < m ){
                        if(box[nx][ny] == 0 && value[nx][ny] == -1){
                            box[nx][ny] = 1;
                            value[nx][ny] = value[nx][ny] + 1;
                            q.add(new Pair(nx,ny));
                        }
                    }
                }
            }
        }

        static void check(){
            int day = 1;
            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++) {
                    if (box[i][j] == 0) {
                        System.out.println("-1");
                        return;
                    }
                    if (value[i][j] > day) {
                        day = value[i][j];
                    }
                }
            }
            System.out.println(day);
        }

        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int m = sc.nextInt();

            boolean ripen = true;

            box = new int[n][m];
            value = new int[n][m];

            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++){
                    box[i][j] = sc.nextInt();
                    if(box[i][j] == 1){
                        value[i][j] = 0;
                        q.add(new Pair(i,j));
                    }
                    if(box[i][j] == 0 && ripen){
                        ripen = false;
                    }
                }

                if(ripen){
                    System.out.println(0);
                }
                else{
                    bfs();
                    check();
                }
            }

        }


    }


}