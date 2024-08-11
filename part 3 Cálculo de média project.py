# condicionais if elif else
#condicionl simples

#calculo de media 

n1=n2=0.0 # duas variaveis sem nota

media= 0.0

n1= float(input("digite a prmeira not: "))
n2= float(input("diite a segnda nota: "))


#calculo
media=(n1+n2) / 2
if (media >=7):
	print('aprovado')
	print('parabens')
elif (media >=5):
	print('voce esta de recuperaçao')

  # >=5 n passando da media 7

else:
	print('reprovdo')
	
print('sua media é {}'. format (media))# a presentamos a media desse jeito

#programa concluido 