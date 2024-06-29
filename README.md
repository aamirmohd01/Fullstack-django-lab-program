1. **lab3** contains both lab 3 program and lab4 program i.e. Current_date_time, four_hours_ahead and four_hours_before
2. **lab5** => list of fruits and students (unordered and ordered)
3. **lab6** => home page, layout, contactus
4. **lab7** => student registration
5. **lab8** => AdminInterface to add or change student details



# For lab7 program follow these steps
- Install XAMPP 
- Go to settings.py and change the DATABASE default setting to :- >
     ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'students',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT':'3306',
    }}
    ```
     
- open XAMPP server
- click on new and create a database using the same name as you provided in NAME in settings.py default
- go to your VS Code virtual environment and follow these:>
-  ```pip install mysqlclient```
-  ```python manage.py makemigrations```
-  ```python manage.py migrate```
-  after successfully migrating go to your xampp / phpmyadmin and in your database look for **course** and **student** table
-  click on them one by one and **insert** data into those tables and click on **GO**
-  after adding the data into both the tables come back to VSCODE virtual environment and run server:
-  ```python manage.py runserver```
-  write *reg/*  in url path
-  select name and course and click on Enroll


# For lab8 program follow these steps
- make changes in your settings.py as mentioned in the previous lab7 program
- you can make a new database or you can use the previous also
- in VS code virtual environment follow these steps:
-  ```python manage.py makemigrations```
-  ```python manage.py migrate```
-  ```python manage.py createsuperuser```
-  after executing the above command you will have to write **your username** , **email**, and **password** (NOTE: Password will be invisible. so, dont'worry just enter password) and again re-enter the password.
-  ```python manage.py runserver```
-  check the output by writing *secretadmin* in the URL path
-  Enter your username and password (as you created after running createsuperuser)
-  login and **add** or **change** the table data

