def missing_number(nums: list[int]) -> int:
    n = len(nums) + 1  # так как одно число отсутствует
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Пример
nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(missing_number(nums))  # 7

# Оценка временной сложности:
# Один проход по массиву для sum(nums)
# Остальные операции — O(1)
# T(n)=O(n)
#
# Память:
# Используются только несколько переменных
# S(n)=O(1)