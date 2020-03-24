#include <cstdio>
using namespace std;

int main() {
	int l = 1, p, v;
	int t = 0;
	while(true) {
		scanf("%d %d %d", &l, &p, &v);
		if(l == 0) {
			break;
		}
		int usage = 0;
		
		usage += (v / p) * l;
		usage += v % p > l ? l : v % p;
		
		printf("Case %d: %d\n", ++t, usage);
	}
	return 0;
}
