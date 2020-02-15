#include <iostream>
using namespace std;

int fact(int n) {
	int f = 1;
	for(int i=2;i<=n;i++) {
		f*=i;
	}
	return f;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	while(T--) {
		int n;
		int answer=0;
		cin >> n;
		for(int i=0;i<=n;i++) {
			for(int j=0;j<=n/2;j++) {
				for(int k=0;k<=n/3;k++) {
					if(i + 2*j + 3*k == n) {
						answer += fact(i+j+k)/(fact(i)*fact(j)*fact(k));
					}
				}
			}
		}
		cout << answer << endl;
		
	}
	// your code goes here
	return 0;
}
