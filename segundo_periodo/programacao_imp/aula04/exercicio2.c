#include <stdio.h>

int main (){
    int a,b; //valores fornecidos pelo usuário
    printf("Digite um valor para a: ");
    scanf ("%d", &a);// leitura do valor de a

    printf("Digite um valor para b: ");
    scanf("%d", &b);// leitura do valor de b

    printf ("valor lido de a: %d\n", a);
    printf ("valor lido de a: %d\n", b);
    if (a==b){
        printf("Os valores lidos de a e b são iguais. Tente novamente!\n");
    }

    if (a < b){
        printf("a é menor que b: %d  < %d", a,b);
    }
    else {
        printf("b menor que a: %d < %d",b,a);
    }

    return 0;
}