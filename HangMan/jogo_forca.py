## JOGO DA FORCA
## Paulo Henrique Teixeira de Oliveira - @paulohtoliveira
import random

f1 = open("nomes.txt", "r")
f2 = [f1]
f3 = []
forca = ['cabeça', 'braços', 'tronco' , 'pernas']

for x in f2: # removendo \n da lista no arquivo txt
    for y in x:
        f3.append(y.strip()) # nova lista sem \n

segredo = random.choice(f3) # escolha aletoria de palavras
tamanho_seg = len(segredo) # tamanho da palavra 

print("SEGREDO:", segredo)

## 
erro = [] # Lista para armazenar erros
acerto = [] # Lista para armazenar acertos
nova_forca = [] # Lista para icluir mebros do corpo que estão sendo enforcados

def adivinha(n,i): # função para adivinhar letras
    if n in segredo and n not in acerto:
        acerto.append(n)
    elif n not in segredo and n not in erro:
        erro.append(n)
        nova_forca.append(forca[i])
    else:
        return False
    return True

def ocultado(n): # função para escolder com traços _
    oc = ""
    for n in segredo:
        if n not in acerto:
            oc += " _ "
        else:
            oc += n
    return oc

def forc(n,i): # função para mostrar os elementos enforcados
    fc = ""
    x = 0
    for n in erro:
        if n not in segredo:
            while x <= i:
                fc += str(x+1) + " " + nova_forca[x]+"\n"
                x += 1
    return "# você está sendo enforcado, tentativas restantes: " + str(len(forca)-x) + " # \n" + fc

def resultado(): # função para mostrar se venceu ou perdeu
    resultado = ""
    if set(segredo) != set(acerto):
        resultado = "PERDEU"
    else:
        resultado = "VENCEU"
    return resultado

################### - JOGO - ##########################

c = 0
z = 0
while ( c < len(forca) ):
    n = str(input("tentativa: "))
    adivinha(n,c)
    print ( ocultado(n) )

    while (True):
        if (n in acerto and set(segredo) != set(acerto)):
            n = str(input("tentativa: "))
            adivinha(n,c)
            print ( ocultado(n) )

            if set(segredo) == set(acerto):
                adivinha(n,c)
                break
        else:
            break
    
    if (n not in segredo):
        print ( forc(n,c) )

    if ( set(segredo) == set(acerto) ):
        break
       
    c += 1

print ("\n# RESULTADO DO JOGO: " + resultado() + " \n")


