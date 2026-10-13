"""5. Contratos con *args, **kwargs y zip

Diseña esta función, inspirada en el cálculo de varias velocidades de clase:

def velocidades(intervalos, *pares, **opciones):
    # Tu implementación
    ...
Cada elemento de intervalos es una duración en segundos; cada elemento de pares contiene exactamente dos posiciones en metros.
 Se calcula (posición final − posición inicial) / intervalo. Puedes asumir números y pares bien formados, 
 pero debes cumplir estas condiciones:

Debe existir al menos un par y la cantidad de intervalos debe coincidir con la de pares.
-Todos los intervalos deben ser positivos. Ante un incumplimiento, lanza ValueError.
-La única opción admitida es escala, cuyo valor por defecto es 1 y multiplica cada velocidad calculada. 
Supón una escala numérica; una clave desconocida también debe producir ValueError.
-Devuelve una lista y no modifica las entradas ni imprime desde la función. Incluye un contrato breve como docstring.
-Explica por qué usar zip sin verificar longitudes puede ocultar un error. Muestra cómo llamar a tu función 
desempaquetando estas colecciones:

intervalos = [2, 4]
pares = [(1, 7), (8, 0)]
opciones = {"escala": 3.6}
Comprueba una llamada válida y una con longitudes distintas. Explica qué recibiría la función si usaras pares sin *, 
y qué ocurriría con la opción mal escrita esacala. No se pide una interfaz interactiva."""




   #Función vista en clase que calcula velocidades a partir de intervalos y pares de posiciones, con opción de escala. 
def velocidad_media(desplazamiento_m: float, intervalo_s: float) -> float:
    """Devuelve la velocidad media en m/s; el intervalo debe ser positivo."""
    if intervalo_s <= 0:
        raise ValueError("el intervalo deben ser positivo")
    return desplazamiento_m / intervalo_s


#Función construida: 

def velocidades(intervalos, *pares, **opciones):
    """Calcula velocidades a partir de intervalos y pares de posiciones, con opción de escala.
    Devuelve una lista de velocidades; lanza ValueError si hay errores en los intervalos o en las opciones."""
    if len(intervalos) != len(pares):  #Una lista con 2 elementos que a su vez contienen dos elementos cada una (anidadas) por eso deben coincidir para no arrojar error.
        raise ValueError("La cantidad de intervalos debe coincidir con la de pares.")
    
    escala = opciones.get("escala", 1) #Para evitar errrores de clave desconocida, ejemplo esacala, se obtiene la opción "escala" con un valor por defecto de 1.
    for clave in opciones:
        if clave != "escala":
            raise ValueError("Opción desconocida.")
    
    velocidades_calculadas = []
    for intervalo, (pos_inicial, pos_final) in zip(intervalos, pares):
        if intervalo <= 0:
            raise ValueError("Todos los intervalos deben ser un número positivo.")
        desplazamiento = pos_final - pos_inicial
        velocidad = velocidad_media(desplazamiento, intervalo) * escala
        velocidades_calculadas.append(velocidad)
    
    return velocidades_calculadas