#### ---- SETUP ---- ####

# Numbers and names displayed aren't from real people, it's just random
import random

contacts = {
  "Lynn Muller": "(555) 876-9441",
  "Yating Tamm": "(555) 525-4745",
  "Dana Muhammadi": "(555) 767-3164",
  "Yin Garcia": "(555) 723-6909",
  "Caden Sato": "(555) 268-5382",
  "Lindsay Sok": "(555) 678-8832",
  "Sloan Manuel": "(555) 897-1950",
  "Shai Ali": "(555) 955-6864",
  "Yolotl Alaoui": "(555) 437-2313",
  "Gio Kone": "(555) 464-1038",
  "Yong Hernandez": "(555) 132-6859",
  "Yun-Seo Cohen": "(555) 685-4541",
  "Finley King": "(555) 147-7551",
  "Farah Kim": "(555) 730-9958",
  "Omer Ba": "(555) 677-4028",
  "Jess Lee": "(555) 317-3679",
  "Reese Muller": "(555) 341-2656",
  "Caden Garcia": "(555) 184-3130",
  "Danni Lee": "(555) 664-8113",
  "Quinn Sato": "(555) 566-2564"
}

#### ---- OUTPUT ---- ####

## -- Intro -- ##

print("Contacts List:")
print()

## -- Contacts -- ##

names = list(contacts.keys())
names.sort()
for name in names:
    print(name + ": " + contacts[name])
