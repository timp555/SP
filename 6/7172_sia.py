from threading import Thread, RLock
# https://docs.python.org/3/library/threading.html#lock-objects

result = []
lock = RLock()


# умножение двух векторов произвольной длины
def multiply_vectors(v1, v2, ind):
    global result
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same size")
    print(f"Thread {v1}: in progress (multiplying)")
    ans = sum(v1[i] * v2[i] for i in range(len(v1)))
    print(f"Thread {v1}: answer = {ans}")

    lock.acquire()
    print(f"Thread {v1}: acquired the lock")
    try:
        result[ind] = ans
    finally:
        lock.release()
        print(f"Thread {v1}: released the lock")


# умножает матрицу произвольного порядка на вектор, при этом умножение каждой строки на вектор производится в
# отдельном потоке
def multiply_matrix_v(m, v):
    row_count = len(m)
    global result
    # init array
    result = [0] * row_count
    print(f"Умножаю матрицу {m} на вектор {v}\n")
    threads = []
    for i in range(row_count):
        thread = Thread(target=multiply_vectors, name=str(m[i]), args=(m[i], v, i, ))
        threads.append(thread)
        print(f"Thread {thread.getName()}: starting")
        thread.start()
    for thread in threads:
        print(f"Thread {thread.getName()}: joining")
        thread.join()
        print(f"Thread {thread.getName()}: done")
    print(f"\nResult: {result}")


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 12, 32], [7, 6, 3], [13, 5, 1], [5, 7, 1]]
    vector = [5, 3, 2]
    multiply_matrix_v(matrix, vector)
