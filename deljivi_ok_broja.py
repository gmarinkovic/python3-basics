# Дати су цели бројеви n и k. Напиши програм који одређује највећи цео број l ≤ n дељив бројем k и најмањи
# цео број d ≥ n дељив бројем k.
#
# Улаз: Са стандардног улаза уносе се два цела броја (сваки у посебном реду).
# • n (0 ≤ n ≤ 100000)
# • k (1 ≤ k ≤ 10000)
#
# Излаз: На стандардни излаз исписати два тражена цела броја, сваки у посебном реду.
#
# Пример 1
# Улаз
# 23
# 5
# Излаз
# 20
# 25
#
# Пример 2
# Улаз
# 49
# 7
# Излаз
# 49
# 49

n = int(input("Unesi broj n :" ))
k = int(input("Unesi broj k :" ))

l = n//k * k
d = (n+k-1)//k * k

print("Najveci ceo broj l koji je manji od n a deljiv sa k je: ",l)
print("Najveci ceo broj d koji je veci od n a deljiv sa k je: ",d)