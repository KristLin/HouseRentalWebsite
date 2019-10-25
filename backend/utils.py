import base64


def filter_houses(
    houses,
    keyword=None,
    suburb=None,
    min_price=None,
    max_price=None,
    start_date=None,
    end_date=None,
    pet_allowed=False,
    party_allowed=False,
    smoke_allowed=False,
    has_wifi=False,
):
    filtered_houses = houses
    filtered_houses = filter_houses_with_keyword(filtered_houses, keyword)
    filtered_houses = filter_houses_with_suburb(filtered_houses, suburb)
    filtered_houses = filter_houses_with_min_price(filtered_houses, min_price)
    filtered_houses = filter_houses_with_max_price(filtered_houses, max_price)
    filtered_houses = filter_houses_with_conditions(houses, has_wifi, pet_allowed, party_allowed, smoke_allowed)
    filtered_houses = filter_houses_with_date(filtered_houses, start_date, end_date)
    
    return filtered_houses


def filter_houses_with_keyword(houses, keyword):
    filtered_houses = []
    if keyword != None:
        for house in houses:
            # simple keyword search
            if keyword.lower() in house["description"].lower():
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def filter_houses_with_suburb(houses, suburb):
    filtered_houses = []
    if suburb != None:
        for house in houses:
            if house["suburb"].lower() == suburb.lower():
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def filter_houses_with_min_price(houses, min_price):
    filtered_houses = []
    if min_price!= None:
        for house in houses:
            if min_price <= int(house["price"]):
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def filter_houses_with_max_price(houses, max_price):
    filtered_houses = []
    if max_price!= None:
        for house in houses:
            if int(house["price"]) <= max_price:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


# fake availability check, can be implemented in the future
def checkHouseAvailability(house, start_date, end_date):
    return True


def filter_houses_with_date(houses, start_date, end_date):
    filtered_houses = []
    if start_date != None and end_date != None:
        for house in houses:
            if checkHouseAvailability(house, start_date, end_date):
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses

def filter_houses_with_condition(houses, condition_name, condition):
    if condition:
        filtered_houses = []
        for house in houses:
            if condition_name in house and house[condition_name]:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses

def filter_houses_with_conditions(houses, has_wifi, pet_allowed, party_allowed, smoke_allowed):
    filtered_houses = houses
    print(has_wifi, pet_allowed, party_allowed, smoke_allowed)
    filtered_houses = filter_houses_with_condition(filtered_houses, "has_wifi", has_wifi)
    filtered_houses = filter_houses_with_condition(filtered_houses, "pet_allowed", pet_allowed)
    filtered_houses = filter_houses_with_condition(filtered_houses, "party_allowed", party_allowed)
    filtered_houses = filter_houses_with_condition(filtered_houses, "smoke_allowed", smoke_allowed)
    return filtered_houses


def filter_houses_with_facilities(houses, has_wifi):
    filtered_houses = []
    for house in houses:
        if house["has_wifi"] == has_wifi:
            filtered_houses.append(house)
    return filtered_houses


# extract valid data used for updating to avoid overwriting info with empty data
def get_valid_update_info(data_object):
    update_info = {}
    for attr in data_object:
        if data_object[attr]:
            update_info[attr] = data_object[attr]
    return update_info


def check_logged_in(active_users, email):
    for user_id in active_users:
        if active_users[user_id]["email"] == email:
            return True
    return False


def b64encode(file):
    return base64.b64encode(file)

def b64decode(str):
    return base64.b64decode(str)

def utf8decode(file):
    return file.decode('utf-8')

# parse data to json string
def parse_data(res):
    if type(res) == dict:
        for key in res:
            if type(res[key]) == bytes:
                res[key] = utf8decode(res[key])
            if type(res[key]) == list:
                altered_list = []
                for item in res[key]:
                    if type(item) == bytes:
                        altered_list.append(utf8decode(item))
                if altered_list:
                    res[key] = altered_list
    return res