#include <stdio.h>

int main()
{
    int a = 1, b = 2, c = 3; 
    printf("endereço de a: %p\n, &a");
    printf("endereço de b: %p\n, &b");
    printf("endereço de c: %p\n, &c");

    int* p = &c;
    printf("p: %p\n",p);
    printf("conteudo de p: %d\n", *p);

    p = p+1 ;
    return 0
    
}