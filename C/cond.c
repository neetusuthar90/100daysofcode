#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

static char *string[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int main()
{
    int n;

    scanf("%d", &n);
    if (n >= 1 && n <= 9)
    {
        printf("%s\n", string[n - 1]);
    }
    else
    {
        printf("Greater than 9");
    }
    printf("Address of string[0]: %p", &string[0]);
    return 0;
}