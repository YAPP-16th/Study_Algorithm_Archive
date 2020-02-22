#include <cstdio>
#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);
    queue<int> q;
    for(int i = 1 ; i <= n ; i++) {
        q.push(i);
    }
    printf("<");
    while(!q.empty()) {
        if(q.size() != 1) {
            for(int i = 0 ; i < k-1 ; i++) {
                q.push(q.front());
                q.pop();
            }
            printf("%d, ", q.front());
            q.pop();
        }
        else {
            printf("%d",q.front());
            q.pop();
        }
    }
    printf(">\n");
    return 0;
}
