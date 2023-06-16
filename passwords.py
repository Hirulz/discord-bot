import random 


elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
print("Bienvenido a este generador de contraseñas") 

pass_length = int(input("De cuantos caracteres quieres tu contraseña?: "))
password="";

for i in range(pass_length):
    password+=random.choice(elements)
print('Esta es tu nueva contraseña:', password)