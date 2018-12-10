
f = open("marcas.txt")
n = open("new_marcas.txt", "w")
marcas = f.readlines()
marcas = [x.strip() for x in marcas]
new_marcas = []
for marca in marcas:
    if marca not in new_marcas:
        new_marcas.append(marca)

for marca in new_marcas:
    n.write(marca + "\n")
f.close()
n.close()