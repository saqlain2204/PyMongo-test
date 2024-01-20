import pymongo

print("Welcome to MongoDB")
print("Connecting to MongoDB...")
# Establishing connection with MongoDB
client = pymongo.MongoClient("<enter your connection string here>")
print("Connected to MongoDB successfully!")
print("Creating database...")
# Creating database
db = client["mydatabase"]
print("Database created!")
print("Creating collection...")
# Creating collection
col = db["customers"]
print("Collection created!")
print("Inserting one document...")
# Inserting one document
mydict = { "name": "John", "address": "Highway 37" }
x = col.insert_one(mydict)
print("Document inserted!")


# Fetching data from MongoDB
print("Fetching data from MongoDB...")
print("Fetching one document...")
x = col.find_one()
print(x['name'], x['address'])

# Fetching required data from MongoDB
print("Fetching required data from MongoDB...")
x = col.find_one({"name": 'John'})
print(x)

# Deleting a collection
print("Deleting a collection...")
col.drop()
print("Collection deleted!")

# Implementing user authentication
print("Implementing login and signup...")
print("Creating collection...")
# Creating database
db = client["Authentication_Details"]
# Creating collection
col = db["users"]
print("Collection created!")
while True:
    print("enter 1 for login and 2 for signup 3 to delete a user")
    x = int(input())
    if x==1:
        print("Enter username")
        username = input()
        print("Enter password")
        password = input()
        password = password[::-1]
        x = col.find_one({"username": username, "password": password})
        if x:
            print("Login successful")
            break
        else:
            print("Login failed")

    elif x==2:
        print("Enter username")
        username = input()
        print("Enter password")
        password = input()
        # Hashing password
        password = password[::-1]
        mydict = { "username": username, "password": password }
        x = col.insert_one(mydict)
        print("Signup successful")
        break

    else:
        print("Enter username")
        username = input()
        print("Enter password")
        password = input()
        password = password[::-1]
        # Matching username and password
        x = col.find_one({"username": username, "password": password})
        if x:
            # Deleting user
            col.delete_one({"username": username, "password": password})
            print("User deleted")
        else:
            print("User not found")

