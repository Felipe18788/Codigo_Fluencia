from scipy.stats import linregress
import numpy as np

temperature_number = int(input("Quantas temperaturas adicionar? "))
straintime_number = int(input("Quantos valores de deformação e tempo adicionar? "))

dados = {
        "temperatura": [],
        "deformação": [],
        "tempo": []
    }

for i in range(temperature_number):
    temperature = float(input("Temperatura: "))
    dados["temperatura"].append(temperature)

    for j in range(straintime_number):
        strain = float(input("Deformação: "))
        time = float(input("Tempo: "))

        dados["deformação"].append(strain)
        dados["tempo"].append(time)

print(f"Temperaturas: ", dados["temperatura"])
print(f"Deformações: ", dados["deformação"])
print(f"Tempos: ", dados["tempo"])

strain_rate = []
for k in range(0,len(dados["deformação"]),straintime_number): 
    lin_strain_v = dados["deformação"][k:k+straintime_number]
    lin_time_v = dados["tempo"][k:k+straintime_number]
    print(lin_strain_v)
    print(lin_time_v)

    strain_rate_value, intercept, r_value, p_value, std_err = linregress(lin_time_v, lin_strain_v)
    
    strain_rate.append(strain_rate_value)

print(f"Valores de taxa de deformação: {strain_rate}") 

temp = np.array(dados["temperatura"])+273

lntaxa = np.log(strain_rate)
inversoT = 1/(temp)

slope, intercept, r_value, p_value, std_err = linregress(inversoT,lntaxa)

print(f"Valor de inclinação para a curva 1/T x ln(strain): {slope}")
print(intercept)

Q = (-8.31)*slope
print(f"O valor de Q é de: {Q}")