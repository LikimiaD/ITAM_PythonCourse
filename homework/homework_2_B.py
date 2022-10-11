def check(dict1, dict2):
    _dict = {}
    print((dict1.keys()-dict2.keys()) == set())
    if (dict1.keys()-dict2.keys()) == set():
        for x in dict1.keys():
            _dict[x] = 'equal'
        e = dict2.keys()-dict1.keys()
        for x in dict2.keys()-dict1.keys():
            _dict[str(x)] = 'added'
    else:
        for x in dict1.keys():
            _dict[x] = 'equal'
        e = dict2.keys()-dict1.keys()
        for x in dict1.keys()-dict2.keys():
            _dict[str(x)] = 'deleted'
    print(_dict)

dict1 = {"a":"b", "b":"a"}
dict2 = {"a":"b", "b":"a", "c": "a"}
check(dict1,dict2)
dict1 = {"a":"b", "b":"a",  "c": "a"}
dict2 = {"a":"b", "b":"a"}
check(dict1,dict2)