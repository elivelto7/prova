print('AVALIAÇÃO ALGORITMO E LÓGICA')

opcao = 0
while opcao != 9:
    print('''    1. Percorrer palavra
    2. Jogo da Quina
    
    9. Finalizar o programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        palavra = input('Digite uma única palavra: ')
        print(palavra)

        print('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
        print('1 2 3 4 5 6 7 8 9 1011121314151617181920212223242526')

        def posicao_letra(letra):
            return ord(letra.lower()) - 97

        contador = 1
        for l in palavra:
            posicao = posicao_letra(l)
            print(f'Letra da palavra: {l} - Posição {contador} \n Letra Alfabeto na posição: {posicao + 1}')
            contador += 1

        input('Pressione ENTER para Prosseguir...')
    elif opcao == 2:
        from random import randint

        num = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
        res = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))

        print('Quina - Concurso 2711 - 27/11/2021')
        print('Números do apostador')

        print('Aposta...: ', end='')
        for n in num:
            print(f'{n} ', end='')

        print('\nResultado: ', end='')
        for r in res:
            print(f'{r}', end='')

        input('\nPressione ENTER para Prosseguir...')

    elif opcao == 9:
        print('Programa Finalizado...')
    else:
        print('Opção inválida. Tente novamente')
