num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operação que deseja realizar (+ ou - ou * ou /): ")

if operacao == '+': 
    print(num1+num2)
elif operacao == '-': 
    print(abs(num1-num2))
elif operacao == '*':
    print(num1*num2)
elif operacao == '/':
    print(num1/num2)
else: 
    print('Opção incorreta.')