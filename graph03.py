import matplotlib.pyplot as plt

ano = [2020, 2021, 2022, 2023, 2024]
city01 = [500, 520, 540, 560, 580]
city02 = [450, 460, 470, 490, 510]


fig, ax = plt.subplots(figsize=(10,6))

ax.set_facecolor('#333333')

plt.plot(ano, city01, label='Cidade A', color='#08f7fe', marker='o', linewidth=2)
plt.plot(ano, city02, label='Cidade B', color='#FE53BB', marker='s',linewidth=2)


ax.set_xticks(range(min(ano), max(ano) + 1, 1))

plt.title('Crescimento Populacional em Duas Cidades:', color='white')
plt.xlabel('População (Milhares)')
plt.ylabel('Ano')

plt.grid(True, color='gray', linestyle='--', linewidth=0.8)

plt.legend()
plt.show()