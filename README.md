Simple RESTful API service for managing a product list, allowing users to add, edit, delete, and view products.<br/>
Key functionalities include unique product identification, category-based filtering, and pagination for product browsing

To run project:
````
git clone https://github.com/P-Ziolkowski/RESTful-API.git

cd RESTful-API/product_api/

python3 -m venv api_venv

source api_venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
````
