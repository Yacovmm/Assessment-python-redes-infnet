import time, random

resultado = []
def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  #return fat
  resultado.append(fat)

t_inicio = float(time.time())

listaFatorial = []

def criaLista(n):
    for i in range(n):
        k = random.randint(1,10)
        listaFatorial.append(k)

criaLista(1000000)



for i in listaFatorial:
    fatorial(i)


t_fim = float(time.time())


print('Inicio:',t_inicio)
print('Fim:',t_fim)
td = t_fim - t_inicio
print('\n','Tempo:',round(td,2),'segundos.')