# Взять функцию подсчета чисел Фибоначчи и сравнить время исполнения кода 
# (вызова функции от большого числа n (чтобы была видна разница в запусках на потоках и процессах) 10 раз, 
# каждая на отдельном потоков\процессов) при использовании threading и multiprocessing. Запускаем одновременно 10 потоков/процессов, сравниваем общее время.
# Необходимо сравнить время выполнения при синхронном запуске, использовании потоков и процессов. 

import threading
import multiprocessing
import time

# Функция для подсчета чисел Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Функция для выполнения подсчета чисел Фибоначчи синхронно
def synchronous_fibonacci(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time

# Функция для выполнения подсчета чисел Фибоначчи с использованием потоков
def threaded_fibonacci(n):
    start_time = time.time()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    return end_time - start_time

# Функция для выполнения подсчета чисел Фибоначчи с использованием процессов
def processed_fibonacci(n):
    start_time = time.time()
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    n = 35 
    
    # Синхронный подсчет
    synchronous_time = synchronous_fibonacci(n)
    print("Синхронно:", synchronous_time)

    # Многопоточный подсчет
    threaded_time = threaded_fibonacci(n)
    print("Потоки:", threaded_time)

    # Многопроцессорный подсчет
    processed_time = processed_fibonacci(n)
    print("Процессы:", processed_time)
