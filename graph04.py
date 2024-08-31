import matplotlib.pyplot as plt

meses = ['jan', 'fev', 'mar','abril', 'maio', 'jun']
prodX = [200, 210, 180, 220, 230, 240]
prodY = [150, 170, 160, 190, 200, 210]

fig, ax = plt.subplots(figsize=(10,6))
ax.set_facecolor('#333333')

plt.plot(meses, prodX, label = 'Produto X', color='#08f7fe', marker='o')
plt.plot(meses, prodY, label = 'Produto Y', color='#FE53BB', marker='s')

plt.title('Evolução de vendas entre 2 produtos', color='green')
plt.ylabel('Vendas')

plt.grid(True, linestyle='--', color='grey', linewidth=0.8)
plt.legend()

plt.show()