palavra = "opa"
tentativas = 6
letras_corrretas = []

def forca():

    while tentativas > 0:
        exibir = []

        tent = input ("Digite uma letra: ")

        for letra in palavra:
            if letra in letras_corrretas:
                exibir += letra

            else:
                exibir += "_"

        print("Palavra: ", exibir)

        if exibir == palavra:
            print("Parabéns! Você venceu!")
            break

        if tent in palavra:
            letras_corrretas.append(tent)
            tentativas -= 1

        elif tent not in palavra:
            tentativas -= 1

        if tentativas == 0:
            print (f"Você perdeu! A palavra era {palavra}")

        else:
            print (f"Tentativas restantes: {tentativas}")

forca()