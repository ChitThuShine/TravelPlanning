# Piotr Kala
#

from holidays_planner_data_helper import \
    is_island_to, \
    get_travel_data, \
    places, \
    plane_min_distance, \
    taxi_max_distane, \
    ferry_max_distance, \
    state0, \
    ferry_rate, \
    plane_rate, \
    taxi_rate, \
    souvenirs_prices, \
    souvenirs_money_rate, \
    not_island_to

# This module has methods and operations needed for travelling and geting souvenirs
#

# Sovenirs Methods
#

def get_souvenir(state, me, x):
    if state.money[me] / souvenirs_money_rate >= souvenirs_prices[x]:
        state.souvenirs_bought[me] = state.souvenirs_bought[me] + 1
        state.money[me] = state.money[me] - souvenirs_prices[x]
        return state
    elif state.photos_available[me] != 0:
        state.souvenirs_made[me] = state.souvenirs_made[me] + 1
        state.photos_available[me] = state.photos_available[me] - 1
        return state
    return False

# Travelling operations
#

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

# Travel Methods
#

def travel_by_plane(state, me, x, y, pos):
    data = get_travel_data(state,pos)
    own = plane_rate(data['dist'])
    if state.money[me] >= own and data['dist'] >= plane_min_distance:
        if pos == len(places) - 2:
            return [('get_souvenir', me, data['from']),
                    ('buy_plane_ticket', me, own), 
                    ('fly', me, data['from'], data['to'])]
        else:
            return [('get_souvenir', me, data['from']),
                    ('buy_plane_ticket', me, own),
                    ('fly', me, data['from'], data['to']),
                    ('travel', me, places[0], places[-1], pos + 1)]
    return False

def travel_by_taxi(state, me, x, y, pos):
    data = get_travel_data(state,pos)
    own = taxi_rate(data['dist'])
    if state.money[me] >= own and \
        data['dist'] <= taxi_max_distane and \
        not is_island_to(not_island_to[data['from']], data['to']):
        if pos == len(places) - 2:
            return [('get_souvenir', me, data['from']),
                    ('call_taxi', me, data['from']),
                    ('ride_taxi', me, data['from'], data['to']),
                    ('pay_taxi_driver', me, own)]
        else:
            return [('get_souvenir', me, data['from']),
                    ('call_taxi', me, data['from']),
                    ('ride_taxi', me, data['from'], data['to']),
                    ('pay_taxi_driver', me, own),
                    ('travel', me, places[0], places[-1], pos + 1)]
    return False

def travel_by_ferry(state, me, x, y, pos):
    data = get_travel_data(state,pos)
    own = taxi_rate(data['dist'])
    if state.money[me] >= own and \
        data['dist'] <= ferry_max_distance and \
        is_island_to(not_island_to[data['from']], data['to']):
        if pos == len(places) - 2:
            return [('get_souvenir', me, data['from']),
                    ('buy_ferry_ticket', me, own),
                    ('go_by_ferry', me, data['from'], data['to'])]
        else:
            return [('get_souvenir', me, data['from']),
                    ('buy_ferry_ticket', me, own),
                    ('go_by_ferry', me, data['from'], data['to']),
                    ('travel', me, places[0], places[-1], pos + 1)]
    return False
