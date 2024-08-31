import matplotlib.pyplot as plt

prova = ['1°','2°','3°','4°','5°']
alunoA = [7.5, 8, 7, 8.5, 9]
alunoB = [8, 7.5, 7.8, 8.2, 8.5]

plt.style.use('dark_background') 

fig, ax = plt.subplots(figsize=(10,6))
#ax.set_facecolor('#333330')

plt.plot(prova, alunoA, label='João', color='red')
plt.plot(prova, alunoB, label='Marcos', color='#08f7fe')

plt.title('Comparação de Desempenho Acadêmico')
plt.ylabel('Notas')
plt.xlabel('Avaliação')

plt.grid(True, color='gray', linestyle='--')
plt.legend()

plt.show()