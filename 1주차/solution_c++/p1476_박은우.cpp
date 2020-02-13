#include <iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//15 28 19
	int E, S, M;
	cin >> E >> S >> M;
	int e = 1, m = 1;
	for (int i = S; i <= 7980; i+=28) {
		if ((i - E) % 15 == 0 && (i - M) % 19 == 0) {
			cout << i;
			break;
		}
	}
    return 0;
}
