import base64


def filter_houses(
    houses,
    keyword=None,
    suburb=None,
    min_price=None,
    max_price=None,
    start_date=None,
    end_date=None,

    wifi=False,
    kitchen=False,
    carpark=False,
    ac=False,

    tenant_num=None,
    order_type="default"
):
    filtered_houses = houses
    filtered_houses = filter_houses_with_keyword(filtered_houses, keyword)
    filtered_houses = filter_houses_with_suburb(filtered_houses, suburb)
    filtered_houses = filter_houses_with_min_price(filtered_houses, min_price)
    filtered_houses = filter_houses_with_max_price(filtered_houses, max_price)
    filtered_houses = filter_houses_with_conditions(filtered_houses, wifi, kitchen, carpark, ac)
    filtered_houses = filter_houses_with_tenant_num(filtered_houses, tenant_num)
    filtered_houses = filter_houses_with_date(filtered_houses, start_date, end_date)

    filtered_houses = order_filtered_houses(filtered_houses, order_type)
    return filtered_houses


def filter_houses_with_keyword(houses, keyword):
    filtered_houses = []
    if keyword:
        for house in houses:
            keyword = keyword.lower()
            # simple keyword search
            if keyword in house["title"].lower() or keyword in house["description"].lower() or keyword in house["suburb"].lower():
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def filter_houses_with_suburb(houses, suburb):
    filtered_houses = []
    if suburb:
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
    if max_price:
        for house in houses:
            if int(house["price"]) <= max_price:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses

def filter_houses_with_tenant_num(houses, tenant_num):
    filtered_houses = []
    if tenant_num:
        for house in houses:
            if int(house["tenant_num"]) == tenant_num:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses

def get_order_key(order_type):
    order_key = "_id"
    if order_type.startswith("price"):
        order_key = "price"
    elif order_type.startswith("rating_num"):
        order_key = "rating_num"
    elif order_type.startswith("rating"):
        order_key = "rating"
    elif order_type.startswith("size"):
        order_key = "size"
    return order_key

def order_filtered_houses(houses, order_type):
    if not order_type:
        return houses
    if order_type == "default":
        return houses
    else:
        order_key = get_order_key(order_type)
        if order_type.endswith("asc"):
            houses.sort(key=lambda x : float(x[order_key]), reverse=False)
        elif order_type.endswith("desc"):
            houses.sort(key=lambda x : float(x[order_key]), reverse=True)
        return houses

# test = [{"title": "house 1", "price": "200"}, {"title": "house 2", "price": "150"}, {"title": "house 3", "price":"300"}]
# print(test)
# print(order_filtered_houses(test, "price_asc"))
# print(order_filtered_houses(test, "price_desc"))

# fake availability check, can be implemented in the future
def checkHouseAvailability(house, start_date, end_date):
    return True


def filter_houses_with_date(houses, start_date, end_date):
    filtered_houses = []
    if start_date and end_date:
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

def filter_houses_with_conditions(houses, wifi, kitchen, carpark, ac):
    filtered_houses = houses
    filtered_houses = filter_houses_with_condition(filtered_houses, "wifi", wifi)
    filtered_houses = filter_houses_with_condition(filtered_houses, "kitchen", kitchen)
    filtered_houses = filter_houses_with_condition(filtered_houses, "carpark", carpark)
    filtered_houses = filter_houses_with_condition(filtered_houses, "ac", ac)
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