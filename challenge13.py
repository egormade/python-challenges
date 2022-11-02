#Challenge13 Calculo de moedas

print("Vamos calcular quanto dinheiro você tem!")

m1 = int(input("Quantas moedas de R$0,01: "))
m5 = int(input("Quantas moedas de R$0,05: "))
m10 = int(input("Quantas moedas de R$0,10: "))
m25 = int(input("Quantas moedas de R$0,25: "))
m50 = int(input("Quantas moedas de R$0,50: "))

total = (m1 * 0.01) + (m5 * 0.05) + (m10 * 0.10) + (m25 * 0.25) + (m50 * 0.50)
print("Você tem R${:.2f} guardado em seu cofre".format(total))