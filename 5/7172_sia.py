from threading import Thread
# https://docs.python.org/3/library/threading.html

# Задание: написать две программы. Первая реализует алгоритм умножения двух векторов произвольной длины. Вторая -
# умножает матрицу произвольного порядка на вектор, при этом умножение каждой строки на вектор производить в
# отдельном процессе.

# #### MAIN RULES #####
# Матрицы A и B могут быть перемножены, если они совместимы в том смысле, что число столбцов
# матрицы A равно числу строк B. // Произведение матриц AB состоит из всех возможных комбинаций скалярных произведений
# вектор-строк матрицы A и вектор-столбцов матрицы B. Элемент матрицы AB с индексами i, j есть скалярное произведение
# i-ой вектор-строки матрицы A и j-го вектор-столбца матрицы B.


# умножение двух векторов произвольной длины
def multiply_vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same size")
    print(f"Thread {v1}: in progress (multiplying)")
    ans = sum(v1[i] * v2[i] for i in range(len(v1)))
    print(f"Thread {v1}: answer = {ans}")
    return ans


# умножает матрицу произвольного порядка на вектор, при этом умножение каждой строки на вектор производится в
# отдельном потоке
def multiply_matrix_v(m, v):
    print(f"Умножаю матрицу {m} на вектор {v}\n")
    threads = []
    for row in m:
        thread = Thread(target=multiply_vectors, name=str(row), args=(row, v, ))
        threads.append(thread)
        print(f"Thread {thread.getName()}: starting")
        thread.start()
    for thread in threads:
        print(f"Thread {thread.getName()}: joining")
        thread.join()
        print(f"Thread {thread.getName()}: done")


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 6, 3], [13, 5, 1]]
    vector = [5, 2, 3]
    multiply_matrix_v(matrix, vector)
