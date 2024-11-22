
#Швидке сортування;
def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + middle + quick_sort(right)  

# 2. Пошук елемента за значенням
def search_element(arr, value):
    try:
        return arr.index(value)  
    except ValueError:
        return -1  

# 3. Пошук перших п’яти мінімальних елементів
def find_min_five(arr):
    return sorted(arr)[:5]  

# 4. Пошук середнього арифметичного
def find_average(arr):
    if len(arr) == 0:
        return 0  
    return sum(arr) / len(arr) 

# 5. Повернення списку без повторів
def remove_duplicates(arr):
    return list(set(arr))  

# Приклад використання функцій
if __name__ == "__main__":

    data = [3, 1, 2, 5, 2, 8, 1, 9, 3, 0]

    # 1. Швидке сортування
    sorted_data = quick_sort(data)
    print("Відсортований список:", sorted_data)

    # 2. Пошук елемента
    element_index = search_element(data, 5)
    print("Індекс елемента 5:", element_index)

    # 3. Пошук перших п’яти мінімальних елементів
    min_five = find_min_five(data)
    print("Перші п’ять мінімальних елементів:", min_five)

    # 4. Пошук середнього арифметичного
    average = find_average(data)
    print("Середнє арифметичне:", average)

    # 5. Список без повторів
    unique_data = remove_duplicates(data)
    print("Список без повторів:", unique_data)
