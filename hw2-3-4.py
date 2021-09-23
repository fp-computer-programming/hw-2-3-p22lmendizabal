# author : LM (AMDG) 09/23/2021
# population on Sept. 23, 2020 = 331,832,432
# one birth every 8 seconds 
# one death every 12 seconds
# one migrant every 645 seconds 

start = 331,832,432

hour = 60

minute = 60

day = 24

year = 365



birth_one_year = (minute /8 * hour * day * year) + (minute/8 * hour * day)
print(birth_one_year)