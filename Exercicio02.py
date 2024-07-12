#2022 é ano de eleição para presidência da república e para o governo estadual. Faça um programa que ao digitar a idade, ele diga se a pessoa pode votar, se é obrigatório ou não.

idade = int(input("Digite a sua idade: "))
if idade >= 18: #Os dois pontos (:) após o if idade >= 18 em Python vão indicar o início de um bloco de código que deve ser executado se a condição especificada no if for verdadeira.
        if idade >= 70 or (idade >= 16 and idade < 18):
            print("Você pode votar, mas o voto é facultativo")
        
        else:
              print("Você pode votar, e o voto é obrigatório!")
        
else: 
      print("Você não pode votar ainda!")