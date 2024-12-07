To setup the environment:
    1) make a virtual environment in the projects directory
        python3 -m venv venv
    2)activate  the venv     
        source venv/bin/activate to activate my virtual environment
    3)install reqiurements.txt
        pip install -r requirements.txt
    4)if you add a new package don't forget to add it in the requirements.txt 
      by running this command in the projects directory
        pip freeze > requirements.txt

for the scrapping file to run you should make a file in the main directory called .env to define the main directory in your system. This file is not uploaded on github.
    PROJECT_DIR=/path/to/main/directory/
    

to run the newsguessr_app run
    ./manage.py runserver
    
if access is denied run 
    chmod +x manage.py  