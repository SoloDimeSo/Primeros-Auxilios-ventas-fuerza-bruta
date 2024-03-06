from string import ascii_lowercase

abc = ascii_lowercase
print(type(abc))

password = input("ingrese la clave")

contador = 0

for letra in password:
    for caracter in abc:
        contador += 1
        if letra == caracter:
            break
        
        
print(f"la palabra se encontro en {contador} interaciones") 
        
def main():
    password_oculta = input("Ingrese la contraseña oculta: ")
    intentos = caracter (password_oculta)
    print(f"La contraseña fue forzada en {contador} intentos")

if password == "gato":
    main()