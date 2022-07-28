#### ---- SETUP ---- ####

## -- Libraries -- ##
import random


## -- Variables -- ##
hero_name = 0
power_rating = 0
verb = 0
#### ---- RANDOMIZATION ---- ####

## -- First part of name -- ##
hero_name = random.randint(1,5)
if hero_name == 1:
    hero_name = "Captain"
elif hero_name == 2:
    hero_name = "Doctor"
elif hero_name == 3:
    hero_name = "Star"
elif hero_name == 4:
    hero_name = "Power"
else:
    hero_name = "The Human"
## -- Theme choice -- ##
power_theme = random.randint(1,8)
if 1 <= power_theme <= 2:
    verb = " Blaze"
    power_theme = "fire"
    power_rating += 3
if 3 <= power_theme <= 4:
    verb = " Tornado"
    power_theme = "wind"
    power_rating += 3
if 5 <= power_theme <= 6:
    verb = " Dolphin"
    power_theme = "water"
    power_rating += 3
if power_theme == 7:
    verb = " Spectre"
    power_theme = "ghosts"
    power_rating += 4
if power_theme == 8:
    verb = " Sparkle"
    power_theme = "light"
    power_rating += 2
## -- Power description -- ##
power_description = random.randint(1,10)
if power_description == 1:
    power_description = " can summon"
    power_rating += 4
if 2 <= power_description <= 4:
    power_description = " can turn into"
    power_rating += 3
if 5 <= power_description <= 7:
    power_description = "can shoot beams of"
if 8 <= power_description <= 10:
    power_description = "can talk to"
    power_rating += 1
## -- Extra power -- ##
extra_power = random.randint(1,2)
if extra_power == 1:
    extra_power = " "
elif extra_power == 2:
    extra_power = random.randint(3,5)
    if extra_power == 3:
        extra_power = "and is invincible"
        power_rating += 4
    elif extra_power == 4:
        extra_power = "and can stop time"
        power_rating += 3
    else:
        extra_power = "and is an expert hacker"
        power_rating += 2
#### ---- RESULTS ---- ####
print("SUPERHERO NAME: " + str(hero_name) + str(verb))
print(str(hero_name) + str(verb) + " " + str(power_description) + " " + str(power_theme) + " " + str(extra_power))
print("")
print("POWER RATING: " + str(power_rating))
