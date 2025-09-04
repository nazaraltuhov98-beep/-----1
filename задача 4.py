sec = int(input("Секунды: "))

d = sec // 86400
sec = sec % 86400

h = sec // 3600
sec = sec % 3600

m = sec // 60
s = sec % 60

print(d, h, m, s)
