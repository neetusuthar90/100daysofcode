#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int n, d;
    int count = 0;
    scanf("%d", &n);
    while (n > 0)
    {
        d = n % 10;
        count = count + d;
        n = n / 10;
    }
    printf("%d", count);
    return 0;
}