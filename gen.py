# https://js.cytoscape.org/
# https://www.graphdracula.net/
# https://d3js.org/

import json

dbfile = "data/db.json"

with open(dbfile, "r") as f:
    data = json.load(f)
    f.close()


##### Build the graph







##### Create an interactive data display







##### Write it to an HTML file

with open("index.html", "w") as f:
    f.write(str(data))
    f.close()
