# import the library
import googlemaps
import pprint
import time
import pandas as pd

# Define the API Key.
API_KEY = 'Your_API_Key_Goes_Here'

# Define the Client
gmaps = googlemaps.Client(key=API_KEY)

lati = float(input("Enter Lat:"))
lngi = float(input("Enter Lng:"))


coord = "{0},{1}".format(lati,lngi)
rad = int(input("Enter radius of surrounding[in mts]:"))
typ = input("Enter type of place:")

params = {
    'location': coord,
    'radius': rad,
    'open_now': False,
    'type': typ
}

stored_results = []
# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters
def extract_places():
    for place in places_result['results']:
        time.sleep(1)
        # define the place id, needed to get place details. Formatted as a string.
        my_place_id = place['place_id']

        # define the fields you would liked return. Formatted as a list.
        my_fields = ['name', 'formatted_phone_number', 'formatted_address', 'geometry/location', 'type']

        # make a request for the details.
        places_details = gmaps.place(place_id=my_place_id, fields=my_fields)
        pprint.pprint(places_details)
        name = places_details['result']['name']
        formatted_address = places_details['result']['formatted_address']
        latlng = places_details['result']['geometry']['location']
        place_type = places_details['result']['types']
        placeList = [name, formatted_address, latlng['lat'], latlng['lng'], place_type]
        stored_results.append(placeList)
    return stored_results

places_result = gmaps.places_nearby(**params)
if 'next_page_token' in places_result:
    while 'next_page_token' in places_result:
        places_result = gmaps.places_nearby(**params)
        new_stored_results = extract_places()
        if 'next_page_token' in places_result:
            params['page_token'] = places_result['next_page_token']
        else:
            break
else:
    places_result = gmaps.places_nearby(**params)
    new_stored_results = extract_places()

# -------------- DUMPING VALUES IN EXCEL -----------------------
print("Dumping Values in Excel...")
# define the headers, that is just the key of each result dictionary.
# row_headers = stored_results[0].keys()
# create a new workbook and a new worksheet.
a = pd.DataFrame(new_stored_results, columns=['Name', 'Address', 'Latitude', 'Longitude', 'Type'])

writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
a.to_excel(writer, sheet_name='Address Details', index=False)
writer.save()
