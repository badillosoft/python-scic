import scic

mat = scic.load_matrix_csv("mat.csv")

print(mat)

scic.save_matrix_csv("mat3.csv", mat)

line3 = scic.get_line("mat3.csv", 3)

print(line3)

n = scic.count_word("mensaje.txt", "hola")

print("La palabra hola aparece {} veces".format(n))