#include <stdio.h>
int  main()
{
    printf("Hello pucpr\n");
    long double PI = 3.14;
    long double raio = 10.0;
    long double area = PI * raio * raio; 
    printf ("%f\n",area);
    printf ("%zu\n", sizeof(PI));
    printf ("%zu\n", sizeof(area));
    printf ("%zu\n", sizeof(raio));
    printf("%p\n", &area);
    printf("%p\n", &PI);
    printf("%p\n", &raio);
    
    return 0;


}