#include <stdio.h>
#include <stdbool.h>

int main()
{
    short a = 10;
    short* p_a = &a;
    printf("valor de a: %d\n",a);
    printf ("valor apontado por p_a: %d\n", *p_a);
    printf("endereço de a: %p\n", &a);
    printf("endereço de de p_a:  %p\n", &p_a);

    double b = 45.9;
    double* p_b = &b;
    printf("valor de b: %d\n",b);
    printf ("valor apontado por p_b: %d\n", *p_b);
    printf("endereço de a: %p\n", &b);
    printf("endereço de de p_a:  %p\n", &p_b);


    char c = '$';
    char* p_c = &c;
    printf("valor de c: %d\n",c);
    printf ("valor apontado por p_c: %d\n", *p_c);
    printf("endereço de a: %p\n", &c);
    printf("endereço de de p_a:  %p\n", &p_c);


    bool d = true;
    bool* p_d = &d;
    printf("valor de d: %d\n",d);
    printf ("valor apontado por p_d: %d\n", *p_d);
    printf("endereço de a: %p\n", &d);
    printf("endereço de de p_a:  %p\n", &p_d);

    return 0;
}