/*  (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)*/

#include <cstdio>

int main(void) {
    int e,s,m;
    scanf("%d %d %d",&e, &s, &m);
    
    int num = s;
    while(true) {
        int e_flag, m_flag;
        if(e == 15) {
            e_flag = 0;
        } else {
            e_flag = e;
        }
        if(m == 19) {
            m_flag = 0;
        } else {
            m_flag = m;
        }
        
        if( num % 15 == e_flag  && num%19==m_flag) {
            break;
        }
        num += 28;
    }
    printf("%d\n",num);
    return 0;
}
