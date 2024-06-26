import folium
import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, geocoder

# Take input phone number along with the country code
number = input("Enter the PhoneNumber with the country code : ")

# Parse the phone number string to convert it into phone number format
phoneNumber = phonenumbers.parse(number)

# Store the API Key in the Key variable
Key = "Enter your Api"  # https://opencagedata.com/api

# Using the geocoder module of phonenumbers to print the Location
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("Location : " + yourLocation)

# Using the carrier module of phonenumbers to print the service provider name
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("service provider : " + yourServiceProvider)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Getting the map for the given latitude and longitude
myMap = folium.Map(location=[lat, lng], zoom_start=9)

# Adding a Marker on the map to show the location name
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# Save map to html file to open it and see the actual location in map format
myMap.save("Location.html")