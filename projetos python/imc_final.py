pip install pyinstaller

user_name = input("Qual seu nome? ")
print("Bem vindo {} !".format((user_name)))

print("Essa é uma calculadora de IMC (Indíce de Massa Corporal)\n")
print("É importante que nas informações fornecidas você use o . em vez da ,")
height = float(input("Qual sua altura em metros (exemplo: 1.70) {} ? ".format(user_name)))
weight = float(input("Qual seu peso atual em quilos (exemplo 70.6) {} ".format(user_name)))

print("Vamos conferir as informações?")
print("Sua altura é de {} m e seu peso é de {} Kg ?".format(height,weight))
confirmation = int(input("Para confirmar as informações digite 1-Confirmar e 2-Negar "))

imc = weight / (height**2)
a = imc

pidg = 18.6 * (height**2)
pidp = 24.9 * (height**2)

g = float(pidg - weight)
p = float(weight - pidp)
if (a <= 18.5):
    c = "Baixo Peso"
    idg = float("O peso ideal seria {}".format(pidg))
    difig = float("O peso recomendado para estar no Peso Normal é de {}".format(g))
elif (18.6 <= a <= 24.9):
    c = "Peso Normal"
elif (25.0 <= a <= 29.9):
    c ="Sobrepeso"
    print(("O peso ideal seria {:.2f}".format(pidp)))
    print("O peso recomendado para estar no Peso Normal é de {}".format(p))
elif (30.0 <= a <= 34.9):
    c = "Obesidadede Grau I"
    print(("O peso ideal seria {:.2f}".format(pidp)))
    print("O peso recomendado para estar no Peso Normal é de {}".format(p))
elif (35 <= a <= 39.9):
    c ="Obesidade Grau II"
    print(("O peso ideal seria {:.2f}".format(pidp)))
    print("O peso recomendado para estar no Peso Normal é de {}".format(p))
elif (a >= 40.0):
    c = "Obesidade Grau III"
    print(("O peso ideal seria {:.2f}".format(pidp)))
    print("O peso recomendado para estar no Peso Normal é de {}".format(p))

if (confirmation == 1) and (18.6 <= a <= 24.9):
    print("Certo {}, vamos agora disponibilizar seu resultado".format(user_name))
    print("Seu IMC é de {:.2f} e a categoria é de {} !".format(imc, c))
    print("O peso ideal é de {} Kg e para estar dentro do Peso Normal deverá ganhar {} Kg".format(idg,difig))
elif (confirmation == 1) and (a >= 25.0):
    print("Certo {}, vamos agora disponibilizar seu resultado".format(user_name))
    print("Seu IMC é de {:.2f} e a categoria é de {} !".format(imc, c))
    print("O peso ideal é de {:.2f} Kg e para estar dentro do Peso Normal deverá perder {:.2f} Kg".format(pidp,p))
elif (confirmation == 1) and (18.6 <= a <= 24.9):
    print("Certo {}, vamos agora disponibilizar seu resultado".format(user_name))
    print("Seu IMC é de {:.2f} e a categoria é de {} !".format(imc, c))
elif (confirmation != 1):
    print("Tente Novamente :( )")

