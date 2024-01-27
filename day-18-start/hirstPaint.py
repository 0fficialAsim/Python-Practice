import colorgram

colors = colorgram.extract( "D:\VSCODE\Python Practice\day-18-start\picture.jpg",10 )

color_tuples = []

for Color in colors:
    temp = ( Color.rgb[0], Color.rgb[1] ,Color.rgb[2])
    color_tuples.append(temp)
    
print(color_tuples)