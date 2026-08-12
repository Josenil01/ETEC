import csv # É um formato de arquivo 

def exportar_guilda(lista_herois):
    try:
        with open("guilda.csv","w", newline="", encoding ="utf-8") as arquivo:
            gravador = csv.writer(arquivo)
            gravador.writerow(["Nome", "Classe", "Nivel", "Ouro", "Inventario"])
            for heroi in lista_herois:
                gravador.writerow([heroi['Nome'], heroi['Classe'], heroi['Nivel'], heroi['Ouro'], heroi['inventario']])
        print("✔️ Guilda Salva com sucesso em 'guilda.csv'") 
    except PermissionError:
        print("❌ error: Fecha o Excel para eu conseguir salvar o arquivo")
       
       
guilda = []       
       
       
       
def gravar():
    while True:
        print("\n[1] Registrar novo Herói | [2] Carregar Save | [3] Salvar e Sair")
        op = int(input("Escolha: "))
        if op == 1:
            novo = {}
            novo ['Nome'] = input("Nome:")
            novo ['Classe'] = input("Classe:")
            novo ['Nivel'] = int(input("Nivel"))
            novo ['Ouro'] = int(input("Ouro Inicial"))
            novo ['Inventario'] = ["Poção", "Corda"]
            guilda.append(novo)
            print('⚔️ Aventureiro pronto para o combate!')

        elif op == 2:
            with open("guilda.csv",'r', newline="", encoding="utf-8") as arquivo:
                    save = csv.DictReader(arquivo)
                    for heroi in save:
                    guilda.append(heroi)
                    print(guilda)
        else:
            if guilda: exportar_guilda(guilda)
            break
def ler():
    try:
        with open("historico.txt",'r', encoding="utf-8") as arquivo:
            print("---Relembrando a sua história---")
            for indice, linha in enumerate(arquivo, 1):
                print(f'Dia {indice}: {linha.strip()}')
    except FileNotFoundError:
        print("❌ Erro: Arquivo não encontrado!")
        
        
print("Diario das missões")
opcao = int(input("O que deseja fazer?\n (1)Ler - (2)Gravar"))

match opcao:
    case 1:
        ler()
    case 2:
        gravar()
    case _:
        print("Opção não encontrada!")