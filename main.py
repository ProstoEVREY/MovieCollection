def AddMovie():
    title = input("Please, enter the name of the movie: ")
    produc = input("Please, enter the production year: ")
    country = input("Please, enter the country, where the movie was produced: ")
    director = input("Please, enter the name of the director: ")
    return {"title":title,"Production":produc,"country":country,"director":director}

def Remove(database):
    user = input("Please, enter the name of the movie you wish to remove: ")
    counter2 = 0
    for item in database:
        if(user == item["title"]):
            database.remove(item)
            print("Object deleted!")
        else:
            counter2+=1
    if(counter2>0):
        print("No such element!")
    return database


add = lambda data:data.append(AddMovie())

def ListMovies(data):
    for item in data:
        print(f'{item["title"]} is a {item["Production"]} year, directed by {item["director"]} in {item["country"]}')

def MainAction(message,database):
    while(1):
        print(message)
        x = int(input())
        if(x==1):
            if(database!=[]):
                ListMovies(database)
            else:
                print("No movies yet!")
                continue
        elif(x==2):
            add(database)
        elif(x==3):
            if(database!=[]):
                database = Remove(database)
            else:
                print("No movies yet!")
        elif(x==4):
            a = input("What do you want to find? ")
            counter = 0
            for item in database:
                if(a == item["title"] or a==item["Production"] or a==item["country"] or a==item["director"]):
                    print(f'{item["title"]} is a {item["Production"]} year, directed by {item["director"]} in {item["country"]}')
                else:
                    counter+=1
            if(counter>0):
                print("No such an element!")
        else:
            print("Bye bye!")
            break
intromessage = """Welcome to the application! Please choose, what you want to do!
1. List all of the movies
2. Add a movie to the list
3.Remove a movie from the list
4. Search the list
Anything else. Quit the application
"""

maindatabase = []
MainAction(intromessage,maindatabase)

