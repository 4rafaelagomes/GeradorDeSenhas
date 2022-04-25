import random
senhalen = int(input("Digite o tamanho da senha: "))
caracteres ="qwertyuiopasdfghjklzxcvbnm0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ!#@*&/?"
senha = "".join(random.sample(caracteres,senhalen ))
print(senha)
