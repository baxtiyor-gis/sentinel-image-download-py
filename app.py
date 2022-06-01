from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from dotenv import load_dotenv
import pprint
import os

load_dotenv()

# https://scihub.copernicus.eu/dhus user's login and password

login = os.getenv('login')
password = os.getenv('password')
url = os.getenv('url')

api = SentinelAPI(login, password, url, show_progressbars=True)

# Selected area file
area_geojson = os.path.join(os.path.dirname(__file__), 'input/simple_area.geojson')

footprint = geojson_to_wkt(read_geojson(area_geojson))

products = api.query(footprint,
                     platformname='Sentinel-2',
                     producttype='S2MSI2A',
                     date=('NOW-10DAYS', 'NOW'),
                     cloudcoverpercentage=(0, 20))

# Convert results to a geoJSON format
res = api.to_geojson(products)['features']

# pprint.pprint(res)

for i in res:
    title = i['properties']['title']
    summary = i['properties']['summary']
    cloudcoverpercentage = i['properties']['cloudcoverpercentage']
    orbitnumber = i['properties']['orbitnumber']
    producttype = i['properties']['producttype']
    processinglevel = i['properties']['processinglevel']
    platformserialidentifier = i['properties']['platformserialidentifier']
    processinglevel = i['properties']['processinglevel']
    producttype = i['properties']['producttype']

    result = {
        'title': title,
        'summary': summary,
        'cloudcoverpercentage': cloudcoverpercentage,
        'orbitnumber': orbitnumber,
        'producttype': producttype,
        'processinglevel': processinglevel,
        'platformserialidentifier': platformserialidentifier,
        'processinglevel': processinglevel,
    }

    pprint.pprint(result)
print("Number of results: %d" % len(res))

# Download all the products
# api.download_all(products)
