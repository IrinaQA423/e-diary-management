from datacenter.models import Schoolkid, Lesson, Commendation, Subject, Mark, Chastisement
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random

COMMENDATIONS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Потрясающе!',
    'Замечательно!',
    'Так держать!',
    'Здорово!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!'
]


def get_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
        
    except ObjectDoesNotExist:
        print(f"Ученик с именем '{name}' не найден")
        return
    except MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{name}'. Уточните ФИО")
        return

def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    if not schoolkid: 
        return
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    count = bad_marks.count()
    bad_marks.update(points=5)
    print(f"{count} плохих оценок исправлено на пятёрки.")


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    if not schoolkid: 
        return
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    count = chastisements.count()
    chastisements.delete()
    print(f"Удалено {count} замечаний")


def create_commendation(schoolkid_name, subject):
    schoolkid = get_schoolkid(schoolkid_name)
    if not schoolkid:  
        return
    lesson = Lesson.objects.filter(
        subject__title=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    ).order_by('-date').first()

    if not lesson:
        print("Уроки по такому предмету не найдены.")
        return

    Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
        )
    print(f"Похвала для {schoolkid} по предмету {subject} добавлена.")
