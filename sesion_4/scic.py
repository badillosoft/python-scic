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