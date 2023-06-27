from phonenumbers import parse, geocoder, carrier
import opencage
import folium
from myphone import number
from opencage.geocoder import OpenCageGeocode

def precise_locator(address_info):
    """
    A precise locator function that takes an address dictionary with keys for address, city, state, and zip code as input,
    and returns the precise location information.
    """

    # Perform geocoding or API call to get precise location information based on the input
    # address, city, state, and zip code.
    precise_location = None  # Placeholder for precise location information

    # Add code to retrieve precise location information using a geocoding service or API,
    # such as Google Maps API, OpenStreetMap, or a similar service.

    # Example implementation using a hypothetical geocoding service:
    # precise_location = geocoding_service.get_location(address_info["address"], address_info["city"], address_info["state"], address_info["zip_code"])

    if precise_location is not None:
        # Extract relevant information from the precise location data
        latitude = precise_location["latitude"]
        longitude = precise_location["longitude"]
        country = precise_location["country"]
        county = precise_location["county"]
        city = precise_location["city"]
        state = precise_location["state"]
        zip_code = precise_location["zip_code"]

        # Print the precise location information
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Country: {country}")
        print(f"County: {county}")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Zip Code: {zip_code}")

        # Alternatively, you can return the precise location information as a dictionary,
        # JSON, or a custom data structure, depending on your requirements.
        # return precise_location
    else:
        print("Unable to retrieve precise location information. Please check your input.")

# Parse phone number
pepnumber = parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Get carrier information
service_pro = carrier.name_for_number(pepnumber, "en")
print(service_pro)

# Perform geocoding using OpenCageData
key = "265aa9593d374a949332585ce13ef865"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

# Extract latitude and longitude from results
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Create folium map
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

# Save map to HTML
myMap.save("mylocation.html")