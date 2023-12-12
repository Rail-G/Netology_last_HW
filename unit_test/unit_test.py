courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

def mentors_name():
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)
    return mentors_names

def course():
    mentor_name = mentors_name()
    list_ = []
    for id1 in range(len(mentor_name)):
        for id2 in range(len(mentor_name)):
            if id1 != id2 and id1 < id2:
                intersection_set = set(mentor_name[id1]) & set(mentor_name[id2])
                if len(intersection_set) > 0:
                    all_names_sorted = sorted(intersection_set)
                    list_.append(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")
    return '\n'.join(list_)


def all_names():
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    return all_names_list

def unique_name():
    all_name = all_names()
    unique_names = set(all_name)
    return unique_names

def popular_names():
    unique = unique_name()
    all_name = all_names()
    popular = []
    for name in unique:
        popular.append([name, all_name.count(name)]) 
    return popular

def result():
    popular = popular_names()
    popular.sort(key=lambda x:x[1], reverse=True)

    top_3 = popular[0:3]
    var = []
    for el, num in top_3:
        var.append(el + ': ' + str(num) + ' раз(а)')
    return ', '.join(var)

codes_info = [
	"",
	"1 — число цели, которая проявляется в форме агрессивности и амбиций",
	"2 — число равновесия и контраста одновременно, поддерживает равновесие, смешивая позитивные и негативные качества",
	"3 — неустойчивость, объединяет талант и весёлость, символ приспосабливаемости",
	"4 — означает устойчивость и прочность",
	"5 — символизирует риск, свободу и душевное беспокойство, которое толкает человека к путешествиям и новому опыту. С одной стороны, это самое счастливое число, с другой — самое непредсказуемое",
	"6 — символ надёжности. Идеальное число, которое делится как на чётное, так и на нечётное, объединяя элементы каждого",
	"7 — символизирует тайну, а также изучение и знание как путь исследования неизвестного и невидимого",
	"8 — число материального успеха, означает надёжность, доведённую до совершенства, символ всеобщего успеха",
	"9 — указывает на сильную личность с потенциальным интеллектом, способную к высокому развитию"
]

def calc_namecode(name):
	letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
			   "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

	name = name.upper()
	code = 0
	for letter in name:
		try:
			ltr_code = letters.index(letter) % 9
		except:
			continue
		if ltr_code == 0:
			ltr_code = 9
		code += ltr_code

	while code > 9:
		curr = code // 10 + code % 10
		code = curr

	return code

def names_code():
    unique_names = unique_name()
    names_codes = [[] for n in range(10)]

    for name in unique_names:
        code = calc_namecode(name)

        names_codes[code].append(name)
    return names_codes

def result_codes():
    names_codes = names_code()
    list_ = []
    for id, _ in enumerate(names_codes):
        if id != 0:
            print(codes_info[id])
            all_names_sorted = sorted(names_codes[id])
            list_.append(f"Коду {id} соответствуют: {', '.join(all_names_sorted)}")
    return '\n'.join(list_)
