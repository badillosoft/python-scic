import matplotlib.pyplot as plt

def T_CLR_STR(s):
    return s.replace("\n", "").replace(" ", "_")

def load_data_csv(filename):
    f = open(filename, "r")

    line = f.readline()

    columns = line.split(",")

    columns = list(map(T_CLR_STR, columns)) # opcional

    output = []

    for line in f:
        values = line.split(",")
        values = list(map(T_CLR_STR, values)) # opcional
        
        data = {}

        for i in range(0, len(columns)):
            key = columns[i]
            value = values[i]
            data[key] = value

        output.append(data)

    f.close()

    return output

def plot_data_pie(data, column):
    # 1. Recolectar los datos de la columna
    # [{"X": 1, "Y": 3}, {"X": 2, "Y": 5}] + "Y" => [3, 5]
    values = []
    
    for dic in data:
        values.append(dic[column])

    # 2. Convertir el arreglo de valores
    # en un diccionario que cuente, cuántas veces
    # se repiten los valores en el arreglo
    # ["A", "A", "B"] => { "A": 2, "B": 1 }
    pie_dic = {}

    for x in values:
        if x in pie_dic:
            pie_dic[x] += 1
        else:
            pie_dic[x] = 1

    print (pie_dic)

    labels = []
    sizes = []

    for k, v in pie_dic.items():
        labels.append(k)
        sizes.append(v)

    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.axis("equal")
    plt.show()