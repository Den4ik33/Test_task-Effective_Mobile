def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for ch_s, ch_t in zip(s, t):
        # Проверка соответствия s -> t
        if ch_s in map_s_t:
            if map_s_t[ch_s] != ch_t:
                return False
        else:
            map_s_t[ch_s] = ch_t

        # Проверка уникальности t -> s
        if ch_t in map_t_s:
            if map_t_s[ch_t] != ch_s:
                return False
        else:
            map_t_s[ch_t] = ch_s

    return True

# Пример
s = "paper"
t = "title"
print(is_isomorphic(s, t))  # True

# Оценка временной сложности
# Один проход по строкам длины n
# Все операции со словарём — O(1) в среднем
# T(n)=O(n)
#
# Память:
# В худшем случае храним до n различных символов в двух словарях
# S(n)=O(n)