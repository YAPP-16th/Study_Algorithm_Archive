#include <stdio.h> 
#include <cstring> 
#include <queue>
 
using namespace std;
 
struct tomato {
    int y, x;
};
 
queue<tomato> q;

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0 , -1 };
 
int n, m, result = 0;
int box[1001][1001];
 
int main() {
    scanf("%d %d", &m, &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &box[i][j]);
            if (box[i][j] == 1) {
                q.push({ i, j });
            }
        }
    }
 
    while (!q.empty()) {
        int y = q.front().y;
        int x = q.front().x;
        q.pop();
 
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
	if(0 <= nx && 0 <= ny && nx < m && ny < n) {
            	    if (box[ny][nx] == 0) {
                    box[ny][nx] = box[y][x] + 1;
                    q.push({ ny, nx });
                }
	}
        }
    }
 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (box[i][j] == 0) { 
                printf("-1\n");
                return 0;
            }
            if (result < box[i][j]) {
                result = box[i][j];
            }
        }
    }
    printf("%d\n", result-1);
    return 0;
}
