# описание лабораторной работы https://pp.userapi.com/c852320/v852320476/3f939/-X5mhUUI8GQ.jpg
# ссылки из задания: http://bit.ly/2dgWxbg  http://bit.ly/2cAhv9p
# для скачивания библиотеки lxml необходимо прописать в командной строке pip install lxml

from lxml import etree

years = {}  # словарь для задания 1
actors_films = {}  # словарь для задания 2
actors_story = {}  # словарь для задания 3

doc = etree.parse('movies.xml')  # создаём DOM-дерево

root = doc.getroot()  # получаем корень дерева

for item in root.iter():
    if item.tag == 'year':
        try:
            year = int(item.text)
        except:
            continue
        if item.text in years.keys():                           # заполняем словарь для задания 1
            years[item.text] += 1
        else:
            years[item.text] = 1
    if item.tag == 'cast':
        for actor in item.iter():
            if actor.tag == 'actor':
                if actor.text in actors_films.keys():           # заполняем словарь для задания 2
                    actors_films[actor.text] += 1
                else:
                    actors_films[actor.text] = 1
                if actor.text not in actors_story.keys():       # заполняем словарь для задания 3
                    actors_story[actor.text] = [year, year]     # если актёра ещё нет в словаре, добавляем его
                else:
                    if year > actors_story[actor.text][1]:      # если текущий год больше позднего года съемок актёра
                                                                # меняем поздний год на текущий
                        actors_story[actor.text][1] = year
                    elif year < actors_story[actor.text][0]:    # если текущий год меньше раннего года съемок актёра
                                                                # меняем ранний год на текущий
                        actors_story[actor.text][0] = year


print("поиск актёра(-ов) с наибольшим кол-вом фильмов")     # задание 2
maximum = 0
for i in actors_films.values():                             # поиск рекорда по участию в фильмах
    if i > maximum:
        maximum = i

for key in actors_films:                                    # поиск актёра(-ов) с рекордом по участию в фильмах
    if actors_films[key] == maximum:
        print(key, "c", maximum, "фильмами")

print()

print("поиск трёх годов, в которых вышло")                  # задание 1
years_keys = list(years.keys())                             # создаём список лет
years_values = list(years.values())                         # создаём список кол-ва фильмов в разных годах
years_values.sort()                                         # сортируем список кол-ва фильмов
years_keys.sort()                                           # сортируем года по порядку
minYear1 = years_values[0]                       # берем первые 3 элемента из списка кол-ва фильмов т.к. он отсортирован
minYear2 = years_values[1]
minYear3 = years_values[2]
maxYear1 = years_values[-3]                      # берем последние 3 эл-та из списка кол-ва фильмов т.к. он отсортирован
maxYear2 = years_values[-2]
maxYear3 = years_values[-1]

print("минимальное кол-во фильмов")                         # подзадание 1 задания
iterations = 0                                              # счётчик нужен т.к. мы ищем только 3 фильма
for i in years_keys:                                        # цикл для поиска годов с минимальным кол-вом фильмов
    if iterations == 3:
        break
    elif years[i] == minYear1 or years[i] == minYear2 or years[i] == minYear3:
        print(i, ", в этом году вышло", years[i], "фильм(-ов)")
        iterations += 1

print("максимальное кол-во фильмов")                        # подзадание 1 задания
iterations = 0                                              # счётчик нужен т.к. мы ищем только 3 фильма

for i in years_keys:                                        # цикл для поиска годов с максимальным кол-вом фильмов
    if iterations == 3:
        break
    elif years[i] == maxYear1 or years[i] == maxYear2 or years[i] == maxYear3:
        print(i, ", в этом году вышло", years[i], "фильм(-ов)")
        iterations += 1

print()

print("поиск актёра с самой долгой карьерой")               # задание 3

toRemove = list(actors_story.keys())                        # список для отсева актёров снявшихся только в 1 фильме

for i in toRemove:                                          # цикл для отсева
    if actors_story[i][0] == actors_story[i][1]:
        actors_story.pop(i)

maximum = 0
actorName = ''

for i in actors_story:                                      # цикл для нахождения самой долгой актёрской карьеры
    if (actors_story[i][1] - actors_story[i][0]) > maximum:
        maximum = actors_story[i][1] - actors_story[i][0]
        actorName = i
print(actorName, maximum, "лет снимался в фильмах, c", actors_story[actorName][0], "по", actors_story[actorName][1])
