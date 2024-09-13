import requests
from utils.constantas import BASE_URL

def createUser(user):
    url = f"{BASE_URL}/bot/users/"

    response = requests.post(url, data=user)
    print(response.json())

    return response.json()


def createUserPhone(user_id, user):
    url = f"{BASE_URL}/bot/users_phone/" + str(user_id)

    response = requests.post(url, data=user)
    print(response.json())

    return response.json()

def getUser(user_id):
    url = f"{BASE_URL}/bot/users/" + str(user_id)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False



def getUserPhone(user_id):
    url = f"{BASE_URL}/api/users_phone/{user_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False


def putUserLang(user_id, lang):
    url = f"{BASE_URL}/bot/users/" + str(user_id)
    response = requests.put(url, data={'user_id': user_id,'lang': lang})

    if response.status_code == 200:
        return response.json()

    return False

def putUserPhone(user_id, phone):
    url = f"{BASE_URL}/bot/users/" + str(user_id)
    response = requests.put(url, data={'user_id': user_id, 'phone': phone})

    if response.status_code == 200:
        return response.json()

    return False

def putUserFullname(user_id, fullname):
    url = f"{BASE_URL}/bot/users/" + str(user_id)
    response = requests.put(url, data={'user_id': user_id, 'fullname': fullname})

    if response.status_code == 200:
        return response.json()

    return False

def getCategorys():
    url = f"{BASE_URL}/foods/category/"
    return requests.get(url).json()

def getFoods(category):
    url = f"{BASE_URL}/foods/category/{category}/"

    return requests.get(url).json()

def addBasket(user_id, food_name, count):
    url = BASE_URL + f"/busket/create"
    response = requests.post(url, data={
        'user_id': user_id,
        'food_name':food_name,
        'count':count
        })
    if response.status_code != 200:
        raise Exception(f"Failed to add to basket: {response.status_code}")
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        raise Exception("Failed to decode JSON response")
    return response.json()



def getFood(food_name):
    url = f"{BASE_URL}/foods/{food_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False


def getBasketList(user_id):
    url = BASE_URL + f"/busket/list?user_id={user_id}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False


def getBasketItem(basket_id):
    response = requests.get(BASE_URL + f"food/busket-item?basket_id={basket_id}")
    return response.json()


def changeBasketItem(basket_id, action):
    response = requests.get(BASE_URL + f'/food/busket-change?basket_id={basket_id}&action={action}')
    return response.json()

def clearBasketAndSetRating(user_id):

    response = requests.get(BASE_URL + f'/busket/clear-and-rating?user_id={user_id}')
    return response.json()

def deleteBasket(food_name, user_id):
    response = requests.get(BASE_URL + f'/busket/delete?food_name={food_name}&user_id={user_id}')
    return response.json()