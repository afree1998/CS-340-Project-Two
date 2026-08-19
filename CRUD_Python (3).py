# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    #I changed this so that it takes in the username and password on the initialization of the object
    def __init__(self, USER, PASS): 
        #USER = 'aacuser' 
        #PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        
        ##Removed this to make the program more malleable
        #self.database = self.client['%s' % (DB)] 
        #self.collection = self.database['%s' % (COL)] 

    #This create takes in the database and collection that is the intended target.
    #While using the default would have been easy, this increases the ability to use the program outside of this example
    def create(self, db, col, data):
        print("Attempting to add record...")
        
        try:
            database = self.client[db]
            collection = database[col]
            ##If the data is present then insert
            if data is not None: 
                collection.insert_one(data)
                return True
            #Otherwise return false
            return False
        
        ##If all else fails throw an exception and return false
        except Exception as error:
            print(f"Operation failed: {error}")
            return False
        
        
    #Edited the read method so that it takes in the database and collection
    def read(self, db, col, data):
        
        #Attempt to connect to the database and collection specified in the function method
        try:
            database = self.client[db]
            collection = database[col]
            
            #If data is present, find the data in the set and return the list
            if data is not None:
                result = collection.find(data)
                return list(result)
            
        ##IF something happens just return an empty list
        except Exception as error:
            print(f"Operation failed: {error}")
            return []
        
        
    #Specify the database and collection that we're targeting as well as the data and updates we're attempting to make
    def update(self, db, col, data, update):
        
        #Try to make those updates by connecting to the database and collection
        try:
            database = self.client[db]
            collection = database[col]
            
            #If something exists in the input then attempt to update and return the modified count
            if data is not None:
                result = collection.update_many(data, update)
                print("Update finished:")
                
                return result.modified_count
            
        #Otherwise, throw an error and return a zero
        except Exception as error:
            print(f"Operation failed: {error}")
            return 0

    ##Specify the database and collection
    def delete(self, db, col, data):
        
        #Connect to the specified databse and collection, and then attempt to delete the data specified
        try:
            database = self.client[db]
            collection = database[col]
            
            if data is not None:
                result = collection.delete_many(data)
                return result.deleted_count
            
        #If something goes wrong throw an error and return zero
        except Exception as error:
            print(f"Operation failed: {error}")
            return 0
        