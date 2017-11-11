def load_matrix_csv(filename):
    f = open(filename, "r")
    mat = []
    for line in f:
        srow = line.split(",")
        row = list(map(lambda s: float(s), srow))
        mat.append(row)
    f.close()
    return mat

def save_matrix_csv(filename, mat):
    f = open(filename, "w")
    for row in mat:
        srow = list(map(lambda x: str(x), row))
        line = ", ".join(srow)
        f.write(line + "\n")
    f.close()

def get_line(filename, i):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines[i - 1]

def count_word(filename, word):
    f = open(filename)
    count = 0
    for line in f:
        words = line.split(" ")
        for w in words:
            if w.lower() == word.lower():
                count += 1
    return count
