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

![Alt text](http://s30.postimg.org/77jmpjh81/msi.png)

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

Example output:

```
OPERATORS: fly, buy_ferry_ticket, pay_taxi_driver, ride_taxi, go_by_ferry, call_taxi, buy_plane_ticket, get_souvenir

TASK:         METHODS:
travel        travel_by_plane, travel_by_taxi, travel_by_ferry
** pyhop, verbose=3: **
   state = state0
   tasks = [('travel', 'me', 'Cracow', 'Cracow', 0)]
depth 0 tasks [('travel', 'me', 'Cracow', 'Cracow', 0)]
depth 0 method instance ('travel', 'me', 'Cracow', 'Cracow', 0)
depth 0 new tasks: False
depth 0 new tasks: [('get_souvenir', 'me', 'Cracow'), ('call_taxi', 'me', 'Cracow'), ('ride_taxi', 'me', 'Cracow', 'Cracow-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 1)]
depth 1 tasks [('get_souvenir', 'me', 'Cracow'), ('call_taxi', 'me', 'Cracow'), ('ride_taxi', 'me', 'Cracow', 'Cracow-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 1)]
depth 1 action ('get_souvenir', 'me', 'Cracow')
depth 1 new state:
    state0.souvenirs_made = {'me': 0}
    state0.loc = {'me': 'Cracow'}
    state0.souvenirs_bought = {'me': 1}
    state0.photos_available = {'me': 7}
    state0.money = {'me': 149990}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 2 tasks [('call_taxi', 'me', 'Cracow'), ('ride_taxi', 'me', 'Cracow', 'Cracow-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 1)]
depth 2 action ('call_taxi', 'me', 'Cracow')
depth 2 new state:
    state0.souvenirs_made = {'me': 0}
    state0.loc = {'me': 'Cracow', 'taxi': 'Cracow'}
    state0.souvenirs_bought = {'me': 1}
    state0.photos_available = {'me': 7}
    state0.money = {'me': 149990}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 3 tasks [('ride_taxi', 'me', 'Cracow', 'Cracow-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 1)]
depth 3 action ('ride_taxi', 'me', 'Cracow', 'Cracow-Airport')
depth 3 new state:
    state0.souvenirs_made = {'me': 0}
    state0.loc = {'me': 'Cracow-Airport', 'taxi': 'Cracow-Airport'}
    state0.souvenirs_bought = {'me': 1}
    state0.photos_available = {'me': 7}
    state0.money = {'me': 149990}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 4 tasks [('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 1)]
depth 4 action ('pay_taxi_driver', 'me', 44.0)
depth 4 new state:
    state0.souvenirs_made = {'me': 0}
    state0.loc = {'me': 'Cracow-Airport', 'taxi': 'Cracow-Airport'}
    state0.souvenirs_bought = {'me': 1}
    state0.photos_available = {'me': 7}
    state0.money = {'me': 149946.0}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 5 tasks [('travel', 'me', 'Cracow', 'Cracow', 1)]
depth 5 method instance ('travel', 'me', 'Cracow', 'Cracow', 1)
depth 5 new tasks: [('get_souvenir', 'me', 'Cracow-Airport'), ('buy_plane_ticket', 'me', 36960.9), ('fly', 'me', 'Cracow-Airport', 'Cayo Guilermo-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 2)]
depth 6 tasks [('get_souvenir', 'me', 'Cracow-Airport'), ('buy_plane_ticket', 'me', 36960.9), ('fly', 'me', 'Cracow-Airport', 'Cayo Guilermo-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 2)]
depth 6 action ('get_souvenir', 'me', 'Cracow-Airport')
depth 6 new state:
    state0.souvenirs_made = {'me': 0}
    state0.loc = {'me': 'Cracow-Airport', 'taxi': 'Cracow-Airport'}
    state0.souvenirs_bought = {'me': 2}
    state0.photos_available = {'me': 7}
    state0.money = {'me': 149926.0}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 7 tasks [('buy_plane_ticket', 'me', 36960.9), ('fly', 'me', 'Cracow-Airport', 'Cayo Guilermo-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 2)]
depth 7 action ('buy_plane_ticket', 'me', 36960.9)
depth 7 new state:
    state0.souvenirs_made = {'me': 0}
    state0.loc = {'me': 'Cracow-Airport', 'taxi': 'Cracow-Airport'}
    state0.souvenirs_bought = {'me': 2}
    state0.photos_available = {'me': 7}
    state0.money = {'me': 112965.1}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 8 tasks [('fly', 'me', 'Cracow-Airport', 'Cayo Guilermo-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 2)]
depth 8 action ('fly', 'me', 'Cracow-Airport', 'Cayo Guilermo-Airport')
depth 8 new state:
    state0.souvenirs_made = {'me': 0}
    state0.loc = {'me': 'Cayo Guilermo-Airport', 'taxi': 'Cracow-Airport'}
    state0.souvenirs_bought = {'me': 2}
    state0.photos_available = {'me': 7}
    state0.money = {'me': 112965.1}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 9 tasks [('travel', 'me', 'Cracow', 'Cracow', 2)]
depth 9 method instance ('travel', 'me', 'Cracow', 'Cracow', 2)
depth 9 new tasks: False
depth 9 new tasks: [('get_souvenir', 'me', 'Cayo Guilermo-Airport'), ('call_taxi', 'me', 'Cayo Guilermo-Airport'), ('ride_taxi', 'me', 'Cayo Guilermo-Airport', 'Cayo Guilermo'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 3)]
depth 10 tasks [('get_souvenir', 'me', 'Cayo Guilermo-Airport'), ('call_taxi', 'me', 'Cayo Guilermo-Airport'), ('ride_taxi', 'me', 'Cayo Guilermo-Airport', 'Cayo Guilermo'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 3)]
depth 10 action ('get_souvenir', 'me', 'Cayo Guilermo-Airport')
depth 10 new state:
    state0.souvenirs_made = {'me': 1}
    state0.loc = {'me': 'Cayo Guilermo-Airport', 'taxi': 'Cracow-Airport'}
    state0.souvenirs_bought = {'me': 2}
    state0.photos_available = {'me': 6}
    state0.money = {'me': 112965.1}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 11 tasks [('call_taxi', 'me', 'Cayo Guilermo-Airport'), ('ride_taxi', 'me', 'Cayo Guilermo-Airport', 'Cayo Guilermo'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 3)]
depth 11 action ('call_taxi', 'me', 'Cayo Guilermo-Airport')
depth 11 new state:
    state0.souvenirs_made = {'me': 1}
    state0.loc = {'me': 'Cayo Guilermo-Airport', 'taxi': 'Cayo Guilermo-Airport'}
    state0.souvenirs_bought = {'me': 2}
    state0.photos_available = {'me': 6}
    state0.money = {'me': 112965.1}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 12 tasks [('ride_taxi', 'me', 'Cayo Guilermo-Airport', 'Cayo Guilermo'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 3)]
depth 12 action ('ride_taxi', 'me', 'Cayo Guilermo-Airport', 'Cayo Guilermo')
depth 12 new state:
    state0.souvenirs_made = {'me': 1}
    state0.loc = {'me': 'Cayo Guilermo', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 2}
    state0.photos_available = {'me': 6}
    state0.money = {'me': 112965.1}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 13 tasks [('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 3)]
depth 13 action ('pay_taxi_driver', 'me', 44.0)
depth 13 new state:
    state0.souvenirs_made = {'me': 1}
    state0.loc = {'me': 'Cayo Guilermo', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 2}
    state0.photos_available = {'me': 6}
    state0.money = {'me': 112921.1}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 14 tasks [('travel', 'me', 'Cracow', 'Cracow', 3)]
depth 14 method instance ('travel', 'me', 'Cracow', 'Cracow', 3)
depth 14 new tasks: [('get_souvenir', 'me', 'Cayo Guilermo'), ('buy_plane_ticket', 'me', 11015.150000000001), ('fly', 'me', 'Cayo Guilermo', 'Long Island'), ('travel', 'me', 'Cracow', 'Cracow', 4)]
depth 15 tasks [('get_souvenir', 'me', 'Cayo Guilermo'), ('buy_plane_ticket', 'me', 11015.150000000001), ('fly', 'me', 'Cayo Guilermo', 'Long Island'), ('travel', 'me', 'Cracow', 'Cracow', 4)]
depth 15 action ('get_souvenir', 'me', 'Cayo Guilermo')
depth 15 new state:
    state0.souvenirs_made = {'me': 1}
    state0.loc = {'me': 'Cayo Guilermo', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 6}
    state0.money = {'me': 112821.1}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 16 tasks [('buy_plane_ticket', 'me', 11015.150000000001), ('fly', 'me', 'Cayo Guilermo', 'Long Island'), ('travel', 'me', 'Cracow', 'Cracow', 4)]
depth 16 action ('buy_plane_ticket', 'me', 11015.150000000001)
depth 16 new state:
    state0.souvenirs_made = {'me': 1}
    state0.loc = {'me': 'Cayo Guilermo', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 6}
    state0.money = {'me': 101805.95000000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 17 tasks [('fly', 'me', 'Cayo Guilermo', 'Long Island'), ('travel', 'me', 'Cracow', 'Cracow', 4)]
depth 17 action ('fly', 'me', 'Cayo Guilermo', 'Long Island')
depth 17 new state:
    state0.souvenirs_made = {'me': 1}
    state0.loc = {'me': 'Long Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 6}
    state0.money = {'me': 101805.95000000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 18 tasks [('travel', 'me', 'Cracow', 'Cracow', 4)]
depth 18 method instance ('travel', 'me', 'Cracow', 'Cracow', 4)
depth 18 new tasks: [('get_souvenir', 'me', 'Long Island'), ('buy_plane_ticket', 'me', 10601.05), ('fly', 'me', 'Long Island', 'Crooked Island'), ('travel', 'me', 'Cracow', 'Cracow', 5)]
depth 19 tasks [('get_souvenir', 'me', 'Long Island'), ('buy_plane_ticket', 'me', 10601.05), ('fly', 'me', 'Long Island', 'Crooked Island'), ('travel', 'me', 'Cracow', 'Cracow', 5)]
depth 19 action ('get_souvenir', 'me', 'Long Island')
depth 19 new state:
    state0.souvenirs_made = {'me': 2}
    state0.loc = {'me': 'Long Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 5}
    state0.money = {'me': 101805.95000000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 20 tasks [('buy_plane_ticket', 'me', 10601.05), ('fly', 'me', 'Long Island', 'Crooked Island'), ('travel', 'me', 'Cracow', 'Cracow', 5)]
depth 20 action ('buy_plane_ticket', 'me', 10601.05)
depth 20 new state:
    state0.souvenirs_made = {'me': 2}
    state0.loc = {'me': 'Long Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 5}
    state0.money = {'me': 91204.90000000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 21 tasks [('fly', 'me', 'Long Island', 'Crooked Island'), ('travel', 'me', 'Cracow', 'Cracow', 5)]
depth 21 action ('fly', 'me', 'Long Island', 'Crooked Island')
depth 21 new state:
    state0.souvenirs_made = {'me': 2}
    state0.loc = {'me': 'Crooked Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 5}
    state0.money = {'me': 91204.90000000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 22 tasks [('travel', 'me', 'Cracow', 'Cracow', 5)]
depth 22 method instance ('travel', 'me', 'Cracow', 'Cracow', 5)
depth 22 new tasks: False
depth 22 new tasks: False
depth 22 new tasks: [('get_souvenir', 'me', 'Crooked Island'), ('buy_ferry_ticket', 'me', 180.42499999999998), ('go_by_ferry', 'me', 'Crooked Island', 'Mayaguana'), ('travel', 'me', 'Cracow', 'Cracow', 6)]
depth 23 tasks [('get_souvenir', 'me', 'Crooked Island'), ('buy_ferry_ticket', 'me', 180.42499999999998), ('go_by_ferry', 'me', 'Crooked Island', 'Mayaguana'), ('travel', 'me', 'Cracow', 'Cracow', 6)]
depth 23 action ('get_souvenir', 'me', 'Crooked Island')
depth 23 new state:
    state0.souvenirs_made = {'me': 3}
    state0.loc = {'me': 'Crooked Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 4}
    state0.money = {'me': 91204.90000000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 24 tasks [('buy_ferry_ticket', 'me', 180.42499999999998), ('go_by_ferry', 'me', 'Crooked Island', 'Mayaguana'), ('travel', 'me', 'Cracow', 'Cracow', 6)]
depth 24 action ('buy_ferry_ticket', 'me', 180.42499999999998)
depth 24 new state:
    state0.souvenirs_made = {'me': 3}
    state0.loc = {'me': 'Crooked Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 4}
    state0.money = {'me': 91024.475}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 25 tasks [('go_by_ferry', 'me', 'Crooked Island', 'Mayaguana'), ('travel', 'me', 'Cracow', 'Cracow', 6)]
depth 25 action ('go_by_ferry', 'me', 'Crooked Island', 'Mayaguana')
depth 25 new state:
    state0.souvenirs_made = {'me': 3}
    state0.loc = {'me': 'Mayaguana', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 4}
    state0.money = {'me': 91024.475}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 26 tasks [('travel', 'me', 'Cracow', 'Cracow', 6)]
depth 26 method instance ('travel', 'me', 'Cracow', 'Cracow', 6)
depth 26 new tasks: False
depth 26 new tasks: False
depth 26 new tasks: [('get_souvenir', 'me', 'Mayaguana'), ('buy_ferry_ticket', 'me', 401.527), ('go_by_ferry', 'me', 'Mayaguana', 'Rum Cay'), ('travel', 'me', 'Cracow', 'Cracow', 7)]
depth 27 tasks [('get_souvenir', 'me', 'Mayaguana'), ('buy_ferry_ticket', 'me', 401.527), ('go_by_ferry', 'me', 'Mayaguana', 'Rum Cay'), ('travel', 'me', 'Cracow', 'Cracow', 7)]
depth 27 action ('get_souvenir', 'me', 'Mayaguana')
depth 27 new state:
    state0.souvenirs_made = {'me': 4}
    state0.loc = {'me': 'Mayaguana', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 3}
    state0.money = {'me': 91024.475}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 28 tasks [('buy_ferry_ticket', 'me', 401.527), ('go_by_ferry', 'me', 'Mayaguana', 'Rum Cay'), ('travel', 'me', 'Cracow', 'Cracow', 7)]
depth 28 action ('buy_ferry_ticket', 'me', 401.527)
depth 28 new state:
    state0.souvenirs_made = {'me': 4}
    state0.loc = {'me': 'Mayaguana', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 3}
    state0.money = {'me': 90622.948}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 29 tasks [('go_by_ferry', 'me', 'Mayaguana', 'Rum Cay'), ('travel', 'me', 'Cracow', 'Cracow', 7)]
depth 29 action ('go_by_ferry', 'me', 'Mayaguana', 'Rum Cay')
depth 29 new state:
    state0.souvenirs_made = {'me': 4}
    state0.loc = {'me': 'Rum Cay', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 3}
    state0.money = {'me': 90622.948}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 30 tasks [('travel', 'me', 'Cracow', 'Cracow', 7)]
depth 30 method instance ('travel', 'me', 'Cracow', 'Cracow', 7)
depth 30 new tasks: False
depth 30 new tasks: False
depth 30 new tasks: [('get_souvenir', 'me', 'Rum Cay'), ('buy_ferry_ticket', 'me', 144.776), ('go_by_ferry', 'me', 'Rum Cay', 'Cat Island'), ('travel', 'me', 'Cracow', 'Cracow', 8)]
depth 31 tasks [('get_souvenir', 'me', 'Rum Cay'), ('buy_ferry_ticket', 'me', 144.776), ('go_by_ferry', 'me', 'Rum Cay', 'Cat Island'), ('travel', 'me', 'Cracow', 'Cracow', 8)]
depth 31 action ('get_souvenir', 'me', 'Rum Cay')
depth 31 new state:
    state0.souvenirs_made = {'me': 5}
    state0.loc = {'me': 'Rum Cay', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 2}
    state0.money = {'me': 90622.948}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 32 tasks [('buy_ferry_ticket', 'me', 144.776), ('go_by_ferry', 'me', 'Rum Cay', 'Cat Island'), ('travel', 'me', 'Cracow', 'Cracow', 8)]
depth 32 action ('buy_ferry_ticket', 'me', 144.776)
depth 32 new state:
    state0.souvenirs_made = {'me': 5}
    state0.loc = {'me': 'Rum Cay', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 2}
    state0.money = {'me': 90478.172}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 33 tasks [('go_by_ferry', 'me', 'Rum Cay', 'Cat Island'), ('travel', 'me', 'Cracow', 'Cracow', 8)]
depth 33 action ('go_by_ferry', 'me', 'Rum Cay', 'Cat Island')
depth 33 new state:
    state0.souvenirs_made = {'me': 5}
    state0.loc = {'me': 'Cat Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 2}
    state0.money = {'me': 90478.172}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 34 tasks [('travel', 'me', 'Cracow', 'Cracow', 8)]
depth 34 method instance ('travel', 'me', 'Cracow', 'Cracow', 8)
depth 34 new tasks: False
depth 34 new tasks: [('get_souvenir', 'me', 'Cat Island'), ('call_taxi', 'me', 'Cat Island'), ('ride_taxi', 'me', 'Cat Island', 'Cat Island-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 9)]
depth 35 tasks [('get_souvenir', 'me', 'Cat Island'), ('call_taxi', 'me', 'Cat Island'), ('ride_taxi', 'me', 'Cat Island', 'Cat Island-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 9)]
depth 35 action ('get_souvenir', 'me', 'Cat Island')
depth 35 new state:
    state0.souvenirs_made = {'me': 6}
    state0.loc = {'me': 'Cat Island', 'taxi': 'Cayo Guilermo'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 1}
    state0.money = {'me': 90478.172}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 36 tasks [('call_taxi', 'me', 'Cat Island'), ('ride_taxi', 'me', 'Cat Island', 'Cat Island-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 9)]
depth 36 action ('call_taxi', 'me', 'Cat Island')
depth 36 new state:
    state0.souvenirs_made = {'me': 6}
    state0.loc = {'me': 'Cat Island', 'taxi': 'Cat Island'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 1}
    state0.money = {'me': 90478.172}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 37 tasks [('ride_taxi', 'me', 'Cat Island', 'Cat Island-Airport'), ('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 9)]
depth 37 action ('ride_taxi', 'me', 'Cat Island', 'Cat Island-Airport')
depth 37 new state:
    state0.souvenirs_made = {'me': 6}
    state0.loc = {'me': 'Cat Island-Airport', 'taxi': 'Cat Island-Airport'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 1}
    state0.money = {'me': 90478.172}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 38 tasks [('pay_taxi_driver', 'me', 44.0), ('travel', 'me', 'Cracow', 'Cracow', 9)]
depth 38 action ('pay_taxi_driver', 'me', 44.0)
depth 38 new state:
    state0.souvenirs_made = {'me': 6}
    state0.loc = {'me': 'Cat Island-Airport', 'taxi': 'Cat Island-Airport'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 1}
    state0.money = {'me': 90434.172}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 39 tasks [('travel', 'me', 'Cracow', 'Cracow', 9)]
depth 39 method instance ('travel', 'me', 'Cracow', 'Cracow', 9)
depth 39 new tasks: [('get_souvenir', 'me', 'Cat Island-Airport'), ('buy_plane_ticket', 'me', 50819.049999999996), ('fly', 'me', 'Cat Island-Airport', 'Cracow-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 10)]
depth 40 tasks [('get_souvenir', 'me', 'Cat Island-Airport'), ('buy_plane_ticket', 'me', 50819.049999999996), ('fly', 'me', 'Cat Island-Airport', 'Cracow-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 10)]
depth 40 action ('get_souvenir', 'me', 'Cat Island-Airport')
depth 40 new state:
    state0.souvenirs_made = {'me': 7}
    state0.loc = {'me': 'Cat Island-Airport', 'taxi': 'Cat Island-Airport'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 0}
    state0.money = {'me': 90434.172}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 41 tasks [('buy_plane_ticket', 'me', 50819.049999999996), ('fly', 'me', 'Cat Island-Airport', 'Cracow-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 10)]
depth 41 action ('buy_plane_ticket', 'me', 50819.049999999996)
depth 41 new state:
    state0.souvenirs_made = {'me': 7}
    state0.loc = {'me': 'Cat Island-Airport', 'taxi': 'Cat Island-Airport'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 0}
    state0.money = {'me': 39615.12200000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 42 tasks [('fly', 'me', 'Cat Island-Airport', 'Cracow-Airport'), ('travel', 'me', 'Cracow', 'Cracow', 10)]
depth 42 action ('fly', 'me', 'Cat Island-Airport', 'Cracow-Airport')
depth 42 new state:
    state0.souvenirs_made = {'me': 7}
    state0.loc = {'me': 'Cracow-Airport', 'taxi': 'Cat Island-Airport'}
    state0.souvenirs_bought = {'me': 3}
    state0.photos_available = {'me': 0}
    state0.money = {'me': 39615.12200000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 43 tasks [('travel', 'me', 'Cracow', 'Cracow', 10)]
depth 43 method instance ('travel', 'me', 'Cracow', 'Cracow', 10)
depth 43 new tasks: False
depth 43 new tasks: [('get_souvenir', 'me', 'Cracow-Airport'), ('call_taxi', 'me', 'Cracow-Airport'), ('ride_taxi', 'me', 'Cracow-Airport', 'Cracow'), ('pay_taxi_driver', 'me', 44.0)]
depth 44 tasks [('get_souvenir', 'me', 'Cracow-Airport'), ('call_taxi', 'me', 'Cracow-Airport'), ('ride_taxi', 'me', 'Cracow-Airport', 'Cracow'), ('pay_taxi_driver', 'me', 44.0)]
depth 44 action ('get_souvenir', 'me', 'Cracow-Airport')
depth 44 new state:
    state0.souvenirs_made = {'me': 7}
    state0.loc = {'me': 'Cracow-Airport', 'taxi': 'Cat Island-Airport'}
    state0.souvenirs_bought = {'me': 4}
    state0.photos_available = {'me': 0}
    state0.money = {'me': 39595.12200000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 45 tasks [('call_taxi', 'me', 'Cracow-Airport'), ('ride_taxi', 'me', 'Cracow-Airport', 'Cracow'), ('pay_taxi_driver', 'me', 44.0)]
depth 45 action ('call_taxi', 'me', 'Cracow-Airport')
depth 45 new state:
    state0.souvenirs_made = {'me': 7}
    state0.loc = {'me': 'Cracow-Airport', 'taxi': 'Cracow-Airport'}
    state0.souvenirs_bought = {'me': 4}
    state0.photos_available = {'me': 0}
    state0.money = {'me': 39595.12200000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 46 tasks [('ride_taxi', 'me', 'Cracow-Airport', 'Cracow'), ('pay_taxi_driver', 'me', 44.0)]
depth 46 action ('ride_taxi', 'me', 'Cracow-Airport', 'Cracow')
depth 46 new state:
    state0.souvenirs_made = {'me': 7}
    state0.loc = {'me': 'Cracow', 'taxi': 'Cracow'}
    state0.souvenirs_bought = {'me': 4}
    state0.photos_available = {'me': 0}
    state0.money = {'me': 39595.12200000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 47 tasks [('pay_taxi_driver', 'me', 44.0)]
depth 47 action ('pay_taxi_driver', 'me', 44.0)
depth 47 new state:
    state0.souvenirs_made = {'me': 7}
    state0.loc = {'me': 'Cracow', 'taxi': 'Cracow'}
    state0.souvenirs_bought = {'me': 4}
    state0.photos_available = {'me': 0}
    state0.money = {'me': 39551.12200000001}
    state0.dist = {'Rum Cay': {'Cat Island': 79.28, 'Mayaguana': 230.31}, 'Cracow-Airport': {'Cayo Guilermo-Airport': 7292.18, 'Cat Island-Airport': 10063.81, 'Cracow': 20}, 'Long Island': {'Crooked Island': 2020.21, 'Cayo Guilermo': 2103.03}, 'Mayaguana': {'Rum Cay': 230.31, 'Crooked Island': 100.25}, 'Cat Island': {'Rum Cay': 79.28, 'Cat Island-Airport': 20}, 'Cracow': {'Cracow-Airport': 20}, 'Cayo Guilermo-Airport': {'Cracow-Airport': 7292.18, 'Cayo Guilermo': 20}, 'Cat Island-Airport': {'Cracow-Airport': 10063.81}, 'Crooked Island': {'Long Island': 2020.21, 'Mayaguana': 100.25}, 'Cayo Guilermo': {'Cayo Guilermo-Airport': 20, 'Long Island': 2103.03}}
depth 48 tasks []
depth 48 returns plan [('get_souvenir', 'me', 'Cracow'), ('call_taxi', 'me', 'Cracow'), ('ride_taxi', 'me', 'Cracow', 'Cracow-Airport'), ('pay_taxi_driver', 'me', 44.0), ('get_souvenir', 'me', 'Cracow-Airport'), ('buy_plane_ticket', 'me', 36960.9), ('fly', 'me', 'Cracow-Airport', 'Cayo Guilermo-Airport'), ('get_souvenir', 'me', 'Cayo Guilermo-Airport'), ('call_taxi', 'me', 'Cayo Guilermo-Airport'), ('ride_taxi', 'me', 'Cayo Guilermo-Airport', 'Cayo Guilermo'), ('pay_taxi_driver', 'me', 44.0), ('get_souvenir', 'me', 'Cayo Guilermo'), ('buy_plane_ticket', 'me', 11015.150000000001), ('fly', 'me', 'Cayo Guilermo', 'Long Island'), ('get_souvenir', 'me', 'Long Island'), ('buy_plane_ticket', 'me', 10601.05), ('fly', 'me', 'Long Island', 'Crooked Island'), ('get_souvenir', 'me', 'Crooked Island'), ('buy_ferry_ticket', 'me', 180.42499999999998), ('go_by_ferry', 'me', 'Crooked Island', 'Mayaguana'), ('get_souvenir', 'me', 'Mayaguana'), ('buy_ferry_ticket', 'me', 401.527), ('go_by_ferry', 'me', 'Mayaguana', 'Rum Cay'), ('get_souvenir', 'me', 'Rum Cay'), ('buy_ferry_ticket', 'me', 144.776), ('go_by_ferry', 'me', 'Rum Cay', 'Cat Island'), ('get_souvenir', 'me', 'Cat Island'), ('call_taxi', 'me', 'Cat Island'), ('ride_taxi', 'me', 'Cat Island', 'Cat Island-Airport'), ('pay_taxi_driver', 'me', 44.0), ('get_souvenir', 'me', 'Cat Island-Airport'), ('buy_plane_ticket', 'me', 50819.049999999996), ('fly', 'me', 'Cat Island-Airport', 'Cracow-Airport'), ('get_souvenir', 'me', 'Cracow-Airport'), ('call_taxi', 'me', 'Cracow-Airport'), ('ride_taxi', 'me', 'Cracow-Airport', 'Cracow'), ('pay_taxi_driver', 'me', 44.0)]
** result = [('get_souvenir', 'me', 'Cracow'), ('call_taxi', 'me', 'Cracow'), ('ride_taxi', 'me', 'Cracow', 'Cracow-Airport'), ('pay_taxi_driver', 'me', 44.0), ('get_souvenir', 'me', 'Cracow-Airport'), ('buy_plane_ticket', 'me', 36960.9), ('fly', 'me', 'Cracow-Airport', 'Cayo Guilermo-Airport'), ('get_souvenir', 'me', 'Cayo Guilermo-Airport'), ('call_taxi', 'me', 'Cayo Guilermo-Airport'), ('ride_taxi', 'me', 'Cayo Guilermo-Airport', 'Cayo Guilermo'), ('pay_taxi_driver', 'me', 44.0), ('get_souvenir', 'me', 'Cayo Guilermo'), ('buy_plane_ticket', 'me', 11015.150000000001), ('fly', 'me', 'Cayo Guilermo', 'Long Island'), ('get_souvenir', 'me', 'Long Island'), ('buy_plane_ticket', 'me', 10601.05), ('fly', 'me', 'Long Island', 'Crooked Island'), ('get_souvenir', 'me', 'Crooked Island'), ('buy_ferry_ticket', 'me', 180.42499999999998), ('go_by_ferry', 'me', 'Crooked Island', 'Mayaguana'), ('get_souvenir', 'me', 'Mayaguana'), ('buy_ferry_ticket', 'me', 401.527), ('go_by_ferry', 'me', 'Mayaguana', 'Rum Cay'), ('get_souvenir', 'me', 'Rum Cay'), ('buy_ferry_ticket', 'me', 144.776), ('go_by_ferry', 'me', 'Rum Cay', 'Cat Island'), ('get_souvenir', 'me', 'Cat Island'), ('call_taxi', 'me', 'Cat Island'), ('ride_taxi', 'me', 'Cat Island', 'Cat Island-Airport'), ('pay_taxi_driver', 'me', 44.0), ('get_souvenir', 'me', 'Cat Island-Airport'), ('buy_plane_ticket', 'me', 50819.049999999996), ('fly', 'me', 'Cat Island-Airport', 'Cracow-Airport'), ('get_souvenir', 'me', 'Cracow-Airport'), ('call_taxi', 'me', 'Cracow-Airport'), ('ride_taxi', 'me', 'Cracow-Airport', 'Cracow'), ('pay_taxi_driver', 'me', 44.0)] 

```
