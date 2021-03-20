From command prompt

Create a virtual environment:
virtuanenv venv

Activate virtual environment:
source venv/bin/activate

Install requirements:
pip install -r requirements.txt

Run command:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 

Admin is alreacdy created when project is running go to 127.0.0.1:8000/admin
Credentials:
Username : admin
Password : zsexdr321


For changing Background Image:
    you can change the background image by placing image in "static" folder in the project, rename your background image with this "main-bg.jpg" if you rename your image before placing in static folder than you dont have to change anything in code.

    same process for logo changing.

    make sure you are replacing the old images filels with the new one. (delete main-bg.jpg and logo.jpg and then place new images with same name)

For changing text:
    open folder SEO(base directory) -> core -> templates -> index.html

    you can see text written in HTML file (index.html) and change the text according to your needs.
