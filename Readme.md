# Example Python Digital Flask 

 Simple example python flask crud app for sqlite.
 
### Ref
* [BluePrint Sample 1](https://realpython.com/flask-blueprint/)
* [BluePrint Sample 2](https://www.freecodecamp.org/news/how-to-use-blueprints-to-organize-flask-apps/)
* [Large project sample](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy)
* [sample ](https://github.com/rickyyangrui/Flask_Movie_Site)
### Installing (for linux)

```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
flask db init
```
```   
flask db migrate -m "entries table"
or
flask db migrate 
```
```
flask db upgrade
```
```
flask run
```

