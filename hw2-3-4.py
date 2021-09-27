# author : LM (AMDG) 09/23/2021
# population on Sept. 23, 2020 = 331,832,432
# one birth every 8 seconds 
# one death every 12 seconds
# one migrant every 645 seconds 

start = 331832432

seconds = 60

minute = 60

hour = 60

day = 24

year = 365

death = 12

immigrant = 645
new_pop = (seconds * minute * hour * day * year / 25 /death + start) + ( seconds + minute + hour + day / 25 / death ) +( minute + hour + day + year / immigrant)
print(" The population on September 24th 2021 is " + str(new_pop) + " people.")