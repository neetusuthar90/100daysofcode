#include<stdio.h>

struct person
{
    int age;
    float weight;
};

int main(){
    struct person *ptr, p1;
    ptr = &p1;

    printf("Enter age: ");
    scanf("%d", &ptr->age); // ptr->age is equivalent to (*ptr).age

    printf("Enter weight: ");
    scanf("%f", &ptr->weight);

    printf("Displaying:\n");
    printf("Age: %d\n", ptr->age);
    printf("Weight: %.2f", (*ptr).weight);
    
    return 0;
}
