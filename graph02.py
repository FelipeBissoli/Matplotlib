import matplotlib.pyplot as plt

mes = ['jan', 'fev', 'mar', 'abril', 'maio', 'jun']
prec = [120, 85, 95, 70, 50, 40]

fig, ax = plt.subplots(figsize=(10,6))
ax.set_facecolor('#333333')
plt.plot(mes, prec, marker='o')

plt.grid(True, color='brown', linestyle='--', linewidth=0.8)

plt.title('Variação de Precipitação ao Longo do Semestre')
plt.xlabel('Mês')
plt.ylabel('Precipitação (mm)')

plt.show()