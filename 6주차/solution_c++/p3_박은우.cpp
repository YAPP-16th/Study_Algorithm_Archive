#include <cstdio>
#include <algorithm>
#define p pair<int, int>
using namespace std;

bool cmp(p s, p e){
	if(s.second == e.second) {
		return s.first < e.first;
	}
	return s.second < e.second;
}

int main() {
	int n;
	p meeting[100000];
	scanf("%d", &n);
	int s, e;
	for(int i=0;i<n;i++) {
		scanf("%d %d", &s, &e);
		meeting[i] = make_pair(s, e);
	}
	sort(meeting, meeting+n, cmp);
	
	int cnt = 0, end = 0;
	
	for(int i=0;i<n;i++) {
		if(end <= meeting[i].first) {
			end = meeting[i].second;
			cnt++;
		}
	}
	
	printf("%d", cnt);
	return 0;
}
