candidatos = [
    ("aluno_1", 5, 10, 8, 8),
    ("aluno_2", 10, 7, 7, 8),
    ("aluno_3", 8, 5, 4, 9), 
    ("aluno_4", 2, 2, 2, 1), 
    ("aluno_5", 10, 10, 8, 9)
]

nota1 = int(input("Coloque a primeira nota: "))
nota2 = int(input("Coloque a segunda nota: "))
nota3 = int(input("Coloque a terceira nota: "))
nota4 = int(input("Coloque a quarta nota: "))

for aluno in candidatos: 
    nome, nota_1, nota_2, nota_3, nota_4 = aluno
    if nota_1 >= nota1 and nota_2 >= nota2 and nota_3 >= nota3 and nota_4 >= nota4:
        print(aluno)
        
    else:    
        print("Nenhum aluno passou")
