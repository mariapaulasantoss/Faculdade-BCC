#include <stdio.h>

int main (){
    char letra_1, letra_2, letra_3;
    printf("Digite 3 letras distintas entre si!\n");

    printf("Digite a primeira letra: ");
    scanf("%c", letra_1);
    getchar(); //consome o ENTER

    printf("Digite a segunda letra:");
    scanf("%c", letra_2);
    getchar(); //consome o ENTER

    printf("Digite a terceira letra: ");
    scanf("%c", letra_3);
    getchar(); //consome o ENTER
   
    printf("Letras lidas: %c %c %c \n", letra_1, letra_2, letra_3);
    
    if (letra_1 < 'a' || letra_1 > 'z'){
        printf("primeira letra inválida!"); return 1;
    }
        
    if (letra_1 < 'a' || letra_2 > 'z'){
        printf("segunda letra inválida!"); return 2;
    }
    if (letra_1 < 'a' || letra_3 > 'z'); {
        printf("segunda letra inválida!"); return 3;
    }
    if (letra_1 ==letra_2 || letra_1 == letra_3 || letra_2 == letra_3)
    {
        printf("as letras precisam ser distintas!"); return 4;
    }
    char x,y,z,r,s;
    if (letra_1 < letra_2 && letra_2 < letra_3) {
        x= letra_1; r = letra_2; s = letra_3;


    } else
    if (letra_2 < letra_1 ) {
        x = letra_2; r = letra_1; s - letra_3;
    }else // (letra_3 < letra_1 && letra_3 , letra_2) {
      {  x =letra_3; r = letra_1; s = letra_2;}
    
    if (r<s){
        y = s; z =s;
    }else {
        y = s; z = r;
    }

    printf("letras e ordem: %c %c %c \n", x, y, z);
    return 0; // retorno com sucesso
}