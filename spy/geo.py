import argparse
import requests
import googlemaps

# Replace with your API keys
OPENCAGE_API_KEY = ''
GOOGLE_MAPS_API_KEY = ''  # Set to an empty string if not provided
HERE_API_KEY = ''

def get_location_info(query):
    try:
        
        opencage_url = f'https://api.opencagedata.com/geocode/v1/json?q={query}&key={OPENCAGE_API_KEY}'
        opencage_response = requests.get(opencage_url)
        opencage_response.raise_for_status()

        opencage_data = opencage_response.json()
        if 'results' in opencage_data and opencage_data['results']:
            result = opencage_data['results'][0]
            print("S1 Location Database:")
            print("Formatted Address:", result.get('formatted', 'N/A'))
            components = result.get('components', {})
            print("Components:")
            for key, value in components.items():
                print(f"{key}: {value}")
        else:
            print("Location not found using S1")

        
        if GOOGLE_MAPS_API_KEY:
            gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
            google_maps_result = gmaps.geocode(query)
            
            if google_maps_result:
                print("\nS2 Location Database:")
                print("Formatted Address:", google_maps_result[0].get('formatted_address', 'N/A'))
                geometry = google_maps_result[0].get('geometry', {})
                location = geometry.get('location', {})
                print(f"Latitude: {location.get('lat', 'N/A')}")
                print(f"Longitude: {location.get('lng', 'N/A')}")
            else:
                print("Location not found using S2 or API key not provided.")

        
        here_url = f'https://geocode.search.hereapi.com/v1/geocode?q={query}&apiKey={HERE_API_KEY}'
        here_response = requests.get(here_url)
        here_response.raise_for_status()

        here_data = here_response.json()
        if 'items' in here_data and here_data['items']:
            item = here_data['items'][0]
            print("\nS3 Location Database")
            print("Title:", item.get('title', 'N/A'))
            address = item.get('address', {})
            print("Address:")
            for key, value in address.items():
                print(f"{key}: {value}")
        else:
            print("Location not found using S3")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get location information using multiple Geocoding APIs")
    parser.add_argument("-a", "--area", help="Area name or pincode", required=False)
    args = parser.parse_args()

    if args.area:
        get_location_info(args.area)
    else:
        query = input("Enter an area name or pincode: ")
        get_location_info(query)
