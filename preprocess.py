import os
import sys
import pandas as pd

x_min = 40.49890536
y_min = -74.25010159
x_max = 40.91504789
y_max = -73.68178027
x_temp = 40.52890536
y_temp = -74.28010159
grid={}
# finding the grid points inorder to divide the grid cells 3 miles each
i = 1 # number of grid cells created
while y_temp <= y_max: # checking for intermediate x and y values to be less than the max designated x and y values
    while x_temp <= x_max:
        grid[i]=[x_min, y_min, x_temp, y_temp] 
        i = i+1
        x_min = x_temp
        x_temp = x_temp + 0.03 # 0.03 of latitude or longitude corresponds to 3 miles
    x_min = 40.49890536 # resetting the x_min and x_temp values to the default to start the iteration from the first 2 points of x
    x_temp = 40.52890536     
    y_min = y_temp
    y_temp = y_temp + 0.03
for key in grid: # Representing the key and values pairs linewise
    print (key, ':', grid[key] )

# read csv into input value. column 2 column
df = pd.read_csv(r'C:\Masters-1st_Sem\Cloud_Computing\Project_2\NYPD_Arrests_Data__Historic.csv')
# drop the null values for Latitu and Longitude
df.dropna(axis=0,how='any',subset=['Latitude', 'Longitude'],inplace=True)
point_grid={}
#count the number of points in each cell in a loop and output them
for index, row in df.iterrows():
    for key in grid:
        values = grid[key]
        if (row["Latitude"] >= values[0] and row["Latitude"] <= values[2] and  row["Longitude"] >= values[1] and row["Longitude"] <= values[3]):
            if key in point_grid:            
                point_grid[key]+=1 #incrementing the points in each grid cell
            else:
                point_grid[key]=1  

for rect in rects:
    i, j = rect
    i = i[1: len(i) - 1]
    counts[i] = int(j.strip())

colors = {}

#assigning a colour for cells that match the range given below
for key in grid:
    coOr = grid[key] # values of x1, y1, x2, y2 assigned to a variable
    if key in counts:
        count = counts[key]
    else: count = 0
    if count < 87500:
        colors[key] = "green"
    elif count < 175000 and count >= 87500:
        colors[key] = "yellow"
    elif count < 262500 and count >= 175000:
        colors[key] = "orange"
    else: colors[key] = "red"
    SQL query row = (key, coOr[0], coOr[1], coOr[2], coOr[3], colors[key])
    print(key[4:])
    # inserting the values of the above output 
    conn.cursor.execute('INSERT INTO gridmap (rect_id, x1, y1, x2, y2, colour) values (%s, %s, %s, %s, %s, %s)' % (key[len(key) - 2:], coOr[0], coOr[2], coOr[1], coOr[3], colors[key]))
    for key in colors:
        print (key, ':', colors[key])

