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
    wic_item_price = main.get_wic('Fish')
    assert wic_item_price == main.Wic_Eligible_food.get('Fish')


def test_clothing_total():
    clothing_item_price = main.get_clothing('hat')
    assert clothing_item_price == main.clothing.get('hat')


def test_everything_else_total():
    everything_else_item_price = main.get_everything_else('toys')
    assert everything_else_item_price == main.everything_else.get('toys')


def test_get_sales_tax_nh():
    sales_tax = main.get_state('NH')
    clothing = main.get_clothing('gucci')
    everything_else = main.get_everything_else('toys')
    sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'NH')
    assert sales_tax_total == 0


def test_get_sales_tax_ma():
    sales_tax = main.get_state('MA')
    clothing = main.get_clothing('gucci')
    everything_else = main.get_everything_else('tools')
    if clothing > 175:
        sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'MA')
        assert sales_tax_total == (clothing + everything_else) * sales_tax
    else:
        sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'MA')
        assert sales_tax_total == everything_else * sales_tax


def test_get_sales_tax_me():
    sales_tax = main.get_state('ME')
    clothing = main.get_clothing('hat')
    everything_else = main.get_everything_else('chair')
    sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, 'ME')
    assert sales_tax_total == (clothing + everything_else) * sales_tax


def test_get_total_with_tax():
    state = 'ME'
    sales_tax = main.get_state(state)
    clothing = main.get_clothing('hat')
    everything_else = main.get_everything_else('chair')
    Wic_eligible_food = main.get_wic('Fish')
    sales_tax_total = main.get_total_sales_tax(clothing, everything_else, sales_tax, state)
    final = main.goods_total(sales_tax_total + Wic_eligible_food, clothing, everything_else)
    assert final == sales_tax_total + clothing + Wic_eligible_food + everything_else


def test_get_total_without_tax():
    clothing = main.get_clothing('hat')
    everything_else = main.get_everything_else('chair')
    Wic_eligible_food = main.get_wic('Fish')
    total_without_tax = main.goods_total(Wic_eligible_food, clothing, everything_else)
    assert total_without_tax == clothing + Wic_eligible_food + everything_else


def test_main():
    total_after_tax = main.main()
    assert total_after_tax == 223.489375  # only checks if it get the right total for fish, gucci and tools in MA
