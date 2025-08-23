# deve verificar se uma senha é forte tendo pelo menos 8 caracteres e pelo menos um numero / deve continuar pedindo ate uma valida

while True:
    senha = input("Digite uma senha com pelo menos 8 caracteres e pelo menos um número ou digite 'sair' para sair: ")
    if senha.lower() == "sair":
        print("\nSaindo do programa")
        break
    elif len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("\nSenha forte valida!")
        break
    else:
        print("\nSenha fraca")
        continue


    