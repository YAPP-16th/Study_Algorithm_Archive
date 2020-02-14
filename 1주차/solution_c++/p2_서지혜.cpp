#include <stdio.h>
 
 
int main()
{
	int array[11] = { 0 };
    int n;
    scanf("%d" ,&n);
    
    array[1] = 1;
    array[2] = 2;
    array[3] = 4;
    
	for(int i=0; i<n;i++) {
        int input;
        scanf("%d" ,&input);
        for(int j=4;j<=input;j++) {
        	array[j] = array[j-1] + array[j-2] + array[j-3];
        }
        printf("%d\n", array[input]);
    }
    
    return 0;
}
