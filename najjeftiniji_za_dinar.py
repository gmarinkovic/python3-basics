# У једној продавници је у току акција у којој се купцима који купе три производа нуди да најјефтинији од та
# три производа добију за један динар. Напиши програм који одређује снижену цену три производа.
# Улаз: Са стандардног улаза уносе се три цела броја из интервала од 50 до 5000 који представљају цене у
# динарима за три купљена производа.
# Излаз: На стандардни излаз исписати један цео број који представља укупну снижену цену та три производа.
#
# Пример
# Улаз
# 2499
# 3599
# 899
# Излаз
# 6099

a = int( input("Unesi cenu prvog proizvoda: "))
b = int( input("Unesi cenu drugog proizvoda: "))
c = int( input("Unesi cenu treceg proizvoda: "))

suma = a+b+c
minimum= min(a,b,c)

ukupna_cena = suma-minimum +1
