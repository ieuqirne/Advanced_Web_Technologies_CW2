cd..
cd venv\scripts
call activate
cd../..
cd sourcecode
pip install -r requirements.txt
set FLASK_APP=flasky.py
set FLASK_ENV=development
python -m flask run --host=0.0.0.0 --port 9110
