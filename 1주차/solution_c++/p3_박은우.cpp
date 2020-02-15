#include <iostream>
using namespace std;

int digits(int n){
	int d = 0;
	while(n){
		n/=10;
		d++;
	}
	return d;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;
	int d = digits(n);
	if(d <= 1){
		cout << n;
		return 0;
	}
	int a = 10;
	int b = 9;
    int c = 9;
	for(int i = 2;i<d;i++) {
		a *= 10;
		b *= 10;
        c += b*i;
	}
	cout << c + (n - a)*d + d;
	// your code goes here
	return 0;
}
