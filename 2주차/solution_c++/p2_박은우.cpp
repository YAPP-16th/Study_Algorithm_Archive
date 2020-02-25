#include <iostream>
using namespace std;

int min(int a, int b) {
	if(a < b){
		return a;
	} else {
		return b;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int dp[100001];
	dp[0] = 0;
	int n = 0;
	cin >> n;
	for(int i = 1; i<=n; i++) {
		dp[i] = i;
	}
	for(int k = 2; k * k <= n; k++) {
		for(int i = 1; i <= n; i++) {
			if(i - k*k >= 0){
				dp[i] = min(dp[i - k * k] + 1, dp[i]);
			}
		}
	}
	cout << dp[n];
	return 0;
}
