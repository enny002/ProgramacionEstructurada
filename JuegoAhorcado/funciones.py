import random 

alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"

def seleccionarPalabra():
  lineas = open ("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra

def entradaUsuario():
  letra = input("introduzca una letra ")
  return letra.lower() 

def actualizarJugada(palabra, letra, jugada):
  n_letras = len(palabra)

  for i in range (0, n_letras):
    if palabra[i] == letra:
      jugada[i] = letra
      
  return jugada

def actualizarAlfabeto(letra, alfabeto):
  alfabeto = alfabeto.replace(letra, " ")
  return alfabeto
 
def imprimirActualizacion(alfabeto, jugada):
  print(f"Jugada: {jugada}")
  print(f"letras disponibles: {alfabeto}")

def verificarJugada(suposicion, palabra):
  success = False
  if suposicion == palabra:
    success = True
  return success
