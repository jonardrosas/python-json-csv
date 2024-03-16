# python-json-csv


Installation:

    $ python -m venv env  
    $ source env/bin/activate

Usage:
  
    $python main <source> <format> --key=
    
source(required) = API endpoint or URL link. Typically sourced from a REST API or a .json file.

format(required) = Desired output format.

key(optional) = If the data is stored within a particular key.


 Example:
 
    $python main.py https://api.slingacademy.com/v1/sample-data/products?limit=100 csv --key=products
