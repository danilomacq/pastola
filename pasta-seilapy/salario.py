class Salario():
    nomeFunc = input("Nome do funcionario: ")
    horasTrabalhadas = float(input("Horas trabalhadas: "))
    valorHora = float(input("Valor hora do funcionario: "))
    print("O ", nomeFunc, "vai receber R$", (valorHora*horasTrabalhadas), "nesse mes")