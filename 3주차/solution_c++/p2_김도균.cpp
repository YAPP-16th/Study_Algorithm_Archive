#include <cstdio>
#include <queue>
#define MAX 100
using namespace std;

int map[MAX][MAX];
int checked[MAX][MAX];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {-1, 1, 0, 0};
int n,m;
bool inRange(int x, int y) 
{
    if(x >= 0 && x<n  && y >= 0 && y < m)
        return true;
    return false;
}
void bfs(int x, int y)
{
    queue<pair<int, int> > q;
    q.push(make_pair(x, y));
    checked[x][y] = 1;
    while (!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (inRange(nx, ny))
            {
                if (checked[nx][ny] == 0 && map[nx][ny] == 1)
                {
                    q.push(make_pair(nx, ny));
                    checked[nx][ny] = checked[x][y] + 1;
                }
            }
        }
    }
}

int main(void)
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            scanf("%1d", &map[i][j]);
    }
    bfs(0, 0);
    printf("%d\n",checked[n-1][m-1]);
    return 0;
}
