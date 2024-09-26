int fibonacci(int num){
    int i=1, pen=0, ult=1, soma=0;
    while(soma < num){
        if(i < 3)
            printf("%d ", i-1);
        else{
            soma = pen + ult;
            pen=ult;
            ult=soma;
            printf("%d ", ult);
        }
    i++;
    }
    if(num == soma){
        return num = 1;
    }
    else{
        return num = 0;
    }
}
int main() {
    int quant;
    printf("Digite um numero da fibonacci: ");
    scanf("%d", &quant);
    if (fibonacci(quant)){
        printf("\nnumero esta na fibonacci");
    }
    else{
        printf("\nnumero nao esta na fibonacci");
    }
    return 0;
}