from random import randrange
# generate random names
import names

def gen_email():
    random_num = randrange(1000000,10000000)
    return str(random_num) + "@mail.com"

def gen_name():
    return names.get_first_name()

def gen_phone():
    random_num = randrange(1000000,10000000)
    return str(random_num)

def gen_tenant_user():
    user = {}
    user["email"] = gen_email()
    user["name"] = gen_name()
    user["phone"] = gen_phone()
    user["password"] = "123"
    user["role"] = "tenant"
    return user

def gen_provider_user():
    user = {}
    user["email"] = gen_email()
    user["name"] = gen_name()
    user["phone"] = gen_phone()
    user["password"] = "321"
    user["role"] = "provider"
    return user


if __name__ == "__main__":
    print(gen_tenant_user())
    print(gen_provider_user())