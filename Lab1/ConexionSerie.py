import pandas as pd

# Datos 
resistencias_ohm = [50, 100, 150, 200]
v_medido_v = [1.04, 2.018, 3.017, 4.085]
i_medido_a = [0.02, 0.02, 0.02, 0.02]
i_medido_ma = [20, 20, 20, 20]

# voltaje final, corriente final yresistencia total 
v_total = sum(v_medido_v)
i_total_a = sum(i_medido_a) / len(i_medido_a)  # promedio de las corrientes medidas
r_total_ohm = sum(resistencias_ohm)

# DataFrame 
resultados = {
    'Resistencia (Ohm)': resistencias_ohm,
    'V Medido (V)': v_medido_v,
    'I Medido (A)': i_medido_a,
    'I Medido (mA)': i_medido_ma
}

df = pd.DataFrame(resultados)


df['Vtotal (V)'] = v_total
df['Itotal (A)'] = i_total_a
df['Rtotal (Ohm)'] = r_total_ohm

# Exportar DataFrame a uExcel
nombre_archivo_excel = 'resultados_conexion_serie.xlsx'
df.to_excel(nombre_archivo_excel, index=False, engine='openpyxl')

print(f"Los resultados se han exportado a '{nombre_archivo_excel}' con éxito.")

