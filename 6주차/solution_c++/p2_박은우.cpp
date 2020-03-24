#include <cstdio>
#include <map>
using namespace std;

int main() {
	int n, m;
	char dnas[1000][50];
	char hamming[1000];
	int distance=0;
	scanf("%d %d", &n, &m);
	for(int i=0;i<n;i++) {
		for(int j=0;j<m;j++) {
			scanf(" %c", &dnas[i][j]);
		}
	}
	
	char dna[4] = {'A', 'C', 'G', 'T'};
	
	for(int c=0;c<m;c++) {
		map<char, int> m;
		for(int r=0;r<n;r++) {
			m[dnas[r][c]]++;
		}
		int max=0;
		
		for(int k=0;k<4;k++) {
			if(max < m[dna[k]]) {
				max = m[dna[k]];
				hamming[c] = dna[k];
			}
		}
		for(int k=0;k<4;k++) {
			if(hamming[c] != dna[k]) {
				distance += m[dna[k]];
			}
		}
		
	}
	
	for(int i=0;i<m;i++) {
		printf("%c", hamming[i]);
	}
	printf("\n%d", distance);
	
	return 0;
}
