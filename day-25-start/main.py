




# with open("day-25-start/weather_data.csv", "r") as file:
#     data = file.readlines()

# Rather than sort out csv file line by line, use an in built library to seperate table demographics 

import csv 

# with open("day-25-start/weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temps = [int(x) for row in data for count, x in enumerate(row) if x.isnumeric()]
    

import pandas

#DataFrame: The entire table makes up the data frame 
#Series: A series is a column within a data frame


data = pandas.read_csv("day-25-start/weather_data.csv")

#Getting  Data from the Columns (Returns a Series )

print(type(data))
print("This is the Dataframe of weather data \n")
print(data)

print(type(data["temp"] ) ) 
print( "\nThis is the Series of Tempreatures ")
print(data["temp"]) 

print( "\nConverted to a dictionary \n")

dict = data.to_dict()
print(dict)

print( "\nConverted to a List (Temp) \n")
temp_list = data["temp"].to_list()
print(temp_list)

print( "\nThe mean of temps. Got a hold of the column using -> data['temp'].mean() ")
print(data['temp'].mean()) 

print( "\nThe highest value within temp series. Got a hold of the column using -> data['temp'].max() ")

print(data["temp"].max()) 
 

#Getting Data from the Rows 
print( "\nGetting row of data where the Day is equal to monday. Returns a Dataframe. -> data[data.day == 'Monday']  ")
print(type(data[data.day == "Monday"]) )
print(data[data['day'] == "Monday"])
print("\n")

print( "\nChecking to see which row inside our column of tempreatures is equal to, 24, the max temp. Returns a Dataframe. -> data[data.temp == data['temp'].max()]  ")

print(data[data.temp == data["temp"].max()])

print("\nWhen we get our dataframe and use square brackets [], and inside the brackets if we\nonly put the name of a column **data['temp']**, then you would get the entire column.")
print("\nIf we filter that value by a condition data[**data.temp == data['temp'].max()**], say when a\ncolumn is equal to a particular value. Then we get hold of the row data. ")

print("\nGetting the condition colum from the dataframe of were the temp is the highest, 24.\nBefore the (.condition) it is a dataframe -> data[data.day == 'Monday'].condition or data[data.day == 'Monday']['condition'] ")
print(data[data.day == "Monday"]['condition'])


#Getting Monday Temp and Converting to Farenheight 
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
print(monday_temp)
ftemp = (monday_temp * 9/5 + 32)

"""

#Create DataFrame from stratch 
random_dict = {
        "Average": [0, 43, 23, 22, 21],
        "Exams": [ "Ex1", "Ex2", "Ex3", "Ex4", "Final"]
}

score_frame = pandas.DataFrame(random_dict)
print(score_frame)
"""




dataframe = pandas.read_csv('day-25-start/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

colors = dataframe['Primary Fur Color']
grayCount = len( dataframe[dataframe['Primary Fur Color'] == 'Gray'] ) 
print(grayCount)

cinnCount = len( dataframe[dataframe['Primary Fur Color'] == 'Cinnamon']) 
blackCount = len( dataframe[dataframe['Primary Fur Color'] == 'Black']) 


data_dict = {
        'qFur Color': ["Gray", "Cinnamon", "Black"],
        'Count':[grayCount, cinnCount, blackCount]
        }

color_stats = pandas.DataFrame(data_dict)
color_stats.to_csv("Squirrel Count") 



