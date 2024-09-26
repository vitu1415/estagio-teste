def inverter_string(texto):
    return texto[::-1]

string_original = input("Colqoue o que deseja inverter: ")
invertida = inverter_string(string_original)
print("Invertida: {}".format(invertida))