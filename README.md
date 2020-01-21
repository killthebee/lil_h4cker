# Хакни школу

Это как читы для гта только для улучшения вашей успеваемости.

## Запуск

- Ожидается что у вас уже скачан сайт и база данных школы
- Разместите scripts.py в директории с manage.py
- Войдите в shell командной  ```python3 manage.py shell```
- Запустите нужный скрипт как написано ниже

## Описание и запуск скриптов

Находясь в shell скопируйте нужный скрипт из scripts.py или импортируйте командой:

```from scripts import example_script```

Где example_script это название нужной функции(скрипта)

Затем присвойте переменной schoolkid_name имя ученика, для
которого собираетесь применять скрипт командой:
```schoolkid_name='Имя'```

Если ученика с таким именем не существует или было найдено более одного
ученика с заданным именем, то об этом будет сообщено соответствующими ошибками.

Затем запустите один из следующий скриптов:
### Fix marks
Заменяет у целевого ученика двойки и тройки на пятерки.
Для запуска введите следующую команду:
```fix_marks(schoolkid_name)```

### Remove chastisements
Удаляет все замечания у целевого ученика.
Для запуска введите следующую команду:
```remove_chastisements(schoolkid_name)```

### Create commendation
Создаёт похвалу для целевого ученика по выбранному предмету.

Перед запуском скрипта необходимо присвоить переменной subject строковое значение
названия урока, например:
```subject='Музыка'```

Если предмета с таким названием не существует или было найдено более одного
предмета с заданным названием, то об этом будет сообщено соответствующими ошибками.

Для запуска введите следующую команду:
```create_commendation(schoolkid_name, subject)```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
