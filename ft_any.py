def ft_any(tab, f):
    i = 0
    while tab[i:]:
        if f(tab[i]) == 1:
            return 1
        i += 1
    return 0