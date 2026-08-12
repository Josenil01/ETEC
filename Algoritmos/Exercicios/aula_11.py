forca = int(input("Digite a força do ataque [1-10]: "));    
if forca < 1 or forca > 10:
    print("Valor invalido para a força do ataque, o valor deve ser entre 1 e 10.");
    forca= int(input("Digite a força do ataque: "));

agilidade = int(input("Digite a agilidade do personagem [1-10]: "));
if agilidade < 1 or agilidade > 10:
    print("Valor invalido para a agilidade do personagem, o valor deve ser entre 1 e 10.");
    agilidade = int(input("Digite a agilidade do personagem: "));

inteligencia = int(input("Digite a inteligência do personagem [1-10]: "));
if inteligencia < 1 or inteligencia > 10:
    print("Valor invalido para a inteligência do personagem, o valor deve ser entre 1 e 10.");
    inteligencia = int(input("Digite a inteligência do personagem: "));

poder = forca * 3 + agilidade * 2 + inteligencia * 0.5;
print(f"O poder do personagem é: {poder:.2f}");