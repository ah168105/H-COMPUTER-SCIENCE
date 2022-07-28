#### ---- INPUT ---- ####

social_media_followers = int(input("How many followers do you have on your favorite social media site? "))
followers_gained = int(input("How many followers do you gain per day? "))

#### ---- CALCULATIONS ---- ####

social_media_followers *= 2
followers_gained *= 365
social_media_followers += followers_gained


#### ---- OUTPUT ---- ####

print("In one month, your number of followers will be " + str(social_media_followers))
