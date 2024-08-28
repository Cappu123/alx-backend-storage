#!/usr/bin/env python3
"""lists all documents in a collection
"""
import pymongo

def list_all(mongo_collection):
    """prototype """
    if mongo_collection is None:
        return ({})
        coll = mongo_collection.find()
        result = []
        for i in mongo_collection:
            result.append(i)
            
        return result
