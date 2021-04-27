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


def get_state(state):
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


def get_wic():
    list_of_Wic = ['Eggs', 'Fish', 'Milk']
    print(list_of_Wic)
    wic = 0
    Wic_total = 0
    while (len(list_of_Wic)) > 0:
        Wic_total += Wic_Eligible_food.get(list_of_Wic[wic])
        wic += 1
        if wic == (len(list_of_Wic)):
            break
    print(Wic_total)
    return Wic_total


def get_clothing():
    list_of_clothing = ['hat', 'shirt', 'pants']
    print(list_of_clothing)
    cloth = 0
    clothing_total = 0
    while (len(list_of_clothing)) > 0:
        clothing_total += clothing.get(list_of_clothing[cloth])
        cloth += 1
        if cloth == (len(list_of_clothing)):
            break
    print(clothing_total)
    return clothing_total


def get_everything_else():
    list_of_other = ['tools', 'toys', 'chair']
    print(list_of_other)
    other = 0
    other_total = 0
    while (len(list_of_other)) > 0:
        other_total += everything_else.get(list_of_other[other])
        other += 1
        if other == (len(list_of_other)):
            break
    print(other_total)
    return other_total


def get_total_sales_tax(clothing_total, other_total, sales_tax, state):
    if state == 'MA' and clothing_total > 175:
        sales_tax_total = (clothing_total + other_total) * sales_tax
        print("sales tax total - ", sales_tax_total)
        return sales_tax_total
    elif state == 'MA' and clothing_total < 175:
        sales_tax_total = other_total * sales_tax
        print("sales tax total - ", sales_tax_total)
        return sales_tax_total
    else:
        sales_tax_total = (clothing_total + other_total) * sales_tax
        print("sales tax total - ", sales_tax_total)
        return sales_tax_total


def goods_total(wic_total, clothing_total, other_total):
    goods_total = wic_total + clothing_total + other_total
    print("total before tax", goods_total)
    return goods_total


def main():
    state = 'MA'
    sales_tax = get_state(state)
    Wic_total = get_wic()
    clothing_total = get_clothing()
    other_total = get_everything_else()
    total_after_tax = (get_total_sales_tax(clothing_total, other_total, sales_tax, state) +
                       goods_total(Wic_total, clothing_total, other_total))
    print("total after tax", total_after_tax)
    return total_after_tax


if __name__ == '__main__':
    main()
