#include<stdio.h>
#include<string.h>
int main()
{
    printf("Hello world\n");
    int a,b;
    char c;
    printf("Enter the first number");
    scanf("%d",&a);
    printf("Enter the second number");
    scanf("%d",&b);
    printf("Enter the operation you want to perform");
    scanf("%c",&c);
    if (c=='+')
    {
        printf("\n%d+%d=%d",a,b,a+b);
    }
    else if (c=='-')
    {
        printf("\n%d-%d=%d",a,b,a-b);
    }
    else if (c=='/')
    {
        printf("\n%d/%d=%d",a,b,a/b);
    }
    return 0;

}