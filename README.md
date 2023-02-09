# Django + Stripe

<div align=center>
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" width=100/>
</div>
🤖 Django + Stripe API бэкэнд приложение.
Реализован API с двумя методами GET, которые принимают id товара для последующего добавления его в checkout session.

# Настройка проекта перед запуском

Создаём и активируем виртуальное окружение
<br><b>Windows:</b>
```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```

<b>Mac/Linux:</b>
```bash
python3 -m virtual-env -p python3 venv
```
```bash
source venv/bin/activate
```

Устанавливаем все зависимости из файла <code>requirements.txt</code> комадой:
```bash
pip install -r requirements.txt
```

Для того, чтобы проект корректно работал, необходимо создать файл <code>.env</code><br>
В данном файле будут храниться вся засекреченная информация, а именно stripe ключи и django secret key. <br>
Образец заполнения файла <code>.env</code> находится в файле <code>.env_template</code><br>

Теперь мы можем переходить непосредственно к запуску проекта через Docker.

# Запуск через Docker

Реализована возможность запуска приложения через Docker image <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" width=30/>.<br>
Для него был написал Dockerfile.<br>

Для запуска необходимо выполнить команду:
```bash
docker build -t shop .
```
Данной командой мы создадим новый docker image

Теперь мы можем запустить приложение командой:
```bash
docker run shop
```

---
Если по какой-то причине возникли сложности при использовании Dockerfile, можно воспользоваться ручным запуском. <br>

# Ручной запуск приложения

Если вы ещё по какой-то причине не создали файл <code>.env</code> и не установили все зависимости, вам необходимо вернуться к первому шагу.

Необходимо применить все созданные раннее миграции командой:
```bash
python manage.py migrate
```

После успешного применения миграций, можно запускать приложение командой:
```bash
python manage.py runserver
```

---
# Работа с приложением

В приложении реализовано два роута:

* http://127.0.0.1:8000/item/{pk}
Данный url адрес приведёт нас на страницу просмотра детальной информации о товаре с идентификатором <code>{pk}</code>.
На данной странице будет находиться кнопка Buy, по нажатию на которой сработает <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" width=25/> скрипт, <br>
который получит <b>session checkout id</b> данного товара и перенаправит пользователя на страницу оплаты.
* http://127.0.0.1:8000/buy/{pk}
Данный url адрес отправит GET запрос на получение session checkout id конкретного товара с идентификатором <code>{pk}</code><br>
Пользователю будет доступен ответ в виде json строки с идентификатором сессии.

---

Была написана документация к каждому View, Model, функциям.<br>
Был создан файл с дампом базы данных, для его установки необходимо выполнить команду:
```bash
python manage.py loaddata shop_app/fixtures/db.json
```

Для входа в админ панель воспользуйтесь логином <code>admin</code> и паролем <code>admin</code> <br>
В админ панеле есть возможность просмотра модели Item и добавления новых.
