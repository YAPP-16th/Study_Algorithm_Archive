#include <iostream>
#include <algorithm>
using namespace std;
int dp[100001];
int main(void)
{
    int n;
    cin >> n;
    for(int i = 1; i <= n ; i++) 
    {
        dp[i] = i;
        for(int j = 1; j*j <= i ; j++)
        {
            dp[i] = min(dp[i],dp[i-j*j] + 1);
        }
    }
    cout << dp[n] << endl;
    return 0;
}
