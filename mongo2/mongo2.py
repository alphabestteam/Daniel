import pymongo


def main():

    connection_string = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(connection_string)
    aviv_db = client["Aviv's_people"]
    army_col = aviv_db["army_col"]
    friends_col = aviv_db["friends_col"]
    family_col = aviv_db["family_col"]

    aviv_db['army_col'].drop()
    aviv_db['friends_col'].drop()
    aviv_db['family_col'].drop()

    new_army_list = [{'name': 'Aviv', 'age': 20, 'role': 'Backend'},
                     {'name': 'Lihi', 'age': 21, 'role': 'QA'},
                     {'name': 'Gabi', 'age': 22, 'role': 'DevOps'},
                     {'name': 'Ori', 'age': 23, 'role': 'Frond-end'},
                     {'name': 'Ido', 'age': 22, 'role': 'developer'},
                     {'name': 'Yarden', 'age': 24, 'role': 'DevOps'}]

    new_friends_list = [{"_id": 1, 'name': 'Amit', 'age': 20, 'role': 'Waiter'},
                        {"_id": 2, 'name': 'Yonatan', 'age': 24, 'role': 'doctor'},
                        {"_id": 3, 'name': 'Noa', 'age': 22, 'role': 'student'},
                        {"_id": 4, 'name': 'Michal', 'age': 21, 'role': 'baker'}]

    new_family_list = [{'name': 'mother', 'age': 45, 'role': 'teacher'},
                       {'name': 'father', 'age': 46, 'role': 'engineer'},
                       {'name': 'brother', 'age': 12, 'role': 'school'},
                       {'name': 'sister', 'age': 24, 'role': 'student'}]

    x = army_col.insert_many(new_army_list)
    print("inserted army")

    y = friends_col.insert_many(new_friends_list)
    print("inserted friends")

    for name in new_family_list:
        x = family_col.insert_one(name)
    print("inserted family")

    army_col.delete_one({'name':'Lihi'})

    # for col in aviv_db.list_collection_names():
    #     for items in aviv_db[col].find():
    #         print(items)

    # ---------------------------------------------------------------------------

    # 1.
    dev_friend = army_col.find_one({'role': 'DevOps', 'age': {'$lt': 23}})
    print(dev_friend)
    2.
    new_role = army_col.find_one( {'age': dev_friend['age'], "_id": {"$ne": dev_friend['_id']}})
    army_col.update_one({'_id': dev_friend['_id']}, {'$set': {'role': new_role['role']}})

    sort_army = army_col.aggregate([{"$sort": {'age': -1}}])
    for friend in sort_army:
        print(friend)

    older = list(army_col.find({"age": {"$gt": 23}}))
    friends_col.insert_many(older)
    army_col.delete_many({"_id": {"$in": [doc["_id"] for doc in older]}})

if __name__ == '__main__':
    main()
