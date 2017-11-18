import scic

datos = scic.load_data_csv("calificaciones.csv")

scic.plot_data_pie(datos, "CAL_GEN")