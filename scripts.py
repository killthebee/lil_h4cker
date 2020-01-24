def fix_marks(schoolkid_name):
    from datacenter.models import Schoolkid, Mark
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid_name):
    from datacenter.models import Schoolkid, Chastisement
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid_name, subject):
    from datacenter.models import Schoolkid, Lesson, Subject, Commendation

    import random as r
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
    ]

    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    targeted_subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
    lessons = Lesson.objects.filter(group_letter=schoolkid.group_letter, subject=targeted_subject)
    last_lesson = lessons.last()
    Commendation.objects.create(
        text=r.choice(commendations),
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )
