import os
import multiprocessing as mp

# https://docs.python.org/3/library/multiprocessing.html

# Задание: написать две программы. Первая реализует алгоритм умножения двух векторов произвольной длины. Вторая -
# умножает матрицу произвольного порядка на вектор, при этом умножение каждой строки на вектор производить в
# отдельном процессе.

# #### MAIN RULES #####
# Матрицы A и B могут быть перемножены, если они совместимы в том смысле, что число столбцов
# матрицы A равно числу строк B. // Произведение матриц AB состоит из всех возможных комбинаций скалярных произведений
# вектор-строк матрицы A и вектор-столбцов матрицы B. Элемент матрицы AB с индексами i, j есть скалярное произведение
# i-ой вектор-строки матрицы A и j-го вектор-столбца матрицы B.


# умножение двух векторов произвольной длины
def multiply_vectors(v1, v2, q):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same size")
    print(f"Процесс {{PID={os.getpid()}, PPID={os.getppid()}}}: умножаю {v1} на {v2}")
    ans = sum(v1[i] * v2[i] for i in range(len(v1)))
    print(f"Процесс с PID {os.getpid()}: получил ответ: {ans}")
    q.put(ans)


# умножает матрицу произвольного порядка на вектор, при этом умножение каждой строки на вектор производится в
# отдельном процессе
def multiply_matrix_v(m, v):
    print(f"Процесс {{PID={os.getpid()}, PPID={os.getppid()}}}: умножаю матрицу")
    procs = []
    # shared between processes data structure
    q = mp.Queue()
    result = [0 for _ in range(len(m))]
    for i in range(len(m)):
        proc = mp.Process(target=multiply_vectors, args=(m[i], v, q))
        procs.append(proc)
        # execute the process
        proc.start()
        # get the return value
        result[i] = q.get()
    # terminating processes
    # On Unix when a process finishes but has not been joined it becomes a zombie.
    for proc in procs:
        proc.join()
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 6, 3], [13, 5, 1]]
    vector = [5, 2, 3]
    print(f"Матрица: {matrix}")
    print(f"Вектор: {vector}\n")
    res = multiply_matrix_v(matrix, vector)
    print(f"\nРезультат умножения матрицы на вектор: {res}")
