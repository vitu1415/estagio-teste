sp = float(input("Coloque o valor do faturamento: "))
rj = float(input("Coloque o valor do faturamento: "))
mg = float(input("Coloque o valor do faturamento: "))
es = float(input("Coloque o valor do faturamento: "))
outros = float(input("Coloque o valor do faturamento: "))
Lista_faturamento = []
Lista_faturamento.append(sp)
Lista_faturamento.append(rj)
Lista_faturamento.append(mg)
Lista_faturamento.append(es)
Lista_faturamento.append(outros)

lista_estados = [sp, rj, mg, es, outros]
lista_porcentagem = []
cont = 0
total = sum(Lista_faturamento)
for x in Lista_faturamento:
    porcentagem = (x * 100)/total
    lista_porcentagem.append(porcentagem)
    print("{} = R${}, porcentagem = {:.2f}%".format(lista_estados[cont], x, porcentagem))
    cont += 1