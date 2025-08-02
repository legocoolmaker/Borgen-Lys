import random
seconds = 86400
cooldown = 115
cooldown_cost = 12
find_chance = 15
find_chance_cost = 45
double_find_chance = 2
double_find_chance_cost = 10

#
def simulate(total_time,cooldown,find_chance,double_find_chance):
  seconds_left = total_time
  finds = 0
  while seconds_left > 0:
    if random.randint(1,100) <= find_chance:
      finds += 1
      if random.randint(1,100) <= double_find_chance:
        finds += 1
    seconds_left -= cooldown
  return finds

total_finds_now = 0
for _ in range(10000):
  total_finds_now += simulate(seconds,cooldown,find_chance,double_find_chance)
total_finds_now /= 10000

total_finds_cooldown = 0
for _ in range(10000):
  total_finds_cooldown += simulate(seconds,cooldown-1,find_chance,double_find_chance)
total_finds_cooldown /= 10000

total_finds_chance = 0
for _ in range(10000):
  total_finds_chance += simulate(seconds,cooldown,find_chance+1,double_find_chance)
total_finds_chance /= 10000

total_finds_dblchance = 0
for _ in range(10000):
  total_finds_dblchance+= simulate(seconds,cooldown,find_chance,double_find_chance+1)
total_finds_dblchance /= 10000

print((total_finds_cooldown-total_finds_now)/cooldown_cost)
print((total_finds_chance-total_finds_now)/find_chance_cost)
print((total_finds_dblchance-total_finds_now)/double_find_chance_cost)




