class Media():
    qtdeMedia = int(input("Quantos numeros vai ter no calculo da media?"))
    total = 0.0
    for num in range(0, qtdeMedia):
        num = float(input("Digite um numero: "))
        total += num
    print(total/qtdeMedia)