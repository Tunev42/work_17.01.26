import time
import tracemalloc
import random

def block_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Проход слева направо
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Если не было обменов = массив отсортирован
        if not swapped:
            break

        # Уменьшаем правую границу ведь последний элемент уже на месте
        end -= 1

        # Проход справа налево
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Увеличиваем левую границу так как первый элемент уже на месте
        start += 1

    return arr


def measure_memory_and_time(func, *args):


    tracemalloc.start()
    start_time = time.time()

    result = func(*args)


    end_time = time.time()

    snapshot = tracemalloc.take_snapshot()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = end_time - start_time

    return result, execution_time, current, peak, snapshot



if __name__ == "__main__":

    test_cases = [
        (["Конь", "Ослик", "Рыбка", "Лиса"], "Тест 1: Слова"),
        (['$', '!','@', '#', '%', '^', '&',  '*'], "Тест 2: Символы"),
        ([random.randint(0, 9)for i in range(10)], "Тест 3: Цифры"),
    ]

    for i, (test_array, description) in enumerate(test_cases, 1):
        print(f"\n{description}")
        print(f"Исходный массив: {test_array}")

        # Измеряем производительность
        sorted_array, exec_time, current_mem, peak_mem, snapshot = measure_memory_and_time(
            block_sort, test_array.copy()
        )

        print(f"Отсортированный: {sorted_array}")
        print(f"Время выполнения: {exec_time:.6f} секунд")
        print(f"Затрачено памяти: {current_mem / 1024:.2f} KB")



        for stat in snapshot.statistics('lineno')[:5]:
            print(f"  {stat.traceback.format()[:80]}...")
            print(f"    Размер: {stat.size / 1024:.2f} KB")
        print("-" * 50)




