def filter_houses(houses, suburb=None):
    filtered_houses = []
    if suburb:
        for house in houses:
            if house['suburb'] == suburb:
                filtered_houses.append(house)
        return filtered_houses
    else:
        return houses


def get_online_data():
    return []

# extract valid data used for updating
def get_update_info(data_object):
    update_info = {}
    for attr in data_object:
        if data_object[attr]:
            update_info[attr] = data_object[attr]
    return update_info
