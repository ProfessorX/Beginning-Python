#include <stdio.h>

int main()
{
    int n;
    int i;
    int c;
    int a;
    n = 1;
    i = 1;
    c = a;
    a = 1;

    printf("Enter the number of rows of Floyd's triangle to print\n");
    scanf("%d", &n);
    
    for (i=1; i<=n; i++){
        for (c=1; c<=i; c++){
            printf("%d ", a);
            a++;
}
        printf("\n");
}
    // return 0;
    
}
