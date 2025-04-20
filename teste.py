import matplotlib
matplotlib.use('Agg')  # Ou outro backend não interativo como 'svg'
import matplotlib.pyplot as plt
import numpy as np

dias = ['2024-10-05', '2024-10-06']
contagens = [5, 4]
x_pos = np.arange(len(dias))

print(f"dias: {dias}")
print(f"contagens: {contagens}")
print(f"Tipo dos dados em contagens: {[type(c) for c in contagens]}")
print(f"x_pos: {x_pos}")

plt.figure(figsize=(6, 4))
plt.bar(x_pos, contagens, color='green')
plt.xticks(x_pos, dias)
plt.ylabel('Número')
plt.title('Teste Matplotlib')
plt.savefig('teste_matplotlib.png')
print("Gráfico salvo como teste_matplotlib.png")
print(f"Matplotlib Backend: {plt.get_backend()}")