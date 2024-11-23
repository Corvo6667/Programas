import random
import string

def gerar_senha(tamanho=12):

    # Conjunto de caracteres disponíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Garante que a senha contenha pelo menos um de cada tipo
    senha = [
        random.choice(string.ascii_lowercase),  #gera letra minuscula
        random.choice(string.ascii_uppercase),  #gera letra maiuscula
        random.choice(string.digits),          #gera numeros
        random.choice(string.punctuation)      #gera caracter especial
    ]
    
    #taca caracter especial em todo resto
    senha += random.choices(caracteres, k=tamanho - len(senha))
    
    #mexe em todos os caracter especial e embaralha tudo
    random.shuffle(senha)
    
    return ''.join(senha)

#teste do gerador
tamanho_senha = int(input("Digite o tamanho da senha que deseja gerar: "))
senha_gerada = gerar_senha(tamanho_senha)
print(f"Senha gerada: {senha_gerada}")
