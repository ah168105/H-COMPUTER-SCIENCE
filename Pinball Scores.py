#### ---- SETUP ---- ####

## -- Lists -- ##

scores = [83103, 81285, 76301, 76294, 75029, 72948, 71444, 68203, 67503, 64629, 62840, 62319, 61923, 60283, 58184, 58018, 57263, 57088, 55024, 53927, 53823, 53311, 52302, 52265, 51983, 51832, 51656, 50820, 48125, 47100]
names = ["SOM", "TYL", "HHS", "OSL", "EGS", "NMB", "LOL", "PAR", "NBD", "AAA", "ATB", "CGR", "ANT", "EMR", "KMP", "JJH", "BMR", "JLT", "WWC", "RST", "JFK", "VVE", "LSN", "ZYA", "DMD", "AMR", "SYD", "UMN", "OLI", "FEF"]

## -- Variables -- ##

start = 0
lines_per_page = 5

#### ---- OUTPUT ---- ####

print("Press Enter to display each page of scores.")

## -- Main loop -- ##
while start < len(scores):
    input()

    ## -- Scores -- ##

    if start == 0:
        page_scores = scores[0:4]
        page_names = names[0:4]
        start += 5
    if start == 5:
        page_scores = scores[5:9]
        page_names = names[5:9]
        start += 5
    if start == 10:
        page_scores = scores[10:14]
        page_names = names[10:14]
        start += 5
    if start == 15:
        page_scores = scores[15:19]
        page_names = names[15:19]
        start += 5
    if start == 20:
        page_scores = scores[20:24]
        page_names = names[20:24]
        start += 5
    if start == 25:
        page_scores = scores[25:29]
        page_names = names[25:29]
        start += 5
    ## -- Display -- ##

    for i in range(len(page_scores)):
        print(str(page_scores[i]) + " - " + page_names[i])
