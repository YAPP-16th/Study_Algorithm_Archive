#include <cstdio>
#include <cmath>

int main(void) {
    int n;
    scanf("%d",&n);
    int sum = 1;

    for(int i = 2 ; i <= n ; i++) {
        // for(int j = 1 ; j <= 8 ; j++) {
        //     if (pow(10.0,j-1) <= i && pow(10.0, j) > i ) {
        //         sum += j;
        //     }
        // }
        if(i < 10) {
            sum += 1;
        }
        else if(i<100) {
            sum += 2;
        }
        else if(i< 1000) {
            sum += 3;
        }
        else if(i < 10000) {
            sum += 4;
        }
        else if(i < 100000) {
            sum += 5;
        }
        else if(i < 1000000) {
            sum += 6;
        }
        else if(i < 10000000) {
            sum += 7;
        }
        else if(i < 100000000) {
            sum += 8;
        }
        else {
            sum += 9;
        }
    }
    printf("%d\n", sum);
    return 0;
}
