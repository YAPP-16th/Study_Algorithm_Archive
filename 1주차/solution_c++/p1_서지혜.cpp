#include <stdio.h>
using namespace std;

int main() {
	int E,S,M;
	int year =1;
	int result = 0;
	scanf("%d %d %d", &E, &S, &M);
	
	while(1) {
		if((year-E)%15==0 && (year-S)%28==0 && (year-M)%19==0) {
			result = year;
			break;
		}
		year++;
	}
	
	printf("%d" ,result);
	return 0;
}