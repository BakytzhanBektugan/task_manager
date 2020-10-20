## Simple Task manager app

Приложение позволяет пользователям зарегистрироваться в системе и создавать 
собственный список задач. Единственным интерфейсом взаимодействия является 
API реализованный с помощью Django Rest Framework.

В качестве СУБД использовался PostgreSQL. Приложение протестировано модульными тестами. 

Для регистрации и авторизации использовался [djoser](https://github.com/sunscrapers/djoser).
Авторизация осуществляется с помощью токенов. Методы регистрации и авторизации 
описаны в соответствующем разделе [документации](https://djoser.readthedocs.io/en/latest/sample_usage.html).

Приложение состоит из двух моделей: Task и TaskHistory наследующие абстрактную модель AbstractTask. В TaskHistory сохраняется история изменения задачи.

#### Основные методы взаимодействия

Получение, изменение и удаление задачи с соответствующими методами(GET, PUT, PATCH, DELETE) по адресу:
```
http://127.0.0.1:8000/api/tasks/task_id/
```

Создание задачи, получение списка задач(POST, GET):
```
http://127.0.0.1:8000/api/tasks/
```

Получение истории изменения задачи(GET):
```
http://127.0.0.1:8000/api/tasks/task_id/history/
```

#### Фильтрация списка задач

Фильтрация возможна по статусу и по планируемой дате завершения задачи. Пример
 запроса фильтрации приведён ниже. Фильтр - **completion_date** выведет все задачи с соответствующей датой завершения,
 **completion_date_from** и **completion_date_to** позволяют указать промежкуток времени.
```
http://127.0.0.1:8000/api/tasks?status=I&completion_date=2022-12-12
```
Запрос выведет все задачи с заданным статусом и датой завершения до указанной даты.
Типы возможных статусов: **('N', 'New'), ('P', 'Planned'), ('I', 'In progress'), ('C', 'Completed')**.

Все необходимые пакеты приведены в [requirements.txt](https://github.com/BakytzhanBektugan/task_manager/blob/master/requirements.txt).


Поработали в ветке