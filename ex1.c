void main(){
    int INDICE = 13, SOMA = 0, K = 0;
    while(K < INDICE){
        K += 1;
        printf("%d", K);
        SOMA += K;
    }
    printf("soma = %d", SOMA);
    return 0;
}