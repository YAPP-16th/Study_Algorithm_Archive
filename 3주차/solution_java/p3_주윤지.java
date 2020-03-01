import java.util.Scanner;

public class Virus {
    static int com; //computer 갯수 input
    static int pair; //쌍의 수 input
    static int count;
    static int visited[];
    static int period;
    static int line;
    static int map[][];

    static void dfs(int start){
        visited[start] = 1;
        for(int i = 1; i<com+1; i++){
            if(map[start][i] == 1 && visited[i] == 0){
                dfs(i);
                count++;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        com = sc.nextInt();
        pair = sc.nextInt();

        map = new int[com+1][com+1];
        visited = new int[com+1];

        for(int i = 0; i < pair; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            map[a][b] = map[b][a] = 1;
        }

        dfs(1);
        System.out.println(count);

    }
}
