1. Tweets
    -> User Permissions
        -> Creating
            -> Text
            -> Image -> Media Storage Server
        -> Delete
        -> Retweeting
            -> Read only serializer
            -> Create only serializer
        -> Liking or Unliking

2. Users
    -> Register
    -> Login
    -> Logout
    -> Profile
        -> Image?
        -> Text?
        -> Follow Button
    -> Feed
        -> User's feed only?
        -> User + who they follow?

3. Following / Followers


Next Steps:
- Large File Uploads for Images ~ Dive into AWS
- Notifications
- Direct Messages / Private Inboxes ~ Chat x Channels
- Explore -> parse & filter for hashtags



### Command

- create app
`./manage.py startapp app-name` to start your app, in our case, it's tweets folder 

- model migration
`/manage.py makemigrations `
```shell
Migrations for 'tweets':
  tweets/migrations/0001_initial.py
    - Create model Tweet
```
- execute migration
`python manage.py migrate`

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tweets
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  Applying tweets.0001_initial... OK
```


- create and store data 

` ./manage.py shell`  

```python
Python 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tweets.models import Tweet
>>> obj = Tweet()
>>> obj.content= "hello world"
>>> obj.save()
>>> exit()
(venv)  elfi.yang@trussle.com@ip-192-168-43-77  ~/Documents/Tweetme-Django-React/tweetme   master ●  ./manage.py shell
Python 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tweets.models import Tweet
>>> obj = Tweet.objects.get(id=1)
>>> obj.content
'hello world'
>>> obj2 = Tweet.objects.create(content="Hello there")
>>> exit()
```

- create superuser
`python manage.py createsuperuser`
```   
Username (leave blank to use 'elfi.yang@trussle.com'): elfi
Email address: 
Password: 
Password (again):  (!23)
Superuser created successfully.
```
```python
 ./manage.py makemigrations
You are trying to add a non-nullable field 'user' to tweet without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 1
Migrations for 'tweets':
  tweets/migrations/0003_tweet_user.py
    - Add field user to tweet
```

To edit user in django : http://127.0.0.1:8000/admin/

