import time

labs = list()
e1 = 0
e2 = 0
nl = 0

if __name__ == "__main__":  
    inicio_global = time.perf_counter()

    # Inicio de operaciones de entrada/salida
    inicio_es = time.perf_counter()

    for idx in range(10):
        nota = float(input(f"Ingrese nota del laboratorio {idx + 1}: "))
        labs.append(nota)
    
    e1 = float(input("Ingrese nota del examen 1: "))
    e2 = float(input("Ingrese nota del examen 2: "))

    fin_es = time.perf_counter()
    # Fin de operaciones de entrada/salida

    # Inicio de procesamiento
    inicio_cpu = time.perf_counter()

    for nota in labs:
        nl += nota
    
    nl /= len(labs)

    nota_final = (50 * nl + 25 * e1 + 25 * e2) / 100

    fin_cpu = time.perf_counter()

    fin_global = time.perf_counter()

    print(f"Nota final: {nota_final}")
    print(f"Tiempo de entrada/salida: {fin_es - inicio_es} segundos")
    print(f"Tiempo de procesamiento: {fin_cpu - inicio_cpu} segundos")
    print(f"Tiempo total: {fin_global - inicio_global} segundos")

    print(f"Valores porcentuales: Tiempo de E/S -> {100 * (fin_es - inicio_es) / (fin_global - inicio_global)}%, Tiempo de CPU -> {100 * (fin_cpu - inicio_cpu) / (fin_global - inicio_global)}%")


