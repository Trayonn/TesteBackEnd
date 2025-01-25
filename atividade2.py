#ATIVIDADE 2

n1 = 0
n2 = 1

numero = int(input("Informe um número: "))

if numero == n1 or numero == n2:
    print("O valor está na sequência de Fibonacci.")

else:
    while n2 < numero:
        p_valor = n1 + n2
        n1 = n2
        n2 = p_valor

    if n2 == numero:
        print("O valor está na sequência de Fibonacci")

    else:
        print("O valor não está na sequência.")


