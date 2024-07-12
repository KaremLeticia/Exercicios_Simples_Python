#Que as festas da faculdade são patrimônio universitário, todo mundo sabe, mas se a gente for em todas, não há carteira que aguente. Pior é pagar por uma festa agora e não 
#ter grana para uma festa melhor depois. Assim, para lidar com essa volatilidade, você decide aplicar umas jogadas do mercado financeiro e de quebra, escrever uns códigos
#Você paga $40 reais para seu amigo. Em troca, ele deverá pagar o seu ingresso para a próxima festa, independente do valor. Se o ingresso for mais caro, você se deu bem, 
#se for mais barato, você se deu mal. Escreva um código que receba o input do valor do próximo ingresso, indique se foi uma operação vantajosa e o quanto você perdeu ou economizou.

valor_pago_ao_amigo = 40.00

valor_do_proximo_ingresso = float(input("Quanto está custando o ingresso da próxima festa? "))

diferenca = valor_do_proximo_ingresso - valor_pago_ao_amigo

if diferenca > 0 :
  print("Você se deu bem e economizou R$", round(diferenca, 2))
elif diferenca < 0:
  print("Você se deu mal e pagou R$", round(abs(diferenca), 2),"a mais ao seu amigo")
else :
  print("Você gastou o mesmo valor no ingresso")