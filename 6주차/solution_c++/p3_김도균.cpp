#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int ans = 0;
int n;
int maxi;
vector<pair<int,int> > vl;

bool cmp(pair<int, int> a, pair<int, int> b) 
{
    if(a.second == b.second )
        return a.first < b.first;
    else
        return a.second < b.second;
}

int main(void)
{
    scanf("%d",&n);
    for(int i = 0;  i < n ; i++) 
    {
        pair<int,int> l;
        scanf("%d %d",&l.first, &l.second);
        vl.push_back(l);
    }
    sort(vl.begin() , vl.end(),cmp);
    for(int i =0 ; i < n ; i++) 
    {
        if(maxi <= vl[i].first) 
        {
            maxi = vl[i].second;
            ans++;
        }
    }
    printf("%d\n",ans);
    return 0;
}
