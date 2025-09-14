def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c.isalpha():# Esto musetra que c solo tenga letras
            base = ord('A') if c.isupper() else ord('a') #Cuando se usa minuscula y mayuscula y dependiendo de esto va a variar el codigo ASCII
            resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado

def descifrado_cesar(texto_cifrado, desplazamiento):
    return cifrado_cesar(texto_cifrado, -desplazamiento)

# Ejemplo de uso
mensaje = "Hola Mundo"
desplazamiento = 3

mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)
mensaje_descifrado = descifrado_cesar(mensaje_cifrado, desplazamiento)

print("Mensaje original:  ", mensaje)
print("Mensaje cifrado:   ", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)
