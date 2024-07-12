#Você descobriu um sebo perto da sua casa e resolve dar uma olhada e encontra muitos títulos interessantes. Mas como você não está nadando em dinheiro, 
# terá que fazer algumas escolhas. Escreva um programa que retorne se você deverá comprar ou não o livro, considerando que ele precisa estar na sua wishlist 
# (nada de comprar por impulso) e o preço do sebo deve ser mais barato do que na internet.

#a) Você deverá comprar Moby Dick?

#b) Você deverá comprar Crime e Castigo?

#c) Você deverá comprar a Odisseia?

preco_moby_dick_internet = 15.35
preco_crime_castigo_internet = 49.90
preco_odisseia_internet = 66.41


preco_moby_dick_sebo = 20.0
preco_crime_castigo_sebo = 18.0
preco_odisseia_sebo = 30.0


wishlist = ["Moby Dick", "Crime e Castigo", "Odisseia"]


def decidir_compra(livro, preco_internet, preco_sebo):
    if livro in wishlist and preco_sebo < preco_internet:
        return "Comprar no sebo"
    else:
        return "Não comprar"

comprar_moby_dick = decidir_compra("Moby Dick", preco_moby_dick_internet, preco_moby_dick_sebo)

comprar_crime_castigo = decidir_compra("Crime e Castigo", preco_crime_castigo_internet, preco_crime_castigo_sebo)

comprar_odisseia = decidir_compra("Odisseia", preco_odisseia_internet, preco_odisseia_sebo)

print("Devo comprar Moby Dick?" , comprar_moby_dick)
print("Devo comprar Crime e Castigo?" , comprar_crime_castigo)
print("Devo comprar a Odisseia?" , comprar_odisseia)

