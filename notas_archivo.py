import time
import pprint


def procesa_datos(cabecera: list[str], datos: list[str]):
    notas = dict()

    for dato in datos:
        valores = dato.split(",")
        notas[valores[0]] = dict()
        try:
            for i in range(10):
                notas[valores[0]][cabecera[i+1]] = float(valores[i+1])
            notas[valores[0]][cabecera[10]] = float(valores[10])
            notas[valores[0]][cabecera[11]] = float(valores[11])
        except ValueError:
            del notas[valores[0]]
            continue
    
    return notas

if __name__ == "__main__":
    inicio_global = time.perf_counter()

    # Inicio de operaciones de entrada/salida
    inicio_es = time.perf_counter()

    with open("notas.csv", 'r') as f:
        contenido = f.read()
    # f = open("notas.csv", 'r')
    # contenido = f.read()
    # f.close()
    
    fin_es = time.perf_counter()
    # Fin de operaciones de entrada/salida

    # Inicio de procesamiento
    inicio_cpu = time.perf_counter()

    lineas = contenido.split("\n")
    cabecera = lineas[0].split(",")
    data = lineas[1:3]

    datos_notas = procesa_datos(cabecera, data)
  
    pprint.pprint(datos_notas)

    # for nota in labs:
    #     nl += nota
    
    # nl /= len(labs)

    # nota_final = (50 * nl + 25 * e1 + 25 * e2) / 100

    # fin_cpu = time.perf_counter()

    # fin_global = time.perf_counter()

    # print(f"Nota final: {nota_final}")
    # print(f"Tiempo de entrada/salida: {fin_es - inicio_es} segundos")
    # print(f"Tiempo de procesamiento: {fin_cpu - inicio_cpu} segundos")
    # print(f"Tiempo total: {fin_global - inicio_global} segundos")

    # print(f"Valores porcentuales: Tiempo de E/S -> {100 * (fin_es - inicio_es) / (fin_global - inicio_global)}%, Tiempo de CPU -> {100 * (fin_cpu - inicio_cpu) / (fin_global - inicio_global)}%")
