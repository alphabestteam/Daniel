class Point:

    def __init__(self,x,y) -> None:
        self._x = x
        self._y = y

    def __str__(self):
        return "({0},{1})".format(self._x, self._y)

    def __add__(self, val):
        x = self._x + val._x
        y = self._y + val._y
        return (x, y) 
    def __eq__(self, val):
             if self._x == val._x and self._y == val._y:
                  return True
             else:
                  return False
         
         