
from time import sleep
elementos =['Ac', 'B', 'C', 'Ds', 'Er', 'F', 'Ga', 'H', 'I', 'K', 'Cl']
nome= ['Actínio', 'Boro' ,'Carbono', 'Darmstádio', 'Érbio', 'Fluor', 'Gálio', 'Hidrogênio', 'Iodo', 'Potássio', 'Cloro']
numero = [ 89, 5, 6, 110, 68, 9, 31, 1, 53, 19, 17 ]
massa = [ 227, 10.8, 12.011, 281, 167.2, 18, 69.72, 1, 126.9, 39, 34]

ele = input('Digite um elemento:').capitalize()
print('\033[7mCarregando informação.....\033[m')
sleep(2)
if ele in elementos:
        index  = elementos.index(ele)

print(f'O nome do elemento é: {nome[index]}\nNúmero atômico: {numero[index]}\nMassa atômica é: {massa[index]}')

else:
   print('\033[1;31mElemento não encontrado. Tente novamente\033[m')


