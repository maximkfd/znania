from OSMPythonTools.api import Api
from OSMPythonTools.overpass import Overpass
from mediawiki import MediaWiki
api = Api()
op = Overpass()
result = op.query('''
area(3600421007)->.searchArea;
rel["leisure"="park"](area.searchArea); 
out body;''')
raw_parks = result._json['elements']
print(raw_parks[0])
for park in raw_parks:
    if 'tags' in park:
        # if 'wikipedia'