cd..
cd venv\scripts
call activate
cd../..
cd sourcecode
pip install -r requirements.txt
set MAIL_USERNAME=youremail@gmail.com
set MAIL_PASSWORD=YourPassword
set BLAH_ADMIN=youremail@gmail.com
set FLASK_APP=blah.py
set FLASK_ENV=development
python -m flask run --host=0.0.0.0 --port 9110
