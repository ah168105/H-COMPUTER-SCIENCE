#### ---- SETUP ---- ####

sites = {
  "apple.com": "17.253.144.10",
  "microsoft.com": "104.215.148.63",
  "google.com": "142.250.69.206",
  "techsmart.codes": "54.190.29.194",
  "wikipedia.org": "198.35.26.96",
  "gutenberg.org": "152.19.134.47",
  "youtube.com": "172.217.3.174",
  "amazon.com": "205.251.242.103",
  "yelp.com": "151.101.40.116",
  "ebay.com": "66.135.195.175",
  "instagram.com": "34.198.113.175",
  "imdb.com": "52.94.225.248"
}

user_url = input("Enter the url of the website you would like to go to: ")

#### ---- PARSING ---- ####

user_url = user_url.lower()
prefix_length = 0

if user_url[:8] == "https://":
    user_url = user_url[8:]

if user_url[:7] == "http://":
    user_url = user_url[7:]

if user_url[:4] == "www.":
    user_url = user_url[4:]

#### ---- OUTPUT ---- ####

if user_url in sites:
    print(sites[user_url])
else:
    print("Sorry, we do not have an IP for that URL.")
