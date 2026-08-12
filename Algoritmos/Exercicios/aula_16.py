# "Crie um dicionário chamado 'precos' com 3 itens à venda na guilda. Peça ao utilizador o nome de um item e exiba o preço correspondente."


# precos ={
#     "Espada":"15",
#     "Arco":"20",
#     "Machado":"25"
# }
# print("Escolha um item aventureiro: \n Espada \n Arco \n Machado")
# item_buscado = input("Item desejado ")
# if item_buscado in precos:
#     print (f'Preço do item {item_buscado} = {precos[item_buscado]}')
# else:
#     print ("Item não disponivel")


# "Peça ao aventureiro para digitar 5 habilidades. Guarde-as num Conjunto (Set). Ao final, mostre quantas habilidades ÚNICAS ele tem."

# habilidades = set()
# for i in range (1,6):
#     habilidades.add(input("Me diga uma habilidade "))
# print(f'habilidades unicas: {len(habilidades)}')



# "Crie um dicionário com 'forca': 10. Pergunte ao utilizador quanto quer aumentar. Atualize e verifique se passou de 20."

# habilidade = {
#     "força":10
# }
# print(f'Força atual: {habilidade["força"]}')
# habilidade["força"]+= int(input("Quanto de força você quer adicionar?"))
# if habilidade["força"] <=20:
#     print(f'Força atualizada para: {habilidade["força"]}')
# else:
#     print(f'Sua força excedeu o limite de 20')


# "Guarde missões num dicionário com valores Booleanos (concluída ou não). Sempre que uma missão for concluída, adicione a sua recompensa a um Conjunto de recompensas únicas. No final, conte as missões concluídas e mostre o Conjunto de recompensas."

missoes = {}
recompensas = {"100 Ouros", "Espada", "Escudo", "Poção de Vida"}
while (True):
    missoes["Missao"]=(input("Nome da missão "))
    escolha  = int (input("Missão Concluida? \n 1 = Verdadeiro \n 2= Falso \n"))
    match (escolha):
        case 1:
            missoes["Status"] = True
            missoes["Recompensas"] = recompensas
        case 2:
            missoes["Status"] = False
        case _:
            print("Opção invalida")
    tem_missao = input("Voce tem outra missão para atualizar? \n (S)Sim / (N)Não \n")
    if tem_missao =="N":
        break
contador  = 0
print(missoes)
for missao, valor in missoes.items():
    print(status, " ", valor2)
    if status:
        contador+=1

print(f'Total de missoes concluidas ={contador}')
print(f'Recompensas recebidas {recompensas}')