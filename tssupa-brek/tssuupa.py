import turtle

class Tßüpa:
    def __init__(self):
        self.duks = turtle.getscreen()
        self.duks.bgcolor("black")
        self.duks.title("Tßüpa brek")
    

    def tok(self, āmaken: int, bākß: int, taskitā: int, trek: int, Þānb: int = 0):
        """
        Brek de tßüpa - ek de tsükā
        """
        turt = turtle.Turtle()
        turt.color("green")

        for _ in range(bākß):
            for i in range(āmaken):
                turt.fd(taskitā)
                turt.right(360 / āmaken)
            taskitā += trek
            turt.right(Þānb)