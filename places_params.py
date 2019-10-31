# import the library
import googlemaps
import pprint

# Define the API Key.
API_KEY = 'Your_API_Key_Goes_Here'

# Define the Clientgeocode_result
gmaps = googlemaps.Client(key=API_KEY)

geocode_result = gmaps.geocode(input("Enter place name:"))
pprint.pprint(geocode_result)

lat = geocode_result[0]["geometry"]["location"]["lat"]
lng = geocode_result[0]["geometry"]["location"]["lng"]

for details in geocode_result[0]["address_components"]:
    if details['types'] == ['postal_code']:
        print("Pin Code:" + details['long_name'])

coord = "\"{0},{1}\"".format(lat,lng)
print(coord)




