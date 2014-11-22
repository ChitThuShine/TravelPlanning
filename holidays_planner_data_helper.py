# Piotr Kala
#

# This module includes helper methods and data
#

import pyhop

plane_min_distance = 2000
taxi_max_distane = 500
ferry_max_distance = 2000
souvenirs_money_rate = 1000

def ferry_rate(dist):
    return (400 + 3 * dist)

def plane_rate(dist):
    return (500 + 5 * dist)

def taxi_rate(dist):
    return (10 + 1.7 *dist)

def is_island_to(place_A_list , place_B_key):
    for x in place_A_list:
        if x == place_B_key:
            return False
    return True

def get_travel_data(state, pos):
    x = places[pos]
    y = places[pos + 1]
    data = { 
        'from' : x,
        'to' : y,
        'dist' : state.dist[x][y] }
    return data

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

state0 = pyhop.State('state0')
state0.loc = { 'me' : 'Cracow' }
state0.money = { 'me' : 150000 }
state0.souvenirs_bought = { 'me' : 0 }
state0.souvenirs_made = { 'me' : 0 }
state0.photos_available = { 'me' : 7 }
state0.dist = { 
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
    }
not_island_to = {
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
    }
souvenirs_prices = {
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
    }
