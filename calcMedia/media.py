# ler quatro numeros de quatro notas e calcular media com pesos 2,3,4,1

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print(f"\nMédia: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado")
elif media < 5.0:
    print("Aluno reprovado")
else:
    print("Aluno em exame") 
    nota_do_exame = float(input("\nDigite a nota do exame: "))
    print(f"Nota do exame: {nota_do_exame}")
    media_final = (media + nota_do_exame) / 2
    if media_final >= 5.0:
        print("\nAluno aprovado")
    else:
        print("\nAluno reprovado")
    print(f"Média final: {media_final:.1f}")
