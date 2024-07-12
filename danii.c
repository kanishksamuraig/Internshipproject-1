#include<stdio.h>
int main()
{
    int a,b;
    char c;
    printf("Enter the first number:");
    scanf("%d",&a);
    printf("Enter the second number:");
    scanf("%d",&b);
    printf("Enter the operation you want to perform:");
    scanf(" %c",&c);
    switch (c)
    {
        case '+':
            printf("%d + %d = %d",a,b,a+b);
            break;
        case '-':
            printf("%d - %d = %d",a,b,a-b);
            break;
        case '/':
            printf("%d / %d = %d",a,b,a/b);
            break;
        case '*':
            printf("%d * %d =%d",a,b,a*b);
            break;
        default:
            printf("Enter the valid operator");
            break;
    }
    return 0;

}

