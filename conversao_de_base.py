#o usuário coloca o número em decimal
decimal = int(input("Coloque o número decimal aqui: "))
#o usuário seleciona para qual base ele gostaria de converter 
select = str(input("Para qual base você gostaria de converter: \nBinário - B \nOctadecimal - O \nHexadecimal - H: "))


# se a resposta do usuário for B ou b, ele vai entrar nessa condição
if select == "B" or select == "b":
    #variável para armazenar o valor de binário
    binario = " "
    while decimal > 0:
        #variável resto para pegar o resto do número decimal
        resto = decimal % 2 
        #variável binario transforma o resto em string e soma o valor do próprio binário
        binario = str(resto) + binario
        #variável decimal é dividida por ela mesmo pegando somente o valor inteiro da operação
        decimal = decimal // 2
    #mostra o resultado o resultado do número digitado pelo usuário na base escolhida por ele
    print(binario)
    # se a resposta do usuário for O ou o, ele vai entrar nessa condição
    
elif select == "O" or select == "o":
    #variável para armazenar o valor de octal
    octal = " "
    while decimal > 0:
        #variável resto para pegar o resto do número decimal
        resto = decimal % 8
        #variável octal transforma o resto em string e soma o valor do próprio octa decimal
        octal = str(resto) + octal
        #variável decimal é dividida por ela mesmo pegando somente o valor inteiro da operação
        decimal = decimal // 8
    #mostra o resultado o resultado do número digitado pelo usuário na base escolhida por ele
    print(octal)
    
# se a resposta do usuário for H ou h, ele vai entrar nessa condição
elif select == "H" or select == "h":
     #variável para armazenar o valor de hexa
    hexa = " "
    while decimal > 0: 
        #variável resto para pegar o resto do número decimal
        resto = decimal % 16
        #se o resto for menor que 10 ele precisa ser convertido em letra
        if resto < 10: 
            #variável hexa transforma o resto em string e soma o valor do próprio octa decimal
            hexa = str(resto) + hexa
        else:
            #subtrai 10 do resto definindo o valor de 0 à 5 para encontra a letra representante do valor dentro da lista
            hexa = "ABCDEF"[resto - 10] + hexa
        #variável decimal é dividida por ela mesmo pegando somente o valor inteiro da operação
        decimal = decimal // 16
    #mostra o resultado o resultado do número digitado pelo usuário na base escolhida por ele
    print(hexa)
else: 
    #caso o usuário coloque um valor diferente da seleção
    print("Seleção inválida")
    