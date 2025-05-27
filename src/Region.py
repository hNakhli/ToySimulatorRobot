
class Region:
    
    # Region is where the boundary and any obstractions (or other objects)
    # would be defined in. Objects must be validated with respect to the
    # map before being placed in it.
    # Note: We could have used a library for this like shapely that has
    # 2D geometry support but for now i've this to be simple
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        
    def in_bound(self, x, y) -> bool:
        try:
            x = int(x)
            y = int(y)
        except Exception:
            # if the conversion failed - return false
            # we could throw an error here to catch the bug early.
            return False
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max