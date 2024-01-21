def insert_json(data, collection):
    result = collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} documents")