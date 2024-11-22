import random

def exibir_boas_vindas():
    print("=" * 30)
    print(" Bem-vindo ao Jogo da Forca! ")
    print("=" * 30)

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "tecnologia", "jogo", "internet", "dados", "software", "hardware"]
    return random.choice(palavras).lower()

def exibir_status(letras_descobertas, tentativas, letras_erradas):
    print("\nPalavra: " + " ".join(letras_descobertas))
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras erradas: {', '.join(letras_erradas) if letras_erradas else 'Nenhuma'}")

def jogar_forca():
    exibir_boas_vindas()
    
    palavra_secreta = escolher_palavra()
    letras_descobertas = ["_"] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []
    
    while tentativas > 0 and "_" in letras_descobertas:
        exibir_status(letras_descobertas, tentativas, letras_erradas)
        
        chute = input("\nDigite uma letra: ").lower()
        
        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if chute in letras_descobertas or chute in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if chute in palavra_secreta:
            print(f"Boa! A letra '{chute}' está na palavra.")
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = chute
        else:
            print(f"Ops! A letra '{chute}' não está na palavra.")
            letras_erradas.append(chute)
            tentativas -= 1
    
    if "_" not in letras_descobertas:
        print(f"\nParabéns! Você descobriu a palavra: {''.join(letras_descobertas)} 🎉")
    else:
        print(f"\nQue pena! Você perdeu! A palavra era: {palavra_secreta}. 😢")
    print("Obrigado por jogar!")

# Executa o jogo
if __name__ == "__main__":
    jogar_forca()
