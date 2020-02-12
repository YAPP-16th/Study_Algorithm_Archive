#include <iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//15 28 19
	int E, S, M;
	cin >> E >> S >> M;
	int e = 1, s = 1, m = 1;
	for (int i = 1; i <= 7980; i++) {
		if (E == e && S == s && M == m) {
			cout << i;
			break;
		}
		e = e % 15 + 1;
		s = s % 28 + 1;
		m = m % 19 + 1;
	}
    return 0;
}
