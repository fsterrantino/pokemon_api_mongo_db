def query_all_documents(collection):
    all_documents = collection.find()
    all_documents_list = list(all_documents)

    return all_documents_list
