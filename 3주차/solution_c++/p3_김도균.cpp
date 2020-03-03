#include <cstdio>
#include <queue>
using namespace std;

int map[101][101];
int checked[101];
int n;
int ans;

void bfs(int point)
{
	queue<int> q;
	q.push(point);
	checked[point] = 1;
	
	while (!q.empty())
	{
		int pair = q.front();
		q.pop();
		for (int i =1; i <= n; i++)
		{
			if (checked[i] == 0 && map[pair][i] == 1)
			{
				ans++;
				q.push(i);
				checked[i] = 1;
			}
		}
	}
}


int main(void)
{
	int com;
	scanf("%d %d", &n, &com);
	for (int i = 0; i < com; i++)
	{
		int y, x;
		scanf("%d %d", &y, &x);
		map[y][x] = map[x][y] = 1;
	}
	bfs(1);
	printf("%d\n", ans);
	return 0;
}
