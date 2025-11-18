# creating a classs in python

# class HouseKeeper:
#     pass

# marry = HouseKeeper()
# print(marry)

class StarCookie:
    milk = 0.1
    def __init__(self,color,weight=5):
        self.color = color
        self.weight = weight

star_cookie1 = StarCookie("Red")
print(star_cookie1.color)
print(star_cookie1.weight)
print(star_cookie1.milk)

star_cookie2 = StarCookie("Blue",10)
print(star_cookie2.color)
print(star_cookie2.weight)
print(star_cookie2.milk)
