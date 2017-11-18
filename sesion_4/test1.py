import scic

datos = scic.load_data_csv("edades.csv")

scic.plot_data_pie(datos, "Genero")