# Solicitar e registrar notas de uma turma ate dgitar fim para encerrar a solicitação / ignorar notas invalidas e continuar solicitando / exibir media no final

notas = []

while True:
    adicionar_nota = input("Digite uma nota ou digite 'fim' para encerrar: ")
    if adicionar_nota.lower() == "fim":
        break
    try:
        nota = float(adicionar_nota)
        if 0 <= nota <= 10:
            notas.append(nota)  
    except ValueError:
        adicionar_nota = input("Digite uma nota ou digite 'fim' para encerrar: ")

media = sum(notas) / len(notas)
print(f"A media das notas e: {media}")
