def filter_houses(
    houses,
    keyword=None,
    suburb=None,
    min_price=None,
    max_price=None,
    start_date=None,
    end_date=None,
    pet_allowed=None,
    party_allowed=None,
    smoke_allowed=None,
    has_wifi=None,
):
    filtered_houses = []
    filtered_houses += filter_houses_with_keyword(houses, keyword)
    filtered_houses += filter_houses_with_suburb(houses, keyword)
    filtered_houses += filter_houses_with_min_price(houses, keyword)
    filtered_houses += filter_houses_with_max_price(houses, keyword)
    filtered_houses += filter_houses_with_conditions(houses, pet_allowed, party_allowed, smoke_allowed)
    filtered_houses += filter_houses_with_facilities(houses, has_wifi)
    filtered_houses += filter_houses_with_date(houses, keyword)
    
    return filtered_houses


def filter_houses_with_keyword(houses, keyword):
    filtered_houses = []
    if keyword != None:
        for house in houses:
            # simple keyword search
            if keyword in house["description"]:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def filter_houses_with_suburb(houses, suburb):
    filtered_houses = []
    if suburb != None:
        for house in houses:
            if house["suburb"] == suburb:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def filter_houses_with_min_price(houses, min_price):
    filtered_houses = []
    if minPrice!= None:
        for house in houses:
            if minPrice <= house["price"]:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def filter_houses_with_max_price(houses, max_price):
    filtered_houses = []
    if max_price!= None:
        for house in houses:
            if house["price"] <= max_price:
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


def filter_houses_with_conditions(houses, pet_allowed, party_allowed, smoke_allowed):
    filtered_houses = []
    for house in houses:
        if house["pet_allowed"] == pet_allowed and house["party_allowed"] == party_allowed and house["smoke_allowed"] == smoke_allowed:
            filtered_houses.append(house)
    return filtered_houses


def filter_houses_with_facilities(houses, has_wifi):
    filtered_houses = []
    for house in houses:
        if house["has_wifi"] == has_wifi:
            filtered_houses.append(house)
    return filtered_houses


# extract valid data used for updating to avoid overwriting info with empty data
def get_update_info(data_object):
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