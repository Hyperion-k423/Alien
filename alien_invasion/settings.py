class Settings():               #这个类里面定义了许多基础设定
    def __init__(self):            #把这些成员定义在__init__方法下有一个好处就是在创建多个Settings对象时，他们的属性值可以不同而且不会相会影响
        self.screen_width = 1200        #如果把这些成员直接定义在class类里面，那他们的属性就固定了
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 30
        self.fleet_direction = 0.5