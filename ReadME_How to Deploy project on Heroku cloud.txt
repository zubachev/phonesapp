0. GitHub ��� �� �����. ����� ������������ HerokuGit
1. ������� � Heroku ������� ������
2. ������� � https://dashboard.heroku.com/apps, ������� ����� ���������� (new app)
3. ����� app-name (��������, phonesappmy), ������, ����� create pipeline, ��� pipeline, �������� �������.
4. ������� � ���� ����������, �������� ������ deploy, ����� Deploy using Heroku Git
5. ����� ������� ������������ Install the Heroku CLI. ��!!! ����� ���� �� ������ ������� ��������� ������ � ������� ���� ��������:
	�) ����� � ����� �������� ������ ����������� ��������� ��������� �����: Procfile, Pipfile � Pipfile.lock. ������� ���� Procfile (��� ����������) ����� ���� web: gunicorn app:app. ���� ���� ������ ��������� ������ ��� ������� ������ ���������� �� ���-������� gunicorn. ������� ����� ��� ���� ��������� app.py � � ��� ��� ������ app � �������� ����� ����� (@app.route � app.run())
	�) ����� �� ����� ������� Pipfile � Pipfile.lock. ����� ��� ������� ��� ����� ������� � ����� ���� requirements.txt � �������� ���� �������� ������, ����������� ��� ������������� (��� ������� ��� :
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
	). ������ ������� ����� ����������. �� ����� �������� �������� ������� � ��������� ������ pip freeze > requirements_.txt. ��� �� ����� ������ ��� ������, ���������, � ������ ����� ��������. ����� ���� ��� ���� requirements.txt ������, ��������� ��������� ������ Anaconda Prompt �� ����� ��������������, ��������� � heroku (heroku login), ��������� �� ������ ������ ������� ( cd phonesappmy ) � ����� pipenv install gunicorn. (pipenv � heroku cli ������ ���� �������������� �����������). ����� ���������� ���������� �������� ������ �������������� 2 ����� Pipfile.
8. ��������� �� ������� ������� 
	- git init
	- git add .
	- git commit -am "make it better"
	- git push heroku master
9. ������� https://phonesappmy.herokuapp.com, ��������� ��� �� ��������. ���� �� ��������, ������� ���� (� ������� heroku logs --tail) � ���������� ������.