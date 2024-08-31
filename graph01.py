import matplotlib.pyplot as plt

mes = ['jan', 'fev', 'mar', 'abril', 'maio', 'jun']
temp = [25, 27, 30, 28, 24, 22]

plt.style.use('dark_background') #mudando a cor de fundo de toda a imagem

fig, ax = plt.subplots(figsize=(10,6)) #mudando a dimencionalidade
ax.set_facecolor('#333333') #a cor de dentro apenas da área gráfica

plt.plot(mes, temp, marker='o') #adicionando o que será plotado no gráfico + o marcador
ax.grid(True, color='grey', linestyle='--', linewidth=0.8) #formatando o grid

plt.title('Variação de Temperatura ao Longo do Ano')
plt.xlabel('Meses')
plt.ylabel('Temperatura em ºcelsius')

plt.show()