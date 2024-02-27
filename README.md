# PageRankProject
Implementing a demo search engine that works using the page rank algorithm and tf-idf algorithm

# Configuration
## Set up and enter a virtual environment
```
git clone https://github.com/theunixdisaster/PageRankProject.git
cd PageRankProject
python3 -m venv env
source env/bin/activate
```
## Installing required packages
When you are at the root directory of your repo(`PageRankProject`) there will be a `requirements.txt` file with all the requirements.
Install it simply by:
```
pip install -r requirements.txt
```

## Updating the database and creating a superuser

### If you are facing issues with database or if the `migrations` directories contains files other than __init__.py before initial migration
(If you do not have any `db.sqlite3` files lying around or if the `migrations` directory don't have anything other than `__init__.py`
ignore this step and go to [applying the migrations](https://github.com/theunixdisaster/PageRankProject/blob/main/README.md#applying-the-migrations))  
Go to the `migrations` directory inside `internet/sites` and delete everything except for `__init__.py`  
Now remove `db.sqlite3` if present in the `internet` folder inside the root directory using `rm -rf db.sqlite3`  
  
Similary go to the `migrations` directory inside `pgrankserver/server` and delete everything except for `__init__.py`  
Now remove `db.sqlite3` if present in the `pgrankserver` folder inside the root directory using `rm -rf db.sqlite3`  
  
### Applying the migrations
Now move back to the root directory of the repo(`PageRankProject`) and run:
```
python3 internet/manage.py makemigrations
python3 internet/manage.py migrate
python3 internet/manage.py createsuperuser #and set a superuser

python3 pgrankserver/manage.py makemigrations
python3 pgrankserver/manage.py migrate
python3 pgrankserver/manage.py createsuperuser
```

## Starting the two servers
Open up two terminals with the virtualenv activated one in the `internet` directory and the other in `pgrankserver` directory  
In the one opened inside `internet` start the server at port `8000`
```
python3 manage.py runserver 8000
```
And in the one opened inside `pgrankserver` start the server at port `8001`
```
python3 manage.py runserver 8001
```

## Adding the websites to the repertoire
In the browser open up `127.0.0.1:8000/scrape` (Open up the corresponding url if the `internet` server was started on another `ip` or `port`)  
Click on the button on the top left corner and this will find the websites present in the internet.  
  
Now open up `127.0.0.1:8001/update` and press the `Update` button.  
  
After all of this you can simply open up `127.0.0.1:8001` and use the search engine.  
  
  
![Screenshot from 2023-01-22 17-16-13](https://user-images.githubusercontent.com/49746983/213914143-53319d8f-7c86-4b79-a0e3-294581ea3148.png)

![Screenshot from 2023-01-22 17-16-37](https://user-images.githubusercontent.com/49746983/213914187-9c67bf12-7e0b-4dfe-b3ef-f3266db0be7f.png)


# Pending work
__________________

Add a 'Did you mean' feature using Keras
