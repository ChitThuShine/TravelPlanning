# Piotr Kala
#

# This module is used to run the planner
#

import pyhop

from holidays_travalling_helper import \
    go_by_ferry, \
    fly, \
    call_taxi, \
    ride_taxi, \
    buy_ferry_ticket, \
    buy_plane_ticket, \
    pay_taxi_driver, \
    travel_by_plane, \
    travel_by_ferry, \
    travel_by_taxi, \
    get_souvenir

from holidays_planner_data_helper import state0, places


pyhop.declare_operators(
    fly,
    buy_plane_ticket,
    call_taxi,
    ride_taxi,
    pay_taxi_driver,
    buy_ferry_ticket,
    go_by_ferry,
    get_souvenir)


print('')
pyhop.print_operators()


pyhop.declare_methods('travel', travel_by_plane, travel_by_taxi, travel_by_ferry)
print('')
pyhop.print_methods()

# Call
#
pyhop.pyhop(state0, [('travel', 'me', places[0], places[-1], 0)], verbose = 3)
