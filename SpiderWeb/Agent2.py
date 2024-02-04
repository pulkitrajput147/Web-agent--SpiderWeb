# For  Data Storing and  Querying

from arango import ArangoClient
import openai
import json

class QueryAnsweringAgent:
    def __init__(self, db_name, collection_name):
        self.client = ArangoClient()
        self.db_name = db_name
        self.collection_name = collection_name

        # Connect to the "_system" database as the root user
        sys_db = self.client.db('_system', username='root', password='')

        # Create a new database if it does not exist
        if not sys_db.has_database(self.db_name):
            sys_db.create_database(self.db_name)

        # Connect to the specified database
        self.db = self.client.db(self.db_name, username='root', password='')

        # Create a new collection if it does not exist
        if not self.db.has_collection(self.collection_name):
            self.db.create_collection(self.collection_name)


    def store_data_in_database(self, data):
        # Insert data into the collection
        self.db[self.collection_name].insert(data)

    def answer_query(self, user_query):
        # Query processing and retrieval logic
        query = f"FOR doc IN {self.collection_name} FILTER CONTAINS(doc.company_name, '{user_query}') RETURN doc"
        cursor = self.db.aql.execute(query)
        results = [document for document in cursor]

        if results:
            return results
        else:
            return None