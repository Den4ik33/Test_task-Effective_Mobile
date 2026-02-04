def prime_factors(n: int) -> list[int]:
    factors = []

    # Делим на 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Делим на нечётные числа до sqrt(n)
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2

    # Если осталось простое число > 1
    if n > 1:
        factors.append(n)

    return factors

# Пример
n = 56
print(prime_factors(n))  # [2, 2, 2, 7]

# Оценка временной сложности:
# В худшем случае проверяются делители до √n
# T(n)=O(sqrt(n))
#
# Память:
# Хранится только список множителей
# Максимум O(log n) элементов (например, для степени двойки)
# S(n)=O(logn)