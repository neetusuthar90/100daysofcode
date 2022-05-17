#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    char s[1000];
    int a[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int d, i;
    scanf("%[^\n]s", s);
    d = strlen(s);
    for (i = 0; i < d; i++)
    {
        int l = (int)(s[i]) - 48;
        if (l >= 0 && l <= 9)
        {
            a[l]++;
        }
        else
        {
            continue;
        }
    }
    for (i = 0; i < 10; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}
