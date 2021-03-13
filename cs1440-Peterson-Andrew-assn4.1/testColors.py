import colour

colorList = []
colorList += list(colour.Color("red").range_to(colour.Color("blue"), 33))[:-1]
colorList += list(colour.Color("blue").range_to(colour.Color("black"), 32))

print(colorList)