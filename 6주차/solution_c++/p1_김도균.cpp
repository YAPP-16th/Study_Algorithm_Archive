#include <iostream>
#include <cstdio>
using namespace std;

int i = 1;

int main(void)
{
    int l, p, v;
    while (true)
    {
        scanf("%d %d %d",&l,&p,&v);
        if (l == 0 && p == 0 && v == 0)
            break;
        int ans = v/p * l;
        int remainder = (v% p > l) ? (l) : (v%p);
        ans += remainder;
        printf("Case %d: %d\n",i++, ans);
    }
    return 0;
}
