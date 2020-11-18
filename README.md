# Description

A simple CRUD service for a note manager. You can create and modify Notes that have the following attributes:

- Title

- Text

## Run (Dev mode)

```bash
cd backend

python manage.py migrate notes_manager  

python manage.py runserver
```

## Try it out

```bash

curl -X POST -H "Content-Type: application/json" -d '{"title": "The worst error a person can make", "text": "Dont fool your-self. And remember, you are the easiest person to fool. (Richard Feynman)"}' 'http://localhost:8000/api/notes/'

curl -X GET 'http://localhost:8000/api/notes/'
```