print("Ваши фамилия, имя?")
a = input()
print("Сколько Вам лет?")
b = input()
print("Где вы живете?")
c = input()
t = int(b)
if 11 <= t % 100 <= 14:
    x = "лет"
else:
    r = t % 10
    if r == 1:
        x = "год"
    elif 2 <= r <= 4:
        x = "года"
    else:
        x = "лет"

print('Студента зовут',a,', ему',b, x,' и он живёт в',c)
