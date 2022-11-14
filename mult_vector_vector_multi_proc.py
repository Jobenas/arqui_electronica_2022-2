import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count

M = 5_000
N = 5_000

pool_multiplier = 1

def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(y)):
        suma += x[i] * y[i]
    
    return suma


if __name__ == '__main__':
    resultado = []

    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(M, ))

    inicio = time.perf_counter()
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=cpu_count() * pool_multiplier)
    resultado = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")