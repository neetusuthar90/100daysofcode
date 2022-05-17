#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, i;
    int count = 0;
    int a[1000];
    scanf("%d\n", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        count = count + a[i];
    }
    printf("%d", count);

    return 0;
}
