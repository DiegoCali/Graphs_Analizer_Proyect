
class Circle:
    def __init__(self, name, diameter, coords, color):
        self.name = name
        self.diameter = diameter
        self.coords = coords
        self.color = color

    def paint(self, c):
        x1 = self.coords[0] - (self.diameter / 2)
        y1 = self.coords[1] - (self.diameter / 2)
        x2 = self.coords[0] + (self.diameter / 2)
        y2 = self.coords[1] + (self.diameter / 2)
        c.create_oval(x1, y1, x2, y2, fill=self.color)
        c.create_text(self.coords[0], self.coords[1], text=self.name)

    def change_color(self, color, c):
        self.color = color
        self.paint(c)


class Line:
    def __init__(self, name, coords_init, coords_finish, color):
        self.name = name
        self.coords_init = coords_init
        self.coords_end = coords_finish
        self.color = color

    def paint(self, c):
        c.create_line(self.coords_init[0], self.coords_init[1],
                      self.coords_end[0], self.coords_end[1], width=3, fill=self.color)
        middle_point_x = (self.coords_init[0] + self.coords_end[0])/2
        middle_point_y = (self.coords_init[1] + self.coords_end[1])/2
        c.create_text(middle_point_x, middle_point_y, text=self.name, fill="blue")

    def change_color(self, color, c):
        self.color = color
        self.paint(c)
