class mouse:
    def setMouse(self, brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price

    def getMouse(self):
        print("mouse info : ")
        print("brand : ",self.brand)    
        print("color : ",self.color)    
        print("price : ",self.price)    
        print("----------------------")    


m1=mouse()
m1.setMouse("HP","red",300)
m1.getMouse()

m2=mouse()
m2.setMouse("lenova","blue",400)
m2.getMouse()


m1.getMouse()
m2.getMouse()
