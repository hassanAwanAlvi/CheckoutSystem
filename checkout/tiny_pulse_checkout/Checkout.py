
product_dict = [ {'ProductCode' : '001' , 'Name' : 'Lavender heart' , 'Price' : 9.25},
                  {'ProductCode' : '002' , 'Name' : 'Personalised cufflinks' , 'Price' : 45.00},
                  {'ProductCode': '003', 'Name': 'Kids T-shirt', 'Price': 19.95}]

def promotional_rules(order_details):
    hits_for_001 = 0
    total_price = 0
    for order_code in order_details:
        price_of_order = get_price(order_code)
        if price_of_order == -1:                    #invalid code so invalid price, I simply skip that order
            continue

        if order_code == "001":
            hits_for_001 += 1
            if 1 < hits_for_001 < 3:
                total_price += price_of_order
                total_price -= 1.5
            elif hits_for_001 == 1:
                total_price += price_of_order
            else:
                total_price += 8.5

        else:
            total_price += price_of_order


    if total_price > 60:
        total_price = total_price - (total_price * 0.1)

    return round(total_price , 2)


def get_price(order_id):

    for product in product_dict:
        if product["ProductCode"] == order_id:
            return product["Price"]

    return -1
