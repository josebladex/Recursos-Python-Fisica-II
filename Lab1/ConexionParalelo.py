import pandas as pd

# Datos
resistencias_ohm = [50, 100, 150, 200]
v_medido_v = [4.082, 4.082, 4.082, 4.082]
i_medido_a = [0.08164, 0.04082, 0.027213333, 0.02041]
i_medido_ma = [81.64, 40.82, 27.21, 20.41]

# resistencia total (Rtotal)
r_total_ohm = 1 / sum(1 / r for r in resistencias_ohm)

# voltaje final (Vtotal)
v_total = v_medido_v[0]  

# corriente final (Itotal)
i_total_a = sum(i_medido_a)

#DataFrame
resultados = {
    'Resistencia (Ohm)': resistencias_ohm,
    'Voltaje (V)': v_medido_v,
    'Intensidad de Corriente (A)': i_medido_a,
    'Intensidad de Corriente (mA)': i_medido_ma
}

df = pd.DataFrame(resultados)


df['R total (Ohm)'] = r_total_ohm
df['V total (V)'] = v_total
df['I total (A)'] = i_total_a

# Exportar DataFrame a Excel
nombre_archivo_excel = 'resultados_conexion_paralelo.xlsx'
df.to_excel(nombre_archivo_excel, index=False, engine='openpyxl')

print(f"Los resultados se han exportado a '{nombre_archivo_excel}' con éxito.")
