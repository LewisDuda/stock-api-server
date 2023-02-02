from datetime import datetime


def db_search(collection, payload):
    results = collection.find(payload, {"_id": 0})
    return list(results)


def date_to_timestamp(year, month, day):
    s_date = str(year) + "-" + str(month) + "-" + str(day)
    return int(datetime.strptime(s_date, "%Y-%m-%d").timestamp() * 1000)
