
class visible:
    #初期化、nameはstring
    def __init__(self,init_x_pos,init_y_pos,name):
        self.is_appear = False
        self.init_x_pos = init_x_pos
        self_init_y_pos = init_y_pos
        self.x_pos = init_x_pos
        self.y_pos = init_y_pos
        self.name = name

    def delete(self):
        self.is_appear = False

    def appear(self):
        self.is_appear = True

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

class Ball(visible):

    def __init__(self, init_x_pos, init_y_pos, name,x_speed,y_speed):
        super().__init__(init_x_pos, init_y_pos, name)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def turn_x(self):
        self.x_speed = -self.x_speed

    def turn_y(self):
        self.y_speed = -self.y_speed

    def move(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def touch(self):
        return

    def set_x_speed(self,speed):
        self.x_speed = speed

    def set_y_speed(self,speed):
        self.y_speed = speed

        

