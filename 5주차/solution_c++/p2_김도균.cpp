#include <bits/stdc++.h>
using namespace std;

char arr[20][20];
//bool visited[20][20];
bool alphabet[26];
int res;
int r, c;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, 1, -1};

bool inRange(int nx, int ny)
{
    if (nx >= 0 && nx < c && ny >= 0 && ny < r)
        return true;
    return false;
}

bool isCapital(char c)
{
    if (c >= 'A' && c <= 'Z')
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool promising(int ny, int nx)
{
    if (alphabet[arr[ny][nx] - 'A'] == true)
        return false;
    return true;
}

void solution(int y, int x, int step)
{
    if(step > res) 
        res = step;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (inRange(nx, ny) && promising(ny, nx))
        {
            step++;
            alphabet[arr[ny][nx] - 'A'] = true;
            solution(ny, nx, step);
            step--;
            alphabet[arr[ny][nx] - 'A'] = false;
        }
    }
}

int main(void)
{
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            scanf(" %c", &arr[i][j]);
        }
    }
    res++;
    alphabet[arr[0][0] - 'A'] = true;
    solution(0, 0 ,1);

    printf("%d\n", res);

    return 0;
}
