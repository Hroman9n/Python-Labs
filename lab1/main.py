# задача-получить список AdjClose и преобразовать из строк в числа

l = list()
AdjClose = list()

# читаем файл
with open("YNDX.csv", "r") as f:
    for i in f:
        l.append(i.strip().split(","))

# берём из файла только то, что нам необходимо
for i in l:
    AdjClose.append(i[-2])

# убираем первый элемент, так как он нам не нужен
AdjClose.pop(0)

# с помощью map преобразовываем список из строк в список из float
#  (int не подойдёт так как у нас не целые числа)
a = list(map(float, AdjClose))

# задача-найти, сколько мы смогли бы заработать, если бы знали стоймость акций за всё время

# стартовый баланс 100$, 0 акций
balance = 100
shares = 0

# покупаем акции в первый день
b = int(balance / a[0])
shares += b
balance -= (b * a[0])

# если цена акций на следующий день меньше, чем на сегодняшний
# продаём все акции, иначе покупаем их
for i in range(1, len(a)-2):
    if a[i] > a[i+1]:
        balance += (a[i] * shares)
        shares = 0
    else:
        b = int(balance / a[i])
        shares += b
        balance -= (b * a[i])

print("мы бы имели", balance, "долларов и", shares, "акций , либо", (balance + shares * a[i-1]),
      "долларов, если бы продали акции в последний день")
