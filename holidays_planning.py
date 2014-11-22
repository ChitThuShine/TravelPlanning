import pyhop

plane_min_distance = 2000
taxi_max_distane = 500
ferry_max_distance = 2000

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

def ferry_rate(dist):
    return (400 + 3 * dist)

def plane_rate(dist):
    return (500 + 5 * dist)

def taxi_rate(dist):
    return (10 + 1.7 *dist)

def go_by_ferry(state, me, x, y):
    if state.loc[me] == x:
        state.loc[me] = y
        return state
    else: return False

def fly(state, me, x, y):
    if state.loc[me] == x:
        state.loc[me] = y
        return state
    else: return False

def call_taxi(state, me, x):
    state.loc['taxi'] = x
    return state

def ride_taxi(state, me, x, y):
    if state.loc['taxi']==x and state.loc[me]==x:
        state.loc['taxi'] = y
        state.loc[me] = y
        return state
    else: return False

def buy_ferry_ticket(state, me, own):
    if state.money[me] >= own:
        state.money[me] = state.money[me] - own
        return state
    return False

def buy_plane_ticket(state, me, own):
    if state.money[me] >= own:
        state.money[me] = state.money[me] - own
        return state
    return False

def pay_taxi_driver(state, me, own):
    if state.money[me] >= own:
        state.money[me] = state.money[me] - own
        return state
    return False

pyhop.declare_operators(
    fly,
    buy_plane_ticket,
    call_taxi,
    ride_taxi,
    pay_taxi_driver,
    buy_ferry_ticket,
    go_by_ferry)
print('')
pyhop.print_operators()

def travel_by_plane(state, me, x, y, pos):
    data = get_travel_data(state,pos)
    own = plane_rate(data['dist'])
    if state.money[me] >= own and data['dist'] >= plane_min_distance:
        if pos == len(places) - 2:
            return [('buy_plane_ticket', me, own), ('fly', me, data['from'], data['to'])]
        else:
            return [('buy_plane_ticket', me, own),
                    ('fly', me, data['from'], data['to']), 
                    ('travel', me, places[0], places[-1], pos + 1)]
    return False

def travel_by_taxi(state, me, x, y, pos):
    data = get_travel_data(state,pos)
    own = taxi_rate(data['dist'])
    if state.money[me] >= own and data['dist'] <= taxi_max_distane and not is_island_to(state0.not_island_to[data['from']], data['to']):
        if pos == len(places) - 2:
            return [('call_taxi', me, data['from']),
                    ('ride_taxi', me, data['from'], data['to']),
                    ('pay_taxi_driver', me, own)]
        else:
            return [('call_taxi', me, data['from']),
                    ('ride_taxi', me, data['from'], data['to']),
                    ('pay_taxi_driver', me, own),
                    ('travel', me, places[0], places[-1], pos + 1)]
    return False

def travel_by_ferry(state, me, x, y, pos):
    data = get_travel_data(state,pos)
    own = taxi_rate(data['dist'])
    if state.money[me] >= own and data['dist'] <= ferry_max_distance and is_island_to(state0.not_island_to[data['from']], data['to']):
        if pos == len(places) - 2:
            return [('buy_ferry_ticket', me, own),
                    ('go_by_ferry', me, data['from'], data['to'])]
        else:
            return [('buy_ferry_ticket', me, own),
                    ('go_by_ferry', me, data['from'], data['to']),
                    ('travel', me, places[0], places[-1], pos + 1)]
    return False

pyhop.declare_methods('travel', travel_by_plane, travel_by_taxi, travel_by_ferry)
print('')
pyhop.print_methods()

state0 = pyhop.State('state0')
state0.loc = { 'me' : 'Cracow' }
state0.money = { 'me' : 120000 }
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
state0.not_island_to = {
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

pyhop.pyhop(state0, [('travel', 'me', places[0], places[-1], 0 )], verbose = 3)
