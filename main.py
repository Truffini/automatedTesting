Wic_Eligible_food = {
    'Baby Food': 1.39, 'Breakfast Cereal': 3.79, 'Canned Beans': 1.79, 'Cheese': 1.91, 'Dried Beans/Peas/Lentils': 1.04,
    'Eggs': 1.48, 'Fish': 11.00, 'Fruits and Vegetables': 2.00, 'Infant Formula': 35.49, 'Juice for Children': 9.98,
    'Juice for Women': 6.59, 'Milk': 2.19, 'Peanut Butter': 5.78, 'Soy Beverage': 2.58, 'Tofu': 1.69,
    'Whole Grain Choices': 4.09, 'Yogurt': 1.59, 'checkout': 0
}
clothing = {
    'shirt': 15.00, 'shoes': 100.00, 'pants': 20.00, 'shorts': 10.00, 'jacket': 50.00, 'hat': 30.00,
    'socks': 5.00, 'underwear': 10.00, 'sweatshirt': 40.00, 'gucci': 180, 'checkout': 0
}
everything_else = {'toys': 9.99, 'tools': 19.99, "school supplies": 29.99, "appliances": 14.99, "chair": 24.99,
                   'laptop': 999.99, 'checkout': 0
                   }


# print("All Wic eligible food items ", Wic_Eligible_food)
# print("All clothing items ", clothing)
# print("Everything else ", everything_else)


def get_state(state):
    # state = 'MA'
    # state = input('enter state abbreviation - ')
    print(state)
    if state == 'MA':
        sales_tax = .0625
    elif state == 'NH':
        sales_tax = 0
    elif state == 'ME':
        sales_tax = .055
    else:
        print('not available')

    print("your sales tax will be", sales_tax)
    return sales_tax


def get_wic(Wic_item):
    # print("type checkout to move on to clothing")
    # Wic_item = input("add Wic item - ")
    price_of_Wic_item = Wic_Eligible_food.get(Wic_item)
    # print(price_of_Wic_item)
    list_of_Wic = []

    if Wic_item != 'checkout':
        list_of_Wic.append(price_of_Wic_item)
        # Wic_item = input("add Wic item - ")
        price_of_Wic_item = Wic_Eligible_food.get(Wic_item)
        print(price_of_Wic_item)
        return price_of_Wic_item

    if Wic_item == 'checkout':
        print(list_of_Wic)
        Wic_total = 0
        for price_of_Wic_item in list_of_Wic:
            Wic_total += price_of_Wic_item
        print(Wic_total)
        return Wic_total


def get_clothing(clothing_item):
    # print("type checkout to move to everything else")
    # clothing_item = input("add clothing item - ")
    price_of_clothing_item = clothing.get(clothing_item)
    # print(price_of_clothing_item)
    list_of_clothing = []

    while clothing_item != 'checkout':
        list_of_clothing.append(price_of_clothing_item)
        # clothing_item = input("add clothing item - ")
        price_of_clothing_item = clothing.get(clothing_item)
        print(price_of_clothing_item)
        return price_of_clothing_item

    if clothing_item == 'checkout':
        print(list_of_clothing)
        clothing_total = 0
        for price_of_clothing_item in list_of_clothing:
            clothing_total += price_of_clothing_item
        print(clothing_total)
        return clothing_total


def get_everything_else(everything_else_item):
    # print("type checkout to finish")
    # everything_else_item = input("add other item - ")
    price_of_everything_else_item = everything_else.get(everything_else_item)
    # print(price_of_everything_else_item)
    list_of_everything_else = []

    while everything_else_item != 'checkout':
        list_of_everything_else.append(price_of_everything_else_item)
        # everything_else_item = input("add  other item - ")
        price_of_everything_else_item = everything_else.get(everything_else_item)
        print(price_of_everything_else_item)
        return price_of_everything_else_item

    if everything_else_item == 'checkout':
        print(list_of_everything_else)
        everything_else_total = 0
        for price_of_everything_else_item in list_of_everything_else:
            everything_else_total += price_of_everything_else_item
        print(everything_else_total)
        return everything_else_total


def get_total_sales_tax(clothing_total, everything_else_total, sales_tax, state):
    if state == 'MA' and clothing_total > 175:
        sales_tax_total = (clothing_total + everything_else_total) * sales_tax
        print("sales tax total - ", sales_tax_total)
        return sales_tax_total
    elif state == 'MA' and clothing_total < 175:
        sales_tax_total = everything_else_total * sales_tax
        print("sales tax total - ", sales_tax_total)
        return sales_tax_total
    else:
        sales_tax_total = (clothing_total + everything_else_total) * sales_tax
        print("sales tax total - ", sales_tax_total)
        return sales_tax_total


def goods_total(Wic_total, clothing_total, everything_else_total):
    goods_total = Wic_total + clothing_total + everything_else_total
    print("total before tax", goods_total)
    return goods_total


def main():
    state = 'MA'
    sales_tax = get_state(state)
    Wic_total = get_wic('Fish')
    clothing_total = get_clothing('gucci')
    everything_else_total = get_everything_else('tools')
    total_after_tax = (get_total_sales_tax(clothing_total, everything_else_total, sales_tax, state) +
                       goods_total(Wic_total, clothing_total, everything_else_total))
    print("total after tax", total_after_tax)
    return total_after_tax


if __name__ == '__main__':
    main()
