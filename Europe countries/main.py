import turtle
import pandas
import tkinter

s = turtle.Screen()
s.title('Europe')
s.setup(1450, 900)

#snaller becomes the name of the shape (non-gif, Shape class gives the coordinates)

smaller = tkinter.PhotoImage(file='Europe_blank_laea_location_map.gif').subsample(3, 4)
s.register_shape('smaller', turtle.Shape('image', smaller))

#use the name of the shape to access the shape (gif is more straightforward)
bg = turtle.Turtle('smaller')

#not necessary
bg.stamp()
bg.hideturtle()


bg.penup()


# adding coordinates to modified_data.csv

# def helper(x, y):
#     print(x, y)

# for i in range(47):
#     s.onscreenclick(helper)


#dataframe object (made up of many series object)
data = pandas.read_csv('final.csv', index_col=0)

scr = []

while len(scr) < 47:
    res = s.textinput(f'Country Names: {len(scr)}/ 47', 'Guess the name!')
    if res:
        res = res.title()

    if res in data['name'].tolist() and res not in scr:
        scr.append(res)
        cur = data[data['name'] == res]
        x, y = int(cur['x']), int(cur['y'])
        bg.goto(x, y)
        bg.write(res)
    if res == 'Exit' or res is None:
        break


#bitwise operators: ~ : not, | : or, & : and
#use iterrows to iterate thru the elements in pandas DataFrame
#shows the x and y coordinates of the countries missing
data[~data['name'].isin(scr)].to_csv('Missing_countries.csv')