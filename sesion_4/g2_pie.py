import matplotlib.pyplot as plt

labels = ('Hombres', 'Mujeres', 'Otros')
sizes = [34, 49, 7]
explode = (0, 0, 0.1)

fig, ax = plt.subplots()

ax.pie(sizes, explode=explode, labels=labels, 
    autopct='%1.1f%%', shadow=False, startangle=90)

ax.axis('equal')

plt.show()