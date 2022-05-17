#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, i;
    int a[1000];
    scanf("%d\n", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    for (unsigned i = n; i--;)
    {
        printf("%d ", a[i]);
    }

    return 0;
}
