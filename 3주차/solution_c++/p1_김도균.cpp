#include <cstdio>
#include <queue>
using namespace std;

int arr[1001][1001];
queue< pair<int,int> > q;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int m,n;

bool inRange(int ny, int nx) {
    if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
        return true;
    }
    return false;
}

void bfs() {
    while(!q.empty()) {
        pair<int,int> np = q.front();
        q.pop();
        int y = np.first;
        int x = np.second;
        for(int i = 0 ; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            //short circuit
            if(inRange(ny,nx) && arr[ny][nx] == 0) {
                arr[ny][nx] = arr[y][x] +1;
                q.push(make_pair(ny,nx));
            }
        }
    }
}

int main(void)
{
    scanf("%d %d", &m, &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (arr[i][j] > 0)
            {
                q.push(make_pair(i, j));
            }
        }
    }
    bfs();
    int max = 0;
    for(int i = 0 ; i < n ; i++) {
        for(int j = 0 ;j < m ; j++) {
            if(arr[i][j] == 0) {
                printf("-1\n");
                return 0;
            }
            if(arr[i][j] > max) {
                max = arr[i][j];
            }
        }
    }
    printf("%d\n",max-1);
    return 0;
}
