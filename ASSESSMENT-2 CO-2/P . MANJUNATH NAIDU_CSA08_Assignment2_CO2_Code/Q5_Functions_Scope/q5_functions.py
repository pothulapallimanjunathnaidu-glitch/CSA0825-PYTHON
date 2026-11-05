def add_item_bad(item, order=[]):
    order.append(item)
    return order


print("Mutable default argument:")
print(add_item_bad("Rice"))
print(add_item_bad("Milk"))


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


print("\\nCorrect solution:")
customer1 = add_item("Rice")
customer2 = add_item("Milk")
customer3 = add_item("Bread", ["Eggs"])
print(customer1)
print(customer2)
print(customer3)


def bill(price, quantity=1, discount=0):
    total = price * quantity
    return total - total * discount / 100


print("\\nBill calculations:")
print(bill(100, 2, 10))
print(bill(price=100, quantity=2))
print(bill(100))


def calculate(a, b):
    return a + b, a * b


total, product = calculate(5, 3)
print("\\nSum:", total)
print("Product:", product)


count = 10


def outer():
    value = 1

    def inner():
        nonlocal value
        value += 1
        return value

    return inner()


print("\\nInner result:", outer())
print("Global count:", count)
