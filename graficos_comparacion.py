import matplotlib.pyplot as plt

# Tiempos obtenidos de tus archivos de profiling
tiempo_original = 29.1496
tiempo_optimizado = 0.1379

# -------------------------------
# Gráfico 1: Comparativa de tiempos
# -------------------------------
codigos = ["Original", "Optimizado"]
tiempos = [tiempo_original, tiempo_optimizado]

plt.figure()
plt.bar(codigos, tiempos)
plt.title("Comparativa de tiempos de ejecución")
plt.xlabel("Tipo de código")
plt.ylabel("Tiempo en segundos")
plt.savefig("comparativa_tiempos.png")
plt.show()

# -------------------------------
# Gráfico 2: Distribución de tiempos
# -------------------------------
plt.figure()
plt.pie(tiempos, labels=codigos, autopct="%1.1f%%")
plt.title("Distribución de tiempos de ejecución")
plt.savefig("distribucion_tiempos.png")
plt.show()