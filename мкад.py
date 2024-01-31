v = int(input('v = '))
t = int(input('t = '))
mkad = 109
s = v * t
if v > 0:
    x = s % mkad
else:
    x = mkad - (abs(s) % mkad)
print(f'точка остановки находится на {x} км МКАДа')