import pyhop
from holidays_planner_helper import \
    is_island_to, \
    get_travel_data, \
    places, \
    plane_min_distance, \
    taxi_max_distane, \
    ferry_max_distance, \
    state0, \
    ferry_rate, \
    plane_rate, \
    taxi_rate


#Operators
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

#Travel Methods
#

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

#Call
#

pyhop.pyhop(state0, [('travel', 'me', places[0], places[-1], 0 )], verbose = 2)
