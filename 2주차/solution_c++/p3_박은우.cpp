#include <iostream>
#include <cmath>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0;
	int k = 0;
	cin >> n >> k;
	int circle[5000] = {0, };
	int d = k - 1;
	cout << "<" << k;
	circle[k - 1] = -1;
	for(int i = 1; i< n; i++) {
		for(int j = 0; j < k;j++){
			d = (d+1)%n;
			if(circle[d] < 0){
				j--;
			}
		}
		cout << ", " << d + 1;
		circle[d] = -1;
	}
	cout << ">";
	return 0;
}
