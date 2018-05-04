0. GitHub нам не нужен. Можно пользоваться HerokuGit
1. Создаем в Heroku учетную запись
2. Заходим в https://dashboard.heroku.com/apps, создаем новое приложение (new app)
3. Пишем app-name (например, phonesappmy), регион, далее create pipeline, имя pipeline, нажимаем создать.
4. Заходим в наше приложение, выбираем раздел deploy, далее Deploy using Heroku Git
5. Далее следуем инструкцияем Install the Heroku CLI. НО!!! Перед этим мы должны создать несколько файлов и сделать пару операций:
	а) Папка с нашим проектом должна обязательно содержать следующие файлы: Procfile, Pipfile и Pipfile.lock. Создаем файл Procfile (без расширения) пишем туда web: gunicorn app:app. Этот файл служит отправной точкой для запуска нашего приложения на веб-сервере gunicorn. Главное чтобы наш файл назывался app.py и в нем был объект app в качестве точки входа (@app.route и app.run())
	б) Далее на нужно создать Pipfile и Pipfile.lock. Чтобы это сделать нам нужно создать в корне файл requirements.txt и добавить туда основные пакеты, необходимые для развертывания (как правило это :
		click==6.7
		Flask==0.12.2
		Flask-SQLAlchemy==2.3.2
		gunicorn==19.7.1
		itsdangerous==0.24
		Jinja2==2.10
		MarkupSafe==1.0
		psycopg2==2.7.4
		scikit-learn==0.19.1
		SQLAlchemy==1.2.5
		Werkzeug==0.14.1
		numpy==1.14.0
		scipy==1.0.0
	). Версии пакетов будут отличаться. Их можно получить выполнив команду в командной строке pip freeze > requirements_.txt. Нам не нужны оттуда все пакеты, повторюсь, а только самые основные. После того как файл requirements.txt создан, запускаем командную строку Anaconda Prompt от имени администратора, логинимся к heroku (heroku login), указываем на корень нашего проекта ( cd phonesappmy ) и пишем pipenv install gunicorn. (pipenv и heroku cli должны быть предварительно установлены). После достаточно длительной операции должны сформироваться 2 файла Pipfile.
8. Выполняем по порядку команды 
	- git init
	- git add .
	- git commit -am "make it better"
	- git push heroku master
9. Заходим https://phonesappmy.herokuapp.com, проверяем все ли работает. Если не работает, смотрим логи (с помощью heroku logs --tail) и исправляем ошибки.