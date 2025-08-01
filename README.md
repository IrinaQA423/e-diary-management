# `scripts.py` — управление электронным дневником через `shell`

Модуль `scripts.py` содержит 3 функции для внесения изменений  в базу  данных электронного дневника.

## Функции

1. `fix_marks(schoolkid)` - заменяет все оценки 2 и 3 у заданного ученика на 5.

2. `remove_chastisements(schoolkid)`- удаляет все замечания у заданного ученика.

3. `create_commendation(schoolkid, subject)`- добавляет случайную похвалу для заданного ученика по предмету (cписок записей для похвалы хранится в `COMMENDATIONS` внутри `scripts.py`).

## Как использовать

1. Запустите Django shell.

```
python manage.py shell
```

2. Импортируйте функции:

```
from scripts import fix_marks, remove_chastisements, create_commendation
from datacenter.models import Schoolkid, Lesson, Commendation, Subject, Mark, Chastisement
import random
```
3. Найдите ученика. Например, Фрoлов Иван:

```
schoolkid = Schoolkid.objects.get(full_name__contains='Фролов Иван')
```

4. Используйте функции:
```
fix_marks(schoolkid)
remove_chastisements(schoolkid)
create_commendation('Фролов Иван', 'Музыка')
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).