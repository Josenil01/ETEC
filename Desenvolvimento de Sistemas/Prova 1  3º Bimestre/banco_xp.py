# ============================================================
# PROVA 1 - 3º BIMESTRE - SISTEMA BANCÁRIO (BANCO XP)
# ============================================================
#
# OBJETIVO
# Desenvolver um sistema bancário em Python que armazene todos
# os dados em um arquivo JSON (usar with open para ler e gravar).
# Utilizar listas (arrays) e dicionários para estruturar os dados.
#
# ------------------------------------------------------------
# ESTRUTURA DE DADOS
# ------------------------------------------------------------
# O arquivo JSON guarda uma lista de contas. Cada conta é um
# dicionário no formato:
#
#   {
#       "nome": "",        # informado pelo usuário (input)
#       "agencia": "",     # informado pelo usuário (input)
#       "cep": "",         # informado pelo usuário (input)
#       "conta": "",       # gerado automaticamente: 9 dígitos
#       "senha": "",       # gerado automaticamente: 4 dígitos
#       "saldo": 0,        # saldo atual da conta (inicia em 0)
#       "extrato": []      # lista de operações (ver abaixo)
#   }
#
# Cada operação registrada no extrato é um dicionário:
#
#   {
#       "id_op": 1,            # sequencial, começa em 1
#       "data": "",           # data/hora da operação
#       "valor": 0.0,         # valor da operação
#                             # (saque e transferência enviada = negativo)
#       "saldo_atual": 0.0,   # saldo da conta após a operação
#       "operacao": ""        # "deposito", "saque", "transferencia"...
#   }
#
# ------------------------------------------------------------
# FUNCIONALIDADES
# ------------------------------------------------------------
# 1) CRIAR CONTA
#    - Solicita via input: nome, agência e cep.
#    - Gera automaticamente: conta (9 dígitos) e senha (4 dígitos).
#    - Saldo inicial = 0 e extrato vazio.
#    - Salva a nova conta no arquivo JSON.
#    - Exibe agência, conta e senha UMA ÚNICA VEZ após o cadastro.
#
# 2) DEPÓSITO
#    - Solicita via input: agência, conta e valor.
#    - O valor deve ser maior que 0.
#    - Soma o valor ao saldo e registra a operação no extrato.
#
# 3) SAQUE
#    - Solicita via input: agência, conta, senha e valor.
#    - Valida a senha.
#    - Só realiza o saque se o saldo final for maior que 0
#      (não permite saldo negativo).
#    - Subtrai o valor do saldo e registra a operação no extrato.
#
# 4) EXTRATO
#    - Solicita via input: agência, conta e senha.
#    - Valida a senha.
#    - Exibe todas as operações da conta e o saldo atual.
#    - Modelo de exibição (usar f-string / template string):
#
#      extrato = f"""
#      ============= EXTRATO - BANCO XP =============
#      Cliente : {conta['nome']}
#      Agência : {conta['agencia']}    Conta: {conta['conta']}
#      ---------------------------------------------
#      ID     DATA               OPERAÇÃO      VALOR       SALDO
#      """
#      for op in conta['extrato']:
#          extrato += f"{op['id_op']:<5}  {op['data']:<16}  {op['operacao']:<12}  {op['valor']:>10.2f}  {op['saldo_atual']:>10.2f}\n"
#
#      extrato += f"""---------------------------------------------
#      SALDO ATUAL: R$ {conta['saldo']:.2f}
#      =============================================
#      """
#
#      Exemplo de saída:
#      ============= EXTRATO - BANCO XP =============
#      Cliente : Maria Silva
#      Agência : 0001    Conta: 123456789
#      ---------------------------------------------
#      ID     DATA               OPERAÇÃO      VALOR       SALDO
#      1      01/09/2026 10:30   deposito          500.00      500.00
#      2      01/09/2026 10:45   saque            -200.00      300.00
#      3      01/09/2026 11:00   transferencia    -100.00      200.00
#      ---------------------------------------------
#      SALDO ATUAL: R$ 200.00
#      =============================================
#
# 5) TRANSFERÊNCIA (entre contas)
#    - Solicita via input: agência/conta de origem, senha,
#      agência/conta de destino e valor.
#    - Valida senha e saldo da conta de origem (não pode ficar < 0).
#    - Debita da origem e credita no destino.
#    - Registra a operação no extrato das DUAS contas.
#
# 6) SAIR
#    - Encerra o programa.
#
# ------------------------------------------------------------
# REGRAS GERAIS
# ------------------------------------------------------------
# - Cada operação (depósito, saque, transferência) deve atualizar
#   automaticamente o saldo e o extrato da conta e regravar o JSON.
# - O código deve ser organizado em funções com responsabilidades
#   bem definidas (ex.: carregar_dados, salvar_dados, buscar_conta,
#   criar_conta, depositar, sacar, exibir_extrato, transferir).
# - O programa principal roda dentro de um while com o menu:
#       1 - Criar conta
#       2 - Depósito
#       3 - Saque
#       4 - Extrato
#       5 - Transferência
#       6 - Sair
# ============================================================

import json
import os
import random
from datetime import datetime

ARQUIVO = "contas.json"


# ------------------------------------------------------------
# PERSISTÊNCIA (with open + JSON)
# ------------------------------------------------------------
def carregar_dados():
    """Le o arquivo JSON e devolve a lista de contas. Se nao existir
    ou estiver corrompido, devolve uma lista vazia."""
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Aviso: nao foi possivel ler o arquivo. Iniciando vazio.")
        return []


def salvar_dados(contas):
    """Grava a lista de contas no arquivo JSON."""
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(contas, f, indent=4, ensure_ascii=False)
    except OSError:
        print("Erro: nao foi possivel salvar os dados.")


# ------------------------------------------------------------
# FUNCOES AUXILIARES
# ------------------------------------------------------------
def gerar_numero_conta():
    """Gera um numero de conta com 9 digitos (como string)."""
    return "".join(str(random.randint(0, 9)) for _ in range(9))


def gerar_senha():
    """Gera uma senha numerica com 4 digitos (como string)."""
    return "".join(str(random.randint(0, 9)) for _ in range(4))


def ler_entrada(mensagem):
    """Le uma linha do usuario tratando Ctrl+C / fim de entrada."""
    try:
        return input(mensagem).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada encerrada.")
        raise SystemExit


def ler_texto(mensagem):
    """Le um texto nao vazio do usuario."""
    while True:
        valor = ler_entrada(mensagem)
        if valor:
            return valor
        print("Valor obrigatorio. Tente novamente.")


def ler_valor(mensagem):
    """Le um valor monetario (float) maior que zero, tratando erros
    de conversao com try/except."""
    while True:
        entrada = ler_entrada(mensagem).replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Valor invalido. Digite um numero (ex: 100.50).")
            continue
        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue
        return round(valor, 2)


def buscar_conta(contas, agencia, numero):
    """Procura uma conta pela agencia e numero. Retorna o dicionario
    da conta ou None."""
    for conta in contas:
        if conta["agencia"] == agencia and conta["conta"] == numero:
            return conta
    return None


def autenticar(conta, senha):
    """Confere se a senha informada corresponde a da conta."""
    return conta["senha"] == senha


def registrar_operacao(conta, valor, operacao):
    """Atualiza o saldo da conta e adiciona a operacao ao extrato."""
    conta["saldo"] = round(conta["saldo"] + valor, 2)
    conta["extrato"].append({
        "id_op": len(conta["extrato"]) + 1,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "valor": round(valor, 2),
        "saldo_atual": conta["saldo"],
        "operacao": operacao,
    })


def montar_extrato(conta):
    """Monta o texto do extrato usando template string (f-string)."""
    texto = f"""
============= EXTRATO - BANCO XP =============
Cliente : {conta['nome']}
Agencia : {conta['agencia']}    Conta: {conta['conta']}
---------------------------------------------
{'ID':<5} {'DATA':<17} {'OPERACAO':<14} {'VALOR':>10} {'SALDO':>10}
"""
    if not conta["extrato"]:
        texto += "Nenhuma operacao registrada.\n"
    else:
        for op in conta["extrato"]:
            texto += (
                f"{op['id_op']:<5} {op['data']:<17} {op['operacao']:<14} "
                f"{op['valor']:>10.2f} {op['saldo_atual']:>10.2f}\n"
            )
    texto += f"""---------------------------------------------
SALDO ATUAL: R$ {conta['saldo']:.2f}
=============================================
"""
    return texto


# ------------------------------------------------------------
# OPERACOES DO MENU
# ------------------------------------------------------------
def criar_conta(contas):
    print("\n--- CRIAR CONTA ---")
    nome = ler_texto("Nome: ")
    agencia = ler_texto("Agencia: ")
    cep = ler_texto("CEP: ")

    numero = gerar_numero_conta()
    while buscar_conta(contas, agencia, numero) is not None:
        numero = gerar_numero_conta()
    senha = gerar_senha()

    conta = {
        "nome": nome,
        "agencia": agencia,
        "cep": cep,
        "conta": numero,
        "senha": senha,
        "saldo": 0.0,
        "extrato": [],
    }
    contas.append(conta)
    salvar_dados(contas)

    print("\nConta criada com sucesso! (anote os dados abaixo)")
    print(f"  Agencia: {agencia}")
    print(f"  Conta  : {numero}")
    print(f"  Senha  : {senha}")


def depositar(contas):
    print("\n--- DEPOSITO ---")
    agencia = ler_texto("Agencia: ")
    numero = ler_texto("Conta: ")
    conta = buscar_conta(contas, agencia, numero)
    if conta is None:
        print("Conta nao encontrada.")
        return

    valor = ler_valor("Valor do deposito: R$ ")
    registrar_operacao(conta, valor, "deposito")
    salvar_dados(contas)
    print(f"Deposito realizado. Saldo atual: R$ {conta['saldo']:.2f}")


def sacar(contas):
    print("\n--- SAQUE ---")
    agencia = ler_texto("Agencia: ")
    numero = ler_texto("Conta: ")
    senha = ler_texto("Senha: ")
    conta = buscar_conta(contas, agencia, numero)
    if conta is None:
        print("Conta nao encontrada.")
        return
    if not autenticar(conta, senha):
        print("Senha incorreta.")
        return

    valor = ler_valor("Valor do saque: R$ ")
    if conta["saldo"] - valor <= 0:
        print("Saque negado: o saldo final ficaria menor ou igual a zero.")
        return

    registrar_operacao(conta, -valor, "saque")
    salvar_dados(contas)
    print(f"Saque realizado. Saldo atual: R$ {conta['saldo']:.2f}")


def exibir_extrato(contas):
    print("\n--- EXTRATO ---")
    agencia = ler_texto("Agencia: ")
    numero = ler_texto("Conta: ")
    senha = ler_texto("Senha: ")
    conta = buscar_conta(contas, agencia, numero)
    if conta is None:
        print("Conta nao encontrada.")
        return
    if not autenticar(conta, senha):
        print("Senha incorreta.")
        return

    print(montar_extrato(conta))


def transferir(contas):
    print("\n--- TRANSFERENCIA ---")
    agencia_o = ler_texto("Agencia de origem: ")
    numero_o = ler_texto("Conta de origem: ")
    senha_o = ler_texto("Senha de origem: ")
    origem = buscar_conta(contas, agencia_o, numero_o)
    if origem is None:
        print("Conta de origem nao encontrada.")
        return
    if not autenticar(origem, senha_o):
        print("Senha incorreta.")
        return

    agencia_d = ler_texto("Agencia de destino: ")
    numero_d = ler_texto("Conta de destino: ")
    destino = buscar_conta(contas, agencia_d, numero_d)
    if destino is None:
        print("Conta de destino nao encontrada.")
        return
    if destino is origem:
        print("Nao e possivel transferir para a mesma conta.")
        return

    valor = ler_valor("Valor da transferencia: R$ ")
    if origem["saldo"] - valor < 0:
        print("Transferencia negada: saldo insuficiente.")
        return

    registrar_operacao(origem, -valor, "transferencia")
    registrar_operacao(destino, valor, "transferencia")
    salvar_dados(contas)
    print(f"Transferencia realizada. Saldo atual: R$ {origem['saldo']:.2f}")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------
def main():
    contas = carregar_dados()

    while True:
        print("""
========== BANCO XP ==========
1 - Criar conta
2 - Deposito
3 - Saque
4 - Extrato
5 - Transferencia
6 - Sair
==============================""")
        opcao = ler_entrada("Escolha uma opcao: ")

        if opcao == "1":
            criar_conta(contas)
        elif opcao == "2":
            depositar(contas)
        elif opcao == "3":
            sacar(contas)
        elif opcao == "4":
            exibir_extrato(contas)
        elif opcao == "5":
            transferir(contas)
        elif opcao == "6":
            print("Encerrando o sistema. Ate logo!")
            break
        else:
            print("Opcao invalida. Escolha um numero de 1 a 6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuario.")
