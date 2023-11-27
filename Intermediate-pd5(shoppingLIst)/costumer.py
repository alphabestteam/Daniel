from product import product


class costumer:

    def __init__(self, name: str) -> None:
        self._costumer_name = name
        self._shopping_list = []

    @property
    def name(self):
        return self._costumer_name

    @property
    def shopping_list(self):
        return self._shopping_list

    def add_product(self, item_name, item_price, item_qut):
        for item in self.shopping_list:
            if item["product"].item_name == item_name:
                item["item_qut"] += item_qut
                return
        new_item = {"product": product(item_name, item_price), "item_qut": item_qut}
        self.shopping_list.append(new_item)

    def remove_product(self, item_name, item_qut):
        for item in self.shopping_list:
            if item["product"].item_name == item_name:
                item["item_qut"] -= item_qut
                print(
                    f"removed {item_qut, item['product'].item_name} from list")
                if item["item_qut"] <= 0:
                    self.shopping_list.remove(item)
            else:
                print("item not found!")
