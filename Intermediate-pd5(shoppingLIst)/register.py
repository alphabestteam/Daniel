from costumer import costumer


class register:

    def __init__(self) -> None:

        self._sales_history = []

    @property
    def sales_history(self):
        return self._sales_history

    def check_out_customer(self, client: costumer):
        total_cost = 0
        for item in client.shopping_list:
            item_cost = item["product"].item_price * item["item_qut"]
            total_cost += item_cost
        new_client = {
            'name': client.name,
            'total': total_cost,
            'cart': [{'name': item["product"].item_name, 'price': item['product'].item_price, 'amount': item['item_qut']} for item in client.shopping_list]
        }
        self.sales_history.append(new_client)
        print(f"Client {client.name}'s total: {total_cost}")

    def print_summary(self):
        total_register = 0
        list_of_product_sales = []
        for item in self.sales_history:
            total_register += item['total']
            list_of_product_sales.append(item['cart'])
        print(f"\nTotal profit: {total_register}. ~~ Items: {list_of_product_sales}")
