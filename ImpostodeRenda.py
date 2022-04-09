#Programa que calcula o IRPF
#Feito por Ewerton Alexander
#Feito no Pycharm

from tqdm import tqdm
import time

#colocando bordas ao redor do texto
def texto1(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)

texto1("--- CALCULANDO O Imposto de Renda ---")
texto1("Programa Construído por Ewerton Alexander de Oliveira Batista")

nome = input("Qual o seu nome? ")
texto1("Olá {}, para iniciar seu cálculo do Imposto de Renda, preciso de algumas infomações. Vamos lá!".format(nome))

nomecomp = input("Digite seu nome Completo: ")
cpf = input("Digite o seu CPF: ")
ra = float(input("Digite seu Rendimento Anual: "))
irf = float(input("Digite o Imposto Retido na Fonte: "))
cp = float(input("Digite o valor da sua contribuição previdenciária: "))
dm = float(input("Digite suas Despesas Médicas: "))
dep = int(input("Se tiver dependentes digite a quantidade, se não, digite 0: "))

texto1("Nome: {}\nCPF: {}\nRenda Anual: {:.2f}\nImposto Retido na Fonte: {:.2f}\n"
      "Contibuição Previdenciária: {:.2f}\n"
      "Despesas Médicas: {:.2f}\nDependentes: {}".format(nomecomp, cpf, ra, irf, cp, dm, dep))

#cáculos:
calcdep = dep * 2060 #calculo de dedução de dependentes
deducoes = cp + dm + calcdep #calculo do valor total das deduções
base = ra - deducoes #base de calculo para IRPF
aliquota1 = 15 / 100 #aliquoa base 2
aliquota2 = 25 / 100 #aliquota base 3
impdevido1 = (base * aliquota1) - 3620 #calculo para imposto devido base 2
impdevido2 = (base * aliquota2) - 4780 #calculo para imposto devido base 3
rest1 = impdevido1 - irf #calculo para restituição base 2
rest2 = impdevido2 - irf #calculo para restituição base 3

#colocar uma barra para aguardar o calculo
print("\nCalculando seu IRPF... aguarde...")
for i in tqdm(range(10)):
    time.sleep(1)


if base <= 28600:
    texto1("Prontinho! {} você está ISENTO DO IRPF!".format(nome))
if base > 28600 and base <= 41600:
    if impdevido1 - irf <=0:
        texto1("Prontinho! {} você tem, R${:.2f} de Imposto a RESTITUIR!".format(nome, rest1))
    else:
        texto1("Prontinho! {} você tem, R${:.2f} de Imposto a PAGAR!".format(nome, rest1))
if base > 41600:
    if impdevido2 - irf <=0:
        texto1("Prontinho! {} você tem, R${:.2f} de Imposto a RESTITUIR!".format(nome, rest2))
    else:
        texto1("Prontinho! {} você tem, R${:.2f} de Imposto a PAGAR!".format(nome, rest2))



while True:
    a = str(input(""))

    if a == "":
        break