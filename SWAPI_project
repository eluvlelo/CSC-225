import requests
import json
import os
import math

data_dir = "api_data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

def get_swapi_resource(resource_type, resource_id=None, search_query=None, page=None):
    """
    Function to get data from SWAPI
    resource_type: people, planets, starships, etc.
    resource_id: optional specific ID to retrieve
    search_query: optional search parameter
    page: optional search parameter
    """
    base_url = "https://swapi.dev/api"
    
    if resource_id:
        url = f"{base_url}/{resource_type}/{resource_id}"
    elif search_query:
        url = f"{base_url}/{resource_type}/?search={search_query}"
        if page:
            url += f"&page={page}"
    else:
        url = f"{base_url}/{resource_type}/"
        
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
            
def search_character(search_term):
    """
    Function to search character names.
    search_term: any name of character(s) of any length
    """
    try:
        characters = get_swapi_resource("people",  search_query=search_term)

        if characters and characters['count'] == 1:
            print(f"\nOne Character Found:")
            print(characters['results'][0]['name'])

        elif characters and characters['count'] > 1:
            if characters['count'] % 10 == 0:
                pages = characters['count']//10 # return number of pages of results. Each page has a max of 10 planets
            else:
                pages = int(math.trunc(characters['count']/10) + 1)
            print(f"\nFound {characters['count']} character(s):")
            for i in range(1, pages+1): # loops through all pages of search_term and returns results
                current_page = get_swapi_resource("people", search_query=search_term, page=i)
                
                number = 1 + (i - 1) * 10 # determines the starting number based on page number
                for i, person in enumerate(current_page['results'], start=number):
                    print(f"{i}. {person['name']}") # print every character found
        
        else:
            print(f"\nNo Characters Found.")

    except Exception as e:
        print(f"An unexpected error occurred {e}")

def character_info(char_id):
    """
    Function to display and save relevant character information.
    char_id: resource_id of a unique character
    """
    try:
        char_results = get_swapi_resource("people", char_id)
        
        if char_results:
            character_data = {
                "name": char_results['name'],
                "height": char_results['height'],
                "mass": char_results['mass'],
                "hair_color": char_results['hair_color'],
                "skin_color": char_results['skin_color'],
                "eye_color": char_results['eye_color'],
                "birth_year": char_results['birth_year'],
                "gender": char_results['gender'],
                
                "films": [],
                "species": [],
                "vehicles": [],
                "starships": [],
                "url": char_results['url']
            }

            homeworld_url = char_results['homeworld']
            homeworld_id = homeworld_url.split('/')[-2] # returns id of homeworld
            homeworld = get_swapi_resource("planets", homeworld_id)
                
            if homeworld:
                character_data['homeworld'] = homeworld['name'] # creates a new key and assigns homeworld name

            films_url = char_results['films']
            films = [] # list after converting url to film title

            if films_url:
                for film_url in films_url:
                    film_id = film_url.split('/')[-2] # returns id of film
                    film = get_swapi_resource("films", film_id)
                    if film:
                        films.append(film['title']) # append film title to films list

                character_data['films'].extend(films) # append 1 or more films titles
                
            species_url = char_results['species']
            species_list = [] # list after converting url to species name

            if species_url:
                for url in species_url:
                    species_id = url.split('/')[-2] # return id of species
                    species = get_swapi_resource("species", species_id)
                    if species:
                        species_list.append(species['name']) # append species names to list

                character_data['species'].extend(species_list) # append 1 or more species names

            # Display Data
            print(f"\nInfo about {character_data['name']}:")
            print(f"Height: {character_data['height']} cm")
            print(f"Mass: {character_data['mass']} kg")
            print(f"Hair color: {character_data['hair_color'].replace('"','')}") # removes quotes. multiple colors possible
            print(f"Skin color: {character_data['skin_color'].replace('"','')}") 
            print(f"Eye color: {character_data['eye_color'].replace('"','')}") # removes quotes. multiple colors possible
            print(f"Birth year: {character_data['birth_year']}")
            print(f"Gender: {character_data['gender']}")
            print(f"Homeworld: {character_data['homeworld']}")
            print(f"Films: {str(character_data['films'])[1:-1].replace("'","")}") # converts list to string and removes brackets and quotes
            print(f"Species: {str(character_data['species'])[1:-1].replace("'","")}")
            print(f"Vehicles: {str(character_data['vehicles'])[1:-1].replace("'","")}")
            print(f"Starships: {str(character_data['starships'])[1:-1].replace("'","")}") # converts list to string and removes brackets and quotes

            # Save character data to file.
            character = "_".join(char_results['name'].split())
            filename = os.path.join(data_dir, f"{character}.json")
            with open(filename, 'w') as file:
                json.dump(character_data, file, indent=4)

            print(f"\nCharacter data saved to {filename}.") 

        else:
            print("Character not Found.")
    
    except Exception as e:
        print(f"An unexpected error occurred {e}")
    
def compare_characters(char1, char2):
    """
    Function to compare all info between characters
    results1: 
    char_id: resource_id of a unique character
    """
    correlation = {
        "characters": [char1['name'], char2['name']],
        "films": [],
        "species": [],
        "vehicles": [],
        "starships": []
    }

    # compares attributes that only have one value
    # creates a new key-value pair if matching values
    if char1['height'] == char2['height']:
        correlation['height'] = char1['height']

    if char1['mass'] == char2['mass']:
        correlation['mass'] = char1['mass']

    if char1['birth_year'] == char2['birth_year']:
        correlation['birth_year'] = char1['birth_year']

    if char1['gender'] == char2['gender']:
        correlation['gender'] = char1['gender']

    hair1 = char1['hair_color']
    hair2 = char2['hair_color']
    # convert strings of hair colors into sets and find intersection
    hair1_set = set(color.strip() for color in hair1.split(","))
    hair2_set = set(color.strip() for color in hair2.split(","))
    hair_intersection = list(hair1_set & hair2_set)

    if hair_intersection:
        correlation['hair_color'] = str(hair_intersection)[1:-1]

    skin1 = char1['skin_color']
    skin2 = char2['skin_color']
    # convert strings of skin colors into sets and find intersection
    skin1_set = set(color.strip() for color in skin1.split(","))
    skin2_set = set(color.strip() for color in skin2.split(","))
    skin_intersection = list(skin1_set & skin2_set)
    if skin_intersection:
        correlation['skin_color'] = str(skin_intersection)[1:-1]

    eye1 = char1['eye_color']
    eye2 = char2['eye_color']
    # convert strings of eye colors into sets and find intersection
    eye1_set = set(color.strip() for color in eye1.split(","))
    eye2_set = set(color.strip() for color in eye2.split(","))
    eye_intersection = list(eye1_set & eye2_set)
    if eye_intersection:
        correlation['eye_color'] = str(eye_intersection)[1:-1]

    if char1['homeworld'] == char2['homeworld']:
        homeworld_url = char1['homeworld']
        homeworld_id = homeworld_url.split("/")[-2] 
        homeworld = get_swapi_resource("planets", homeworld_id)
        if homeworld:
            correlation['homeworld'] = homeworld['name'] # creates new key-value pair if common homeworld

    # converts both list of films into sets and finds intersection
    film_intersection = list(set(char1['films']) & set(char2['films']))
    common_films = [] # list of url converted into film titles

    if film_intersection:
        for url in film_intersection:
            film_id = url.split("/")[-2]
            film = get_swapi_resource("films", film_id)
            common_films.append(film['title']) # appends title to list
        
        correlation['films'].extend(common_films)

    # converts both list of species into sets and finds intersection
    species_intersection = list(set(char1['species']) & set(char2['species']))
    common_species = [] # list of url converted into species names

    if species_intersection:
        for url in species_intersection:
            species_id = url.split("/")[-2]
            species = get_swapi_resource("species", species_id)
            common_species.append(species['name']) # appends species name to list
        
        correlation['species'].extend(common_species)

    # converts both list of vehicles into sets and finds intersection
    vehicles_intersection = list(set(char1['vehicles']) & set(char2['vehicles']))
    common_vehicles = [] # list of url converted into vehicle names

    if vehicles_intersection:
        for url in vehicles_intersection:
            vehicle_id = url.split("/")[-2]
            vehicle = get_swapi_resource("vehicles", vehicle_id)
            common_vehicles.append(vehicle['name']) # appends vehicle name to list
        
        correlation['vehicles'].extend(common_vehicles)

    # converts both list of starships into sets and finds intersection
    starships_intersection = list(set(char1['starships']) & set(char2['starships']))
    common_starships = [] # list of url converted into starship names

    if starships_intersection:
        for url in starships_intersection:
            starship_id = url.split("/")[-2]
            starship = get_swapi_resource("starships", starship_id)
            common_starships.append(starship['name']) # appends starship name to list
        
        correlation['starships'].extend(common_starships)

    # display common character info
    if 'height' in correlation:
        print(f"Height: {correlation['height']} cm")

    if 'mass' in correlation:
        print(f"Mass: {correlation['mass']} kg")

    if 'hair_color' in correlation:
        print(f"Hair-color: {correlation['hair_color']}")
    
    if 'skin_color' in correlation:
        print(f"Skin-color: {correlation['skin_color']}")

    if 'eye_color' in correlation:
        print(f"Eye-color: {correlation['eye_color']}")
    
    if 'birth_year' in correlation:
        print(f"Birth-year: {correlation['birth_year']}")

    if 'gender' in correlation:
        print(f"Gender: {correlation['gender']}")

    if 'homeworld' in correlation:
        print(f"Homeworld: {correlation['homeworld']}")

    if correlation['films']:
        print("Films: " + str(correlation['films'])[1:-1])

    if correlation['species']:
        print("Species: " + str(correlation['species'])[1:-1])

    if correlation['vehicles']:
        print("Vehicles: " + str(correlation['vehicles'])[1:-1])

    if correlation['starships']:
        print("Starships: " + str(correlation['starships'])[1:-1])

    # Save connections between characters to file
    if correlation:
        person1 = "_".join(char1['name'].split())
        person2 = "_".join(char2['name'].split())
        filename = os.path.join(data_dir, f"{person1}_{person2}.json")
        with open(filename, 'w') as file:
            json.dump(correlation, file, indent=4)

        print(f"\nCharacter connections saved to {filename}.") 

def planet_statistics():
    """
    Function to generate average population.
    """
    statistics = {}
    results = get_swapi_resource("planets")
    planet_populations = {}

    if results['count'] % 10 == 0:
        pages = results['count']//10 # return number of pages of results. Each page has a max of 10 planets
    else:
        pages = int(math.trunc(results['count']/10) + 1)

    print(f"\nFinding largest population:")
    for i in range(1, pages+1): # loops through all pages of search_term and returns results
        page = "?page=" + str(i) 
        current_page = get_swapi_resource("planets", page) # retrieves result of current page

        for planet in current_page['results']:
            try:
                int_population = int(planet['population'])
                planet_populations[planet['name']] = int(planet['population'])
            except ValueError:
                pass

    largest = max(planet_populations.values())
    planet = max(planet_populations, key=planet_populations.get)
    statistics['max_population'] = largest
    statistics['max_pop_planet'] = planet
    print(f"Largest Population: {statistics['max_population']}")
    print(f"Planet: {statistics['max_pop_planet']}")

    # Save statistics to file
    filename = os.path.join(data_dir, f"planet_statistics.json")
    with open(filename, 'w') as file:
        json.dump(statistics, file, indent=4)

    print(f"\nStatistics saved to {filename}.") 

def main():
    while True:
        print("\nOptions:")
        print("1. Search for Characters")
        print("2. Display Character Info")
        print("3. Compare Characters")
        print("4. Planet with Largest Population")
        print("5. Exit")

        choice = input("\nEnter a choice: ")

        if choice == "1": 
            search_term = input("Enter character name to search: ")
            search_character(search_term)

        elif choice == "2":
            exit_search = False
            while not exit_search:
                search_term = input("Search by name or ID: ").lower()
                
                # search by id
                if search_term == "id":
                    char_id = input("Enter a character ID: ")
                    character_info(char_id)
                    exit_search = True

                # search by name
                elif search_term == "name":
                    while True:
                        search_term = input("Enter character name to search: ")
                        character = get_swapi_resource("people",  search_query=search_term)
                        
                        if character['count'] == 1: # display details if only 1 character found
                            char_id = character['results'][0]['url'].split('/')[-2] # returns id of character
                            character_info(char_id)
                            exit_search = True
                            break
                        
                        elif character['count'] == 0:
                            print("Character not found.")
                            break

                        else:
                            print("Please enter a unique name.")

                else:
                    print("Enter 'name' or 'id' to search.")
            
        elif choice == "3":
            while True:
                char1 = input("Enter 1st character ID: ")
                results1 = get_swapi_resource("people", char1)
                if results1 and char1:
                    break
                else:
                    print("First character not found.")
                
            while True:
                char2 = input("Enter 2nd character ID: ")
                results2 = get_swapi_resource("people", char2)
                if results2 and char2:
                    break
                else:
                    print("Second character not found.")

            print(f"\nComparing {results1['name']} to {results2['name']}")
            compare_characters(results1, results2)

        elif choice == "4":
            planet_statistics()

        elif choice == "5":
            print("Now exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()   



       
