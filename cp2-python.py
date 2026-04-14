# Exer 3
cp1 = float(input("Fale a nota do checkpoint 1: "))
cp2 = float(input("Fale a nota do checkpoint 2: "))
cp3 = float(input("Fale a nota do checkpoint 3: "))
sp1 = float(input("Fale a nota do sprint 1: "))
sp2 = float(input("Fale a nota do sprint 2: "))
gs = float(input("Fale a nota do global solution: "))

if cp1 <= cp2 and cp1 <= cp3:
    menor = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    menor = cp2
else:
    menor = cp3

media = (cp1 + cp2 + cp3 - menor + sp1 + sp2)/4 * 0.4 + gs * 0.6

mediaPeso = media * 0.4

print("Media sem peso: ",round(media))
print("media com peso: ",round(mediaPeso))