import main


def test_sales_tax_ma():
    sales_tax = main.get_state("MA")
    assert sales_tax == .0625


def test_sales_tax_me():
    sales_tax = main.get_state("ME")
    assert sales_tax == .055


def test_sales_tax_nh():
    sales_tax = main.get_state("NH")
    assert sales_tax == 0


def test_wic_total():
    wic_item_price = main.get_wic()
    assert wic_item_price == main.Wic_Eligible_food.get('Fish') + main.Wic_Eligible_food.get('Eggs') + \
           main.Wic_Eligible_food.get('Milk')  # checks just [Fish, Eggs, Milk]


def test_clothing_total():
    clothing_item_price = main.get_clothing()
    assert clothing_item_price == main.clothing.get('hat') + main.clothing.get('shirt') + main.clothing.get('pants')
    # checks just [hat, shirt, pants]


def test_everything_else_total():
    everything_else_item_price = main.get_everything_else()
    assert everything_else_item_price == main.everything_else.get('toys') + main.everything_else.get('tools') +\
           main.everything_else.get('chair')  # checks just [toys, tools, chair]


def test_get_sales_tax_nh():
    sales_tax = main.get_state('NH')
    clothing = main.get_clothing()
    everything_else = main.get_everything_else()
    sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'NH')
    assert sales_tax_total == 0


def test_get_sales_tax_ma():
    sales_tax = main.get_state('MA')
    clothing = main.get_clothing()
    everything_else = main.get_everything_else()
    if clothing > 175:
        sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'MA')
        assert sales_tax_total == (clothing + everything_else) * sales_tax
    else:
        sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'MA')
        assert sales_tax_total == everything_else * sales_tax


def test_get_sales_tax_me():
    sales_tax = main.get_state('ME')
    clothing = main.get_clothing()
    everything_else = main.get_everything_else()
    sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'ME')
    assert sales_tax_total == (clothing + everything_else) * sales_tax


def test_get_total_with_tax():
    state = 'ME'
    sales_tax = main.get_state(state)
    clothing = main.get_clothing()
    everything_else = main.get_everything_else()
    Wic_eligible_food = main.get_wic()
    sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, state)
    final = main.goods_total(sales_tax_total + Wic_eligible_food, clothing, everything_else)
    assert final == sales_tax_total + clothing + Wic_eligible_food + everything_else


def test_get_total_without_tax():
    clothing = main.get_clothing()
    everything_else = main.get_everything_else()
    Wic_eligible_food = main.get_wic()
    total_without_tax = main.goods_total(Wic_eligible_food, clothing, everything_else)
    assert total_without_tax == clothing + Wic_eligible_food + everything_else


def test_main():
    total_after_tax = main.main()
    assert total_after_tax == 138.07562499999997

    # only checks if it get the right total for [Fish, Eggs, Milk]
    # ['hat', 'shirt', 'pants'] and [tools, toys, chair] in MA
