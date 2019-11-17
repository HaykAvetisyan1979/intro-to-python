products = {"candy": 10, "juce": 5, "pen": 50}


def check(product, num):
    if product in products.keys():
        if products[product] >= num:
            return True

    return False
