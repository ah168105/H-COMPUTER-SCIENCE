#### Credit: Art created by jgs at https://www.asciiart.eu/art-and-design/mona-lisa


#### ---- SETUP ---- ####

## -- List -- ##

lines = ["", "       ______", "     .;;;;;;;;.", "    /;;;;;;;;;;;\\", "   /;/`    `-;;;;; . .", "   |;|__  __  \\;;;|", ".-.|;| e`/e`  |;;;|", "   |;|  |     |;;;|'--", "   |;|  '-    |;;;|", "   |;;\\ --'  /|;;;|", "   |;;;;;---'\\|;;;|", "   |;;;;|     |;;;|", "   |;;.-'     |;;;|", "'--|/`        |;;;|--.", ";;;;    .     ;;;;.\\;;", ";;;;;-.;_    /.-;;;;;;", ";;;;;;;;;;;;;;;;;;;;;;", ";;;;;;;;;;;;;;;;;;;;;;", "", ""]

## -- Frame -- ##
border = ""
for i in range(11):
    border += "+="

#### ---- OUTPUT ---- ####

## -- Intro -- ##

print("Behold, the beautiful Mona Lisa:")
print()
print(border)
## -- Art -- ##

for line in lines:
    print(line)
print(border)
