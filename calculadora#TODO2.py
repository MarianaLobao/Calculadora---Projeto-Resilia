n = float(input("Digite o número da população desejada: "))
e = float(0.05)
z = input("Digite a porcentagem de confiança desejada. Entre as opções: 80%, 85%, 90%, 95%, 99% : ")
p = (0.5)

if(z == '80') :
    z = 1.28
elif(z == '85') :
    z = 1.44
elif(z== '90') :
    z = 1.65
elif(z == '95') :
    z = 1.96
elif(z== '99') :
    z = 2.58
else:
    print("Opção inválida. Digite somente as porcentagens indicadas. Sem o sinal de porcentagem '%'.")


calculo1 = z * z 
calculo2 = p * (1 - p)
resultado1 = calculo1*calculo2
calculo3 = resultado1 / e**2


#SEGUNDO CÁLCULO

calculo4 = (z**2 * p)
calculo5 = 1 - p
resultado2 = calculo4 * calculo5
calculo6 = e * e 
calculo7 = calculo6 * n
resultado3 = 1+ (resultado2 / calculo7)

#RESULTADO FINAL 
resultado_final = calculo3 / resultado3


print(int(resultado_final))



#80% de confiança => escore z de 1,28.
#85% de confiança => escore z de 1,44.
#90% de confiança => escore z de 1,65.
#95% de confiança => escore z de 1,96.
#99% de confiança => escore z de 2,58.