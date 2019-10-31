# google-maps-api
Python script to extract nearby places and load excel sheet.

maps_places.py:
The original file was written by @areed1192, for detailed projects on google-maps-api @areed1192 did a great job in his repository.

maps_nxt_page_token.py: 
This file contains code which includes looping of nextpage token to pages until we get 60 results. This code uses places api.

places_params.py:
This file contains code to parse out the required details of the given place(Say name, phone number, Latitude, longitude, postal code etc.). This code uses geocode api.
