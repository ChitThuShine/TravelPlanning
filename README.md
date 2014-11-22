Solving travel problem using python - pyhop.

Problem:

-I have to go for a holidays to Cuba from Cracow and visit 5 islands next to it and comeback home afterwards.

-I have some amount of cash and I should properly plan my spendings.

-I have to get a souvenir from every placeA

-I can buy souvenir (if I have enought money)

-I can also make photos as souvenirs but only a limited number

The order of places I have to visit:

```
places = [
    'Cracow',
    'Cracow-Airport',
    'Cayo Guilermo-Airport',
    'Cayo Guilermo', 
    'Long Island',
    'Crooked Island',
    'Mayaguana',
    'Rum Cay',
    'Cat Island',
    'Cat Island-Airport',
    'Cracow-Airport',
    'Cracow']
```

My current state:

location = Cracow
money = 150000
souvenirs bought = 0
souvenirs made = 0
photos available = 7

Distances (from google maps)

```
'Cracow' : { 'Cracow-Airport' : 20 },
'Cracow-Airport' : { 'Cayo Guilermo-Airport' :  7292.18, 'Cat Island-Airport' : 10063.81, 'Cracow' : 20 },
'Cayo Guilermo' : { 'Cayo Guilermo-Airport' :  20 , 'Long Island' : 2103.03 },
'Long Island' : { 'Cayo Guilermo' : 2103.03, 'Crooked Island' : 2020.21 },
'Crooked Island' : { 'Long Island' :  2020.21, 'Mayaguana' : 100.25 },
'Mayaguana' : { 'Crooked Island' : 100.25 , 'Rum Cay' : 230.31 },
'Rum Cay' : { 'Mayaguana' : 230.31, 'Cat Island' : 79.28 },
'Cat Island' : { 'Cat Island-Airport' : 20, 'Rum Cay' : 79.28 },
'Cat Island-Airport' : { 'Cracow-Airport' : 10063.81 },
'Cayo Guilermo-Airport' : { 'Cracow-Airport' : 7292.18, 'Cayo Guilermo' : 20 }
```

Structure to show if a place is not an island to another

```
'Cracow' : ['Cracow-Airport'],
'Cracow-Airport' : ['Cracow'],
'Cayo Guilermo' : [ 'Cayo Guilermo-Airport'],
'Long Island' : [],
'Crooked Island' : [],
'Mayaguana' : [],
'Rum Cay' : [],
'Cat Island' : [ 'Cat Island-Airport'],
'Cat Island-Airport' : [ 'Cat Island' ],
'Cayo Guilermo-Airport' : [ 'Cayo Guilermo' ]
```

Souvenirs prices

```
'Cracow' : 10,
'Cracow-Airport' : 20,
'Cayo Guilermo' : 100,
'Long Island' : 200,
'Crooked Island' : 160,
'Mayaguana' : 124,
'Rum Cay' : 700,
'Cat Island' : 125,
'Cat Island-Airport' : 679,
'Cayo Guilermo-Airport' : 778
```


Methods that show how much I have to pay for a transport

```
def ferry_rate(dist):
    return (400 + 3 * dist)

def plane_rate(dist):
    return (500 + 5 * dist)

def taxi_rate(dist):
    return (10 + 1.7 *dist)
```

I can travel by taxi, ferry or plane.

Important assumptions:

- I can go by taxi only if the distance is smaller than spcecified in settings
- I can go by taxi only if I do not move from island to island
- I can go by plan only if the distance is bigger than spcecified in settings
- I can go by ferry only if the distance is smaller than spcecified in settings
- I have to have enough cash to use chosen transport
