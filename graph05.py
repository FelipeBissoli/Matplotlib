import matplotlib.pyplot as plt

dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
temp = [32, 34, 33, 31, 30, 29, 28]

fig, ax = plt.subplots(figsize=(10,6))
ax.set_facecolor('#333333')

plt.plot(dias, temp)

plt.title('Veriação da Temperatura Diária ao longo de Uma Semana')
plt.ylabel('Temperatura em °C')

plt.grid(True, color='green', linestyle='--', linewidth='0.8')

plt.show()