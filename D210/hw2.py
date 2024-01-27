import numpy
import pandas
import csv
from collections import Counter 
import numpy as np


def count_word(filename):
    words = []
    with open(filename, "r") as file: 
        for line in file: 
            for name in line.split():
                if(len(name.split()) > 1 ): 
                    for one in name.split():
                        words.append(one.lower())
                else:
                    words.append(name.lower())
        
    with open(filename, "w") as file: 
        word_c = Counter(sorted(words))
        print(sorted(word_c.most_common()) )
        for tuple in sorted(word_c.most_common()): 
            file.write(f"{tuple[0]}: {tuple[1]}\n")
           

    
def count_last_letter(words):
    letters = []
    for name in words.split():
        letters.append(name[len(name) - 1])
    lett_c = Counter(letters)
    d = {}
    for key, value in lett_c.items():
        d[key] = value
    return d

import numpy as np

def read_roster(filename):
    roster = np.zeros(4, dtype={'names': ('name', 'age', 'major', 'gpa'),
                         'formats': ('U50', 'i4', 'U4', 'f8')})
    print(type(roster))
    name = []
    age = [] 
    major = []
    gpa = []
    with open(filename) as file: 
        for line in file: 
            for i, attribue in enumerate(line.split(',')):
                match i:
                    case 0:
                        name.append(attribue)
                    case 1:
                        age.append(int(attribue))
                    case 2: 
                        major.append(attribue)
                    case 3:
                        gpa.append(float(attribue))
                    case _:
                        print("error")
        
        roster['name'] = name
        roster['age'] = age
        roster['major'] = major
        roster['gpa'] = gpa
        return roster

def compute_student_stats(roster): 
    
    print(numpy.average(roster['gpa'])) 

    numpy.max(roster['gpa'],axis= None, )


    maxCS_gpa = numpy.max(roster['gpa'][roster['major'] == 'CS'])
    print(maxCS_gpa)

    count = 0
    for gpa in roster['gpa']:
        if gpa > 3.5:
            count += 1
    print(count)

    avg_twentyFive = numpy.mean(roster['gpa'][roster['age' >= 25]])
    print(avg_twentyFive)


def read_ratings_data(f):
    ratings = {}

    with open(f) as file: 
        df = pandas.read_csv(file).drop(columns= ['1'])
        for i,x in zip(df['1.1'],df['4.0']):
            if(i not in ratings):
                ratings[i] = [x]
            else:
                ratings[i].append(x)
    return ratings

def read_movies_data(f):
    with open(f) as file:
        df = pandas.read_csv(f, sep ="|", names=["title", "year", "genre"]).sort_index()
        return df

movie_df = read_movies_data("D210/studentInfo.txt")


def create_genre(movies_df):
    
    genres = {}
    for genre in movies_df.genre:
        if(genre not in genres):
            genres[genre] = movies_df[movies_df.genre == genre].index.to_list()
    return genres

print(create_genre(movie_df))