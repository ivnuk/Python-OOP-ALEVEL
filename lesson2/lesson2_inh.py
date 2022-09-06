from lesson1.practice import Element


class Connector:
    # def __init__(self, db_url=None, api_url=None, auth_username=None, auth_password=None):
    #     if db_url is None:
    #         pass
    #     if api_url is None:
    #         pass

    def connect(self):
        # if self.db_url ...
        # if self.api_url ...
        raise NotImplementedError

    def get_data(self, context):
        raise NotImplementedError


class DBConnector(Connector):
    def __init__(self, db_url):
        self.db_url = db_url

    def connect(self):
        """
        Create connection to specific database
        :return:
        """

    def get_data(self, context):
        """
        Get information based on the given context
        executing sql query
        :param context:
        :return:
        """

    def __del__(self):
        self.drop_connection()


class APIConnector(Connector):
    def __init__(self, api_url, auth_username, auth_password):
        self.api_url = api_url
        self.auth_username = auth_username
        self.auth_password = auth_password

    def connect(self):
        """
        Get API token to communicate via API
        :return:
        """

    def get_data(self, context):
        """
        Get the data sending the specific request
        :param context:
        :return:
        """


class RedisConnector(Connector):
    pass


class Boat:

    def swim(self):
        print("I can swim.")


class Car:
    def ride(self):
        print("I can ride.")


class AmphibiousVehicle(Car, Boat):
    # def __mro_entries__(self, bases):
    #     ...
    def swim(self):
        self.ride()
        super(AmphibiousVehicle, self).swim()


class A:
    def __init__(self):
        self.prop1 = 1
        pass

    def meth1(self):
        if self.prop1 > 0:
            pass


class B(A):
    def __init__(self):
        super(B, self).__init__()


class C(B):
    def __init__(self):
        super().__init__()
        pass


class D(B):
    def __init__(self):
        super(D, self).__init__()


class E(D, C):
    pass


print(__name__)

if __name__ == '__main__':
    # amphib = AmphibiousVehicle()
    # print(__name__)
    # amphib.ride()
    # amphib.swim()
    # print(amphib.__class__.__mro__)
    # print(E.__mro__)
    # elem = Element(10, 20)

    d = D()
    print(isinstance(d, D))
    print(isinstance(d, B))
    print(isinstance(d, C))
    print(issubclass(d.__class__, A))
