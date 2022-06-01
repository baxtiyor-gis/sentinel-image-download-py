# Simple download satellite image from https://scihub.copernicus.eu with Python


Read offical [Documentation](https://sentinelsat.readthedocs.io/)

## Install
-------

Clone repository:

    $ git clone https://github.com/baxtiyor-gis/sentinel-image-download-py

Create virtual environment

    $ python -m venv env

Activate virtual environment (cmd)
    
    $ env\Scripts\activate 



Activate virtual environment (bash)
    
    $ source env/Scripts/activate 


Rename .env_example to .env and set login and password from https://scihub.copernicus.eu


    login = "simple_login"
    password = "simple_password"
    url = "https://scihub.copernicus.eu/dhus"
    
Install packages
    
    $ pip install -r requirements.txt

Run python file
    
    $ python app.py









