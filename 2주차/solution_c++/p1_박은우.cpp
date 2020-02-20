#include <iostream>
#include <string>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string a;
	getline(cin, a);
	int length = a.length();
	int cnt = 0;
	int b = 0;
	for (int i = 0; i < length; i++) {
		if (a.at(i) == '(') {
			if (a.at(i + 1) == ')') {
				cnt += b;
				i++;
			}
			else {
				b++;
			}
		}
		else if (a.at(i) == ')') {
			b--;
			cnt++;
		}
	}
	cout << cnt;
	return 0;
}
