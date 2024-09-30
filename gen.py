# https://js.cytoscape.org/
# https://www.graphdracula.net/
# https://d3js.org/

import json

dbfile = "data/db.json"

with open(dbfile, "r") as f:
    data = json.load(f)
    f.close()


##### Build the graph
# First, let's make an unweighted graph that is ignorant of music theory

graph = {}

for song in data["songs"]:
    chords = song["chords"]
    for i,chord in enumerate(chords[:-1]):
        nextchord = chords[i+1]
        graph.setdefault(chord, set()).add(nextchord)


##### Create an interactive data display







##### Write it to an HTML file

with open("index.html", "w") as f:
    f.write(str(graph))
    f.close()
