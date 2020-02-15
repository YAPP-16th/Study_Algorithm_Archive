#include <iostream>
using namespace std;

int main() {
   int n,a=9, size=0, total = 0, b=1;
   cin >> n;
   int tmp = n;
   while(tmp>0) {
      tmp= tmp/10;
      size++;
   }
   if(size==1) {
      cout<< n;
      return 0;
   }
   total += a;
   b*=10;
   for(int i=2;i<size;i++) {
      a=a*10;
      total += i*a;
      b*=10;
   }
   total += size*(n-b+1);
   cout << total;
   return 0;
}
