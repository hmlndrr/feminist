chmod 400 shefiles
chmod 400 templates
chmod 400 .gitignore
chmod 400 requirements.txt
chmod 400 feminist.py
chmod 500 run.sh
gunicorn -b :80 feminist:app