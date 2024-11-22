from math import ceil

def compare_positive_elements(sequence: list[int]) -> str:
    n = len(sequence)
    if n == 0:
        return "Послідовність порожня."
    
   
    mid = ceil(n / 2)  
    first_half = sequence[:mid]
    second_half = sequence[mid:]

    positive_in_first = sum(1 for x in first_half if x > 0)
    positive_in_second = sum(1 for x in second_half if x > 0)

    if positive_in_first > positive_in_second:
        return "У першій половині більше додатних елементів."
    elif positive_in_first < positive_in_second:
        return "У другій половині більше додатних елементів."
    else:
        return "Кількість додатних елементів в обох половинах однакова."

sequence = [1, -3, 5, 6, -2, 8, -1]
result = compare_positive_elements(sequence)
print(result)
