# лист с описанием лабороторной работы https://pp.userapi.com/c844521/v844521703/117e65/_5G3uhWWy-g.jpg

import xlrd

#БЛОК чтение Excel файла
wb = list()             # рабочая книга
summerMedals = list()   # список с общим кол-вом медалей в летних играх
winterMedals = list()   # список с общим кол-вом медалей в зимних играх

f = xlrd.open_workbook('olympicsalltime.xls')

sheet = f.sheet_by_index(0)

for i in range(sheet.nrows):
    row = sheet.row_values(i)
    wb.append(row)

#БЛОК создаём списки с общим кол-вом медалей для задач 1 и 2
for i in wb:
    summerMedals.append(i[2] + i[3] + i[4])
    winterMedals.append(i[6] + i[7] + i[8])

# убираем ненужные элементы
summerMedals.pop(0)
summerMedals.pop(-1)
winterMedals.pop(0)
winterMedals.pop(-1)

# задача 1

#БЛОК поиск 3 максимальных значений
m1 = m2 = m3 = 0
for j in range(len(summerMedals)):
    if summerMedals[j] > m1:
        m3 = m2
        m2 = m1
        m1 = summerMedals[j]
    elif summerMedals[j] > m2:
        m3 = m2
        m2 = summerMedals[j]
    elif summerMedals[j] > m3:
        m3 = summerMedals[j]

#БЛОК поиск названия стран
for i in wb:
    total = i[2] + i[3] + i[4]
    if (total) == m1:
        summer1st = i[0]
    elif (total) == m2:
        summer2nd = i[0]
    elif (total) == m3:
        summer3d = i[0]

# вывод ответа
print(summer1st, "на 1 месте с", m1, "медалями", summer2nd, "на 2 месте с", m2, "медалями", summer3d,
      "на 3 месте с", m3, "медалями")

print()

# задача 2
#БЛОК поиск 3 максимальных значений
m1 = m2 = m3 = 0
for j in range(len(winterMedals)):
    if winterMedals[j] > m1:
        m3 = m2
        m2 = m1
        m1 = winterMedals[j]
    elif winterMedals[j] > m2:
        m3 = m2
        m2 = winterMedals[j]
    elif winterMedals[j] > m3:
        m3 = winterMedals[j]

#БЛОК поиск названия стран
for i in wb:
    total = i[6] + i[7] + i[8]
    if (total) == m1:
        winter1st = i[0]
    elif (total) == m2:
        winter2nd = i[0]
    elif (total) == m3:
        winter3d = i[0]

# вывод ответа
print(winter1st, "на 1 месте с", m1, "медалями", winter2nd, "на 2 месте с", m2, "медалями", winter3d,
      "на 3 месте с", m3, "медалями")

print()

# задача 3
averSummerUSSR = (wb[108][2] + wb[108][3] + wb[108][4]) / wb[108][1]                    # среднее кол-во медалей СССР
                                                                                        # в летних играх
averWinterUSSR = (wb[108][6] + wb[108][7] + wb[108][8]) / wb[108][5]                    # среднее кол-во медалей СССР
                                                                                        # в зимних играх
print(averSummerUSSR, "в среднем СССР получил медалей в летних играх", averWinterUSSR,
      "в среднем СССР получил медалей в зимних играх")

print()

# задача 4
totalSummerPostUSSRmedals = 0   # всего медалей стран бывшего СССР в летних играх
totalWinterPostUSSRmedals = 0   # всего медалей стран бывшего СССР в зимних играх
totalSummerPostUSSRgames = 0    # кол-во летних игр в которых учавствовали страны бывшего СССР
totalWinterPostUSSRgames = 0    # кол-во зимних игр в которых учавствовали страны бывшего СССР

# БЛОК добавляем кол-во медалей и игр стран бывшего СССР (в табл 5, 9, 13, 40, 45, 69, 75, 76, 79, 85, 109, 127, 136, 140)
for i in range(len(wb)):
    if (i == 4 or i == 8 or i == 12 or i == 39 or i == 44 or i == 68 or i == 74 or i == 75 or i == 78 or i == 84 or
        i == 108 or i == 126 or i == 135 or i == 139):
        totalSummerPostUSSRmedals += (wb[i][2] + wb[i][3] + wb[i][4])
        totalWinterPostUSSRmedals += (wb[i][6] + wb[i][7] + wb[i][8])
        totalSummerPostUSSRgames += wb[i][1]
        totalWinterPostUSSRgames += wb[i][5]

averSummerPostUSSR = totalSummerPostUSSRmedals / totalSummerPostUSSRgames   # ссреднее кол-во медалей СССР
                                                                            # в летних играх
averWinterPostUSSR = totalWinterPostUSSRmedals / totalWinterPostUSSRgames   # среднее кол-во медалей СССР
                                                                            # в зимних играх

print(averSummerPostUSSR, "в среднем бывшие страны СССР получили медалей в летних играх", averWinterPostUSSR,
      "в среднем бывшие страны СССР получили медалей в зимних играх")