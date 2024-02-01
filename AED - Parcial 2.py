'''

Vega Marconetto, Máximo (90788) - 1k6
Turno 03 – Enunciado 01 [T3E1]

Determinar la cantidad de palabras que contienen el primer caracter de todo el texto
(minúscula o mayúscula si es letra) en la segunda posición de dicha palabra.
Por ejemplo, en el texto "Al manso caballo le gusta pastar."
hay 3 palabras que cumplen el criterio ("manso", "caballo" y "pastar").

Determinar el porcentaje de palabras (con respecto al total de palabras de texto)
que contienen una vocal (minúscula o mayúscula) en la tercera posición y una consolante
(minúscula o mayúscula) en la cuarta. Por ejemplo, en el texto
"La mentalidad sobre los peajes es enervante." hay 7 palabras en total
y 2 palabras que cumplen con el criterio ("peajes" y "enervante").
Por lo tanto el porcentaje seria 28.57%.

Determinar la cantidad de palabras que contienen mas de 5 caracteres y
que NO COMIENCEN con el ultimo caracter de la primera palabra del texto.
Por ejemplo, en el texto "Comenzamos a silenciar los micrófonos en el parcial."
hay 2 palabras que cumplen el criterio ("micrófonos" y "parcial").
Por "caracteres", se entiende "cualquier tipo de símbolo, sea este un dígito, una letra,
o cualquier otro que pueda aparecer".

Determinar la cantidad de palabras que contienen la secuencia "t" seguida de una vocal
cualquiera (con cualquiera de sus letras en minúscula o en mayúscula) pero de forma
tal que la secuencia esté presente en las primeras cuatro letras de la palabra.
Por ejemplo, en el texto "La atenta mirada de la tia explota de amor." hay 2 palabras
que cumplen con el criterio ("atenta" y "tia"). La palabra "explota" tiene una
secuencia t+vocal, pero no entre las primeras cuatro letras, por lo que no debe ser
contada.'''

print()

# Funicon para identificar si el caracter es una vocal
def es_vocal(car):
    return car in 'aeiou'


# Funicon para identificar si el caracter es una consonante
def es_consonante(car):
    return car in 'bcdfghjklmnñopqrstvwxyz'


# Funcion para identificar el porcentaje de palabras con ciertas caracteristicas
# en la cantidad de palabras de la cadena
def porcentaje(palabras, total_palabras):

    porcentaje = palabras * 100 / total_palabras
    return round(porcentaje, 2)


def test():

    '''DEFINICION DE VARIABLES'''

    cont_letras_palabras = 0
    cont_palabras = 0

    # Variables ejercicio 1
    segundo_caracter_igual = False
    cont_segundo_caracter_igual = 0

    # Variables ejercicio 2
    tercera_vocal = cuarta_consonante = False
    cont_vocal_consonante = 0

    # Variables ejercicio 3
    primer_caracter_palabra = ultimo_caracter = None
    cont_priemr_igual_ultimo = 0

    # Variables ejercicio 4
    t = t_vocal = False
    posicion_t_vocal = cont_palabra_t_vocal = 0



    print('*'* 10, 'ANALISIS DE CADENA DE CARACTERES', '*' * 10)
    print()

    # Se pide ingresar la cadena de caracteres
    texto = input('Ingrese un texto, finalizandolo con un punto: ')
    print()

    # Validacion que la cadena finalice con un punto
    while texto[-1] != '.':
        texto = input('Por favor, ingrese el texto terminando con un punto: ')
        print()

    # Transformar todas los caracteres en minusculas
    texto = texto.lower()

    # Inicia el procesamiento caracter por caracter
    for car in texto:

        # Si el caracter es diferente a un espacio o un punto, estamos dentro de una palabra
        if car != ' ' and car != '.':

            # Cuenta los caracteres de la palabra en analisis
            cont_letras_palabras += 1

            #PUNTO 1

            # Se identifica el primer caracter del texto
            priemer_caracter = texto[0]

            # Se identifica si el segundo caracter de cada palabra
            # es igual al primero del texto
            if cont_letras_palabras == 2 and car == priemer_caracter:
                segundo_caracter_igual = True

            #PUNTO 2

            # Se identifica si el tercer caracter de cada palabra
            # es una vocal
            if cont_letras_palabras == 3 and es_vocal(car):
                tercera_vocal = True

            # Se identifica si el cuarto caracter de cada palabra
            # es una consonante
            if cont_letras_palabras == 4 and es_consonante(car):
                cuarta_consonante = True

            # PUNTO 3

            # Se identifica el ultimo caracter de la primera palabra de al cadena
            if cont_palabras == 0:
                ultimo_caracter = car

            # Se identifica el primer caracter de cada palabra a partir de
            # la segunda palabra
            else:
                if cont_letras_palabras == 1:
                    primer_caracter_palabra = car

            # PUNTO 4

            # Se identifica si hay alguna t
            if car == 't':
                t = True

            else:
                # Se identifica si hay alguna vocal despues de una t
                if t and es_vocal(car):
                    t_vocal = True
                    posicion_t_vocal = cont_letras_palabras

                t = False



        # El caracter es un espacio o un punto, indicando que termino una palabra
        else:

            # Si los primeros caracteres son un espacio, continuar con el siguiente caracter
            if cont_letras_palabras == 0:
                continue

            # Contador de palabras
            cont_palabras += 1

            # PUNTO 1
            # Cuenta las palabras que cumplan con la condicion del punto 1
            if segundo_caracter_igual:
                cont_segundo_caracter_igual += 1

            # PUNTO 2
            # Cuenta las palabras que cumplan con la condicion del punto 2
            if tercera_vocal and cuarta_consonante:
                cont_vocal_consonante += 1

            # PUNTO 3:
            # Cuenta las palabras que cumplan con la condicion del punto 3
            if cont_palabras > 1:
                if cont_letras_palabras > 5 and \
                        primer_caracter_palabra != ultimo_caracter:

                    cont_priemr_igual_ultimo += 1

            # PUNTO 4
            # Cuenta las palabras que cumplan con la condicion del punto 4
            if t_vocal and posicion_t_vocal < 4:
                cont_palabra_t_vocal += 1

            '''REINICIALIZACION DE VARIABLES'''
            cont_letras_palabras = 0
            segundo_caracter_igual = False
            tercera_vocal = cuarta_consonante = False
            primer_caracter_palabra = None
            t = t_vocal = False
            posicion_t_vocal = 0




    print('*' * 10, 'RESULTADOS', '*' * 10)
    print()

    # PUNTO 1
    print('Ejercicio 1')
    print('Cantidad de palabras que contienen el primer caracter del texto en \n'
          'la segunda posición de la palabra:', cont_segundo_caracter_igual, 'palabras')
    print()

    # PUNTO 2
    print('Ejercicio 2')
    if cont_palabras > 0:
        porcent = porcentaje(cont_vocal_consonante, cont_palabras)

        print('La cantidad de palabras que contienen una vocal en la tercera \n'
              'posición y una consolante en la cuarta es de', cont_vocal_consonante, '\n' 
              'palabras. Y su porcentaje respecto al texto es:', porcent, '%')

        print()
    else:
        print('El porcentaje no se puede calcular')

    # PUNTO 3
    print('Ejercicio 3')
    print('Cantidad de palabras de mas de 5 caracteres y que no comienzan \n'
          'con el ultimo caracter de la primera palabra del texto:', cont_priemr_igual_ultimo, 'palabras')
    print()

    # PUNTO 4
    print('Ejercicio 4')
    print('Cantidad de palabras que contienen la secuencia "t" seguida de una vocal \n'
          'cualquiera  en las primeras cuatro letras de la palabra:', cont_palabra_t_vocal, 'palabras')
    print()

    print('Programa terminado')


# Chequeo de la variable __name__
if __name__ == '__main__':
    test()
