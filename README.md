# django_rooms

## Da aggiungere per finire
```
Login with Social
Privacy Policy Page
About page
Site Maps
Google Analytics
Meta Tag
```

# How Install
## clonare la parte git
```
git clone https://github.com/fcorallini/django_rooms.git
```
## installare i pacchetti apt elencati nel file apt-requirements.txt
```
sudo apt-get install nomepacchetto
```
## creare virtualenv e installare pacchetti Python3 
```
virtualenv -p python3 virtualenv; source virtualenv/bin/activate
pip install -r ~/workingcopy/django_rooms/main/requirements.txt
cd ~/workingcopy/django_rooms/main
```
## struttura progetto
```
.
├── main //parte django
├── site //frontend nuxt
└── virtualenv
```
## creazione database e utente admin Django
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
# Server nuxt.js
## install dependencies
```
npm install
```
## serve with hot reload at localhost:3000
```
npm run dev
```