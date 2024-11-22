import random


def exibir_boas_vindas():
    print ("=" * 40)
    print ("Bem vindo ao pedra, papel e tessoura!")
    print ("=" * 40)
    print ("Regras do jogo")
    print ("Pedra ganha de Tesoura")
    print ("Tesoura ganha de Papel")
    print ("Papel ganha de Pedra")
    print ("Digite 'sair' a qualquer momento para encerrar.\n")

def obter_escolha_do_jogador():

    while True:
        escolha = input ("Escolha (pedra, papel ou tesoura): ").lower()
        if escolha in("pedra", "papel", "tesoura", "sair"):
            return escolha
        print("Entrada inválida! Por favor, digite 'pedra', 'papel', 'tesoura' ou 'sair'.")

def determinar_vencedor(jogador , computador):

    if jogador == computador:
        return "empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        return "jogador"
    return "computador"

def exibir_placar(placar):

    print(f"\nPlacar atual")
    print(f"jogador:  {placar['jogador']} | computador: {placar['computador']}\n")

def jogar ():
    
    exibir_boas_vindas()

    placar = {"jogador": 0, "computador": 0}

    while True:

        jogador = obter_escolha_do_jogador()
        if jogador == "sair":  # Se o jogador digitar "sair", encerra o jogo.
            print("Encerrando o jogo...")
            break
        
        computador = random.choice(["pedra", "papel", "tesoura"])
        print(f"O computador escolheu: {computador}")

        vencedor = determinar_vencedor(jogador, computador)

        if vencedor == "jogador":
            print("Você ganhou esta rodada!")
            placar["jogador"] += 1
        elif vencedor == "computador":
            print("O computador ganhou esta rodada!")
            placar["computador"] += 1
        else:
            print("Esta rodada foi um empate!")
        
        exibir_placar(placar)
 
    print("\nObrigado por jogar!")
    print(f"Placar final: jogador {placar['jogador']} x {placar['computador']} computador")
    if placar["jogador"] > placar["computador"]:
        print("Parabens, você ganhou o jogo!")
    elif placar["jogador"] > placar["computador"]:
        print("O computador venceu o jogo. Tente novamente!")
    else:
        print("O jogo terminou empatado!")

if __name__ == "__main__":
    jogar()


