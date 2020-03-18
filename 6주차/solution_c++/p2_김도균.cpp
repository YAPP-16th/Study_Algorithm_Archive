#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

char arr[1000][50];
int check[4];
int n, m;
int cnt;
string ans;

void input()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf(" %c", &arr[i][j]);
        }
    }
}

void init()
{
    for(int i = 0 ; i < 4 ; i++){
        check[i] = 0 ;
    }
}

int main(void)
{
    scanf("%d %d", &n, &m);
    input();

    for (int j = 0; j < m; j++)
    {
        init();
        for (int i = 0; i < n; i++)
        {
            switch(arr[i][j])
            {
                case 'A': check[0]++; break;
                case 'C': check[1]++; break;
                case 'G': check[2]++; break;
                case 'T': check[3]++; break;
            }
        }
        // printf("%d : " ,j+1);
        // for(int k = 0 ; k < 4 ; k++)
        // {
        //     printf("%d ",check[k]);
        // }
        int max = 0;
        for(int k = 0 ; k < 4 ;k++)
        {
            if(check[k] != 0)
                cnt += check[k];
        }
        for(int k = 0 ; k < 3 ; k++)
        {
            //if(check[k] < check[k+1]) 
            if(check[max] < check[k+1])
            {
                max = k + 1;
            }
        }
        switch(max)
        {
            case 0 : ans += 'A'; cnt-=check[0]; break;
            case 1 : ans += 'C'; cnt-=check[1]; break;
            case 2 : ans += 'G'; cnt-=check[2]; break;
            case 3 : ans += 'T'; cnt-=check[3]; break;
        }
    }

    cout<< ans << '\n';
    cout << cnt << '\n';

    return 0;
}
