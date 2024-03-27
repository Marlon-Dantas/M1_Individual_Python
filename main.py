import time
candidatos = [
    ("aluno1", "e5_t10_p8_s8"),
    ("aluno2", "e10_t7_p7_s8"),
    ("aluno3", "e8_t5_p4_s9"), 
    ("aluno4", "e2_t2_p2_s1"), 
    ("aluno5", "e10_t10_p8_s9")
]

nota_entrevista_1 = int(input("Coloque a nota da entrevista: "))
nota_teste_teorico_2 = int(input("Coloque a nota do teste teorico: "))
nota_teste_pratico_3 = int(input("Coloque a nota do teste prático: "))
nota_softskills_4 = int(input("Coloque a nota de Softskills: "))

total = []

for aluno in candidatos: 
    nome, notas = aluno
    e, t, p, s = [int(nota[1:]) for nota in notas.split('_')]
    if e >= nota_entrevista_1 and t >= nota_teste_teorico_2 and p >= nota_teste_pratico_3 and s >= nota_softskills_4:
        print(f"O candidato {nome} passou com as notas {e}, {t}, {p}, {s}")
        total.append(aluno)

if len(total) == 0:
    print("Nenhum canditado passou")

time.sleep(5)