class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        for i, data in enumerate(self):
            if i == index:
                return data

        return None

    def append(self, data):
        if not self.head:
            self.head = self.tail = Node(None, None, data)
            self.size = 1
            return True

        node = Node(None, self.tail, data)
        self.tail.nextNode = node
        self.tail = node
        self.size += 1
        return True

    def prepend(self, data):
        if not self.head:
            self.head = self.tail = Node(None, None, data)
            self.size = 1
            return True

        node = Node(self.head, None, data)
        self.head.prevNode = node
        self.head = node
        self.size += 1

    def insert(self, pos, data):
        if pos > self.size or pos < 0:
            raise ValueError('invalid insert position')

        if pos == self.size:
            return self.append(data)

        if pos == 0:
            return self.prepend(data)

        curr = self.head
        i = 0
        while i < pos - 1:
            curr = curr.nextNode
            i += 1

        node = Node(curr.nextNode, curr, data)
        curr.nextNode.prevNode = node
        curr.nextNode = node
        self.size += 1
        return True

    def clean(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        self.iter_node = self.head
        return self

    def __next__(self):
        node = self.iter_node
        if not node:
            raise StopIteration
        self.iter_node = node.nextNode
        return node.data


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active

    def __repr__(self):
        return 'id: {} - {} {} {}$ a: {}'.format(
            self.identification,
            self.name,
            self.brand,
            self.price,
            self.active
        )


db = LinkedList()


def get_car_by_id(identification):
    """
    :rtype: Car
    """
    for car in db:
        if car.identification == identification:
            return car

    return None


def init(cars):
    for car in cars:
        add(car)


def add(car):
    for i, data in enumerate(db):
        if data.price > car.price:
            db.insert(i, car)
            return

    db.append(car)


def updateName(identification, name):
    car = get_car_by_id(identification)
    if car:
        car.name = name


def updateBrand(identification, brand):
    car = get_car_by_id(identification)
    if car:
        car.brand = brand


def activateCar(identification):
    car = get_car_by_id(identification)
    if car:
        car.active = True


def deactivateCar(identification):
    car = get_car_by_id(identification)
    if car:
        car.active = False


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    price = 0
    for car in db:
        if car.active:
            price += car.price

    return price


def clean():
    db.clean()

