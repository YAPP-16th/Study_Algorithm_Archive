// 왜 에러인지는 알겠는데 못 고치고 있습니다.ㅠㅠ

import java.util.*;

class Index{
    int x = -1;
    int y = -1;
    LinkedList<Index> linkedList = new LinkedList<Index>();
    int dist = -1;
    boolean visited = false; //방문 여부 확인
}

public class Miro {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int [][] miro = new int[n][m];
        Index[][] index = new Index[n][m];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                index[i][j] = new Index();
                index[i][j].dist = n*m; //거리는 최대로 초기화
            }
        }

        sc.nextLine();

        for(int i = 0; i < n; i++){
            String line = sc.nextLine();
            for(int j = 0; j < m; j++){
                miro[i][j] = Integer.parseInt(line.substring(j,j+1)); //미로에 값넣기
                index[i][j].x = i;
                index[i][j].y = j; //초기화
            }
        }

        Queue<Index> q = new LinkedList<Index>();
        index[0][0].dist = 1;
        q.add(index[0][0]);

        while(q.peek() != null){
            if(q.peek() == null){
                break;
            }
            else if(q.peek().visited == true){
                q.poll();
                continue;
            }
            else{
                q.peek().visited = true;
            }
        } //방문한 노드는 넘어감, 방문안했으면 방문 체크 후 밑의 연산 시작

        int nx = q.peek().x;
        int ny= q.peek().y;

        if(nx!=0 && index[nx-1][ny] == 1){
            if(index[nx-1][ny].dist > q.peek().dist +1 ){
                index[nx - 1][ny].dist = q.peek().dist + 1;
            }
            q.add(index[nx-1][ny]);
        } //위

        if(nx!=n-1 && index[nx+1][ny] == 1){
            if(index[nx+1][ny].dist > q.peek().dist + 1){
                index[nx+1][ny].dist = q.peek().dist + 1;
            }
            q.poll();
        } //아래

        if(ny!=m-1 && index[nx][ny+1] == 1){
            if(index[nx][ny+1].dist > q.peek().dist + 1){
                index[nx][ny+1].dist = q.peek().dist + 1;
            }
            q.add(index[nx][ny+1]);
        } //오른쪽

        if(ny!=0 && index[nx][ny-1] == 1){
            if(index[nx][ny-1].dist > q.peek().dist + 1){
                index[nx][ny-1].dist = q.peek().dist + 1;
            }
            q.add(index[nx][ny-1]);
        } //왼쪽

        System.out.println(index[n-1][m-1].dist); //출력값
    }


}
