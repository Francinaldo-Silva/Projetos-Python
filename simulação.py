import statistics
dados = []
od = []  
n = int(input("Quantidade de dados de Amostra: "))
for i in range(n):
    d = int(input("%dº dado de entrada: " % (i+1)))
    dados.append(d)
print("===================")
print("Dados de Entrada: ")
print("\n===================")
for i in dados:
    print(i, end = " ")
od = sorted(dados)
print("\n===================")
print("\nDados ordenados: ")
for i in od:
    print(i, end = " ")
for i in od:
    t = len(od)
    if t % 2 == 0:
        med = (od[int(t/2)] + od[int((t/2)-1)])/2    
    else:
        med = statistics.median(od)
print("\n===================")
print("Média da lista: ", statistics.mean(od))
print("===================")
print("Moda da lista: ", statistics.mode(od))
print("===================")
print("Mediana: %d"% med)
print("===================")
print("Maior da lista: ", max(od))
print("===================")
print("Menor da lista: ", min(od))
print("===================")

