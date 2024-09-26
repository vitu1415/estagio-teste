print("Coloque os valores do dia\nEx:10, 11, 12...\n")
dia = list(map(int, input("coloque os valor: ").split(",")))
dia.sort()
print("menor valor = {}".format(dia[0]))
print("maior valor = {}".format(dia[-1]))
media = sum(dia)/len(dia)
print("Media = {}".format(media))
superio_media = 0
for x in dia:
    if x > media:
        superio_media += 1
print("Total de dias onde foi superior = {}".format(superio_media))