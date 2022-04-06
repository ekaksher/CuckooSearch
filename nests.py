from typing import Tuple

from coordinate import Coordinate
class Nest(Coordinate):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__abandoned = True    
    @property
    def abandoned(self):
        return self.__abandoned
    
    def abandon(self) -> None:
        self.__abandoned = True
        self._initialize()

    def update_pos(self, new_position: Tuple[float, float]) -> None:
        """
        If the new position's value is better than the old one, update the nests position and value.

        Arguments:
            new_position {Tuple[float, float]} -- The new position
        """

        new_value = self._function(new_position)
        if new_value < self.value:
            if self.__abandoned:
                self.__abandoned = False
            # Value is updated automatically in base class
            self._position = new_position