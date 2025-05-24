palavra_secreta = "qualquer"
tentativas = 0
letras_corretas = ""


def forca():

    while True:

        letra_digitada = input("Digite uma letra: ")
        palavra_formada = ""

        if letra_digitada in palavra_secreta:
            letras_corretas += letra_digitada
        
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_corretas:
                palavra_formada += letra_secreta

            else:
                palavra_formada += "*"

        tentativas += 1

        print(f"Palavra formada: {palavra_formada}")

        if palavra_formada == palavra_secreta:
            print (f"Fim do jogo! \nA palavra secreta era {palavra_secreta}. \n Você acertou na {tentativas}º tentativa.")

forca()