
class product:

    def __init__(self, item_name: str, item_price: int) -> None:
        self._item_name = item_name
        self._item_price = item_price

    @property
    def item_name(self):
        return self._item_name

    @property
    def item_price(self):
        return self._item_price
