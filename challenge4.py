from classes import BaseHashMapManager


class User:
    def __init__(self, id: int, username: str, password: str) -> None:
        self.__id = id
        self.__username = username
        self.__password = password

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value


user_table = BaseHashMapManager()
alyson = User(1, "gentil-eilison", "bert@sesamestreet123")
kadson = User(2, "gentil-kadisson", "ernie@sesamestreet123")
carlos = User(3, "antonio-carlos", "malharmuitobom@libras")
user_table.add_item(alyson.id, alyson)
user_table.add_item(kadson.id, kadson)

carlos_in_table = user_table.find_item(carlos.id)

if not carlos_in_table:
    print("Carlos não está cadastrado! Vamos inserí-lo...")
    user_table.add_item(carlos.id, carlos)

user_table.update_item(alyson.id, username="gentil-alyson")
user_table.update_item(kadson.id, username="gentil-kadson")
print("Usuários com nome incorreto atualizados!")

alyson_hash = user_table.find_item(alyson.id)
kadson_hash = user_table.find_item(kadson.id)
carlos_hash = user_table.find_item(carlos.id)
print(alyson_hash.username, kadson.username, carlos.username, sep=" ")
