cd ..
cd venv
cd Scripts
source activate
cd ..
cd ..
cd SourceCode
pip install -r requirements.txt
export MAIL_USERNAME=youremail@gmail.com
export MAIL_PASSWORD=YourPassword
export BLAH_ADMIN=youremail@gmail.com
export FLASK_APP=blah.py
export FLASK_ENV=development
python -m flask run --host=0.0.0.0 --port 9110
