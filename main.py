candidatos = [
    ("Bruno", "e5_t10_p8_s8"),
    ("Marlon", "e10_t7_p7_s8"),
    ("Ana", "e8_t5_p4_s9"), 
    ("Beatriz", "e2_t2_p2_s1"), 
    ("Lucas", "e10_t10_p8_s9")
]

nota_entrevista_1 = int(input("Coloque a nota da entrevista: "))
nota_teste_teorico_2 = int(input("Coloque a nota do teste teorico: "))
nota_teste_pratico_3 = int(input("Coloque a nota do teste prático: "))
nota_softskills_4 = int(input("Coloque a nota de Softskills: "))

total = []

for aluno in candidatos: 
    nome, notas = aluno
    entrevista_nota, teorico_nota, pratico_nota, softskills_nota = [int(nota[1:]) for nota in notas.split('_')]
    if entrevista_nota >= nota_entrevista_1 and teorico_nota >= nota_teste_teorico_2 and pratico_nota >= nota_teste_pratico_3 and softskills_nota >= nota_softskills_4:
        print(f"O candidato {nome} passou com as notas: {entrevista_nota} na entrevista, {teorico_nota} no teste teorico, {pratico_nota} no teste prático e {softskills_nota} no teste de Softskills.")
        total.append(aluno)

if len(total) == 0:
    print("Nenhum canditado passou")

input("Pressione a tecla Enter para fechar o programa....")
