# Rest Country
Installation
`pip install -r requirements.txt`

run the test server `python manage.py runserver`
access the admin site `http://127.0.0.1/8000/admin` and add the `Continent` first and then the `Country`

## Usage
#### Localhost
Go to `http://127.0.0.1/8000/api/country/` to list all the countries

filter example
`http://127.0.0.1/8000/api/country/?continent__name=<continent>` to list all countries in a given continent

`http://127.0.0.1/8000/api/country/?common__name=<country>`  to show the country with the particular name "country"

NOTE: all query must be Title format.
