#include <stdio.h>
int main ()
{
    int idade = -1;
    double altura = -1;
    printf("Digite a sua altura: ");
    scanf (" %3d %5lf", &altura, &idade);
    printf("Sua idade: %f", altura);
    printf("\n");
    return 0;


}