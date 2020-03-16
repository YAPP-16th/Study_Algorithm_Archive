#include <iostream>
#include <cstdio>
using namespace std;


int n;
int res; 
int col[16];

bool promising(int i ) {
    int k;
    bool flag;

    k = 1;
    flag = true;
    while( k < i && flag) {
        if(col[i] == col[k] || abs(col[i] - col[k]) == abs(i-k) ){
            flag = false;
        } 
        k++;
    }
    return flag;
}

void queens(int i ) {
    int j;
    if(promising(i)){ 
        if( i == n ) {
            res++;
        }
        else {
            for( j =1 ; j <= n ; j++) {
                col[i+1] = j;
                queens(i+1);
            }
        }
    }
}

int main(void) {
    scanf("%d", &n);
    for(int i = 1;  i <= n ; i++) {
        col[1] = i;
        queens(1);
    }
    //queens(0);
    printf("%d\n",res);
    return 0;
}
