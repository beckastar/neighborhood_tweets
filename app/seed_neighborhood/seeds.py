# this seeds the neighborhood table. it has it's own app.py needed in order to run. if it is necessary to reseed or to create a
# another neighborhood table, these two files need to go into the file one leve above. 

#runs once to create all neighborhoods and populate neighborhoods table with geo data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, types 
from app import db
import models 
from models import Neighborhood, Source, Content
#populate sqlalchemy class with name
#geo = "37.3343,34.23423,32.3434,-23.445"
lh = str((37.770336, -122.436812, 37.774814, -122.424366)).strip("()")
lower_haight = Neighborhood(name="Lower Haight", geo=lh)
db.session.add(lower_haight)
uh = str((37.768269, -122.453849, 37.773154, -122.436790)).strip("()")
upper_haight = Neighborhood(name= "Upper Haight", geo=uh)
db.session.add(upper_haight)
dt = str((37.765004, -122.435632,37.769482,-122.427049)).strip("()")
duboce_triangle = Neighborhood(name = "Duboce Triangle", geo=dt)
db.session.add(duboce_triangle)
fllmre = str((37.779590, -122.438722,37.785017,-122.423873)).strip("()")
fillmore = Neighborhood(name= "Fillmore", geo = fllmre)
db.session.add(fillmore)
im = str((37.758326,-122.424839,37.765586, -122.407801)).strip("()")
inner_mission = Neighborhood(name = "Inner Mission", geo=im)
db.session.add(inner_mission)
os = str((37.736201, -122.506292, 37.765315, -122.477324)).strip("()")
outer_sunset = Neighborhood(name = "Outer Sunset", geo=os)
db.session.add(outer_sunset)
cv = str((37.761108, -122.452776, 37.766909, -122.447541)).strip("()")
cole_valley = Neighborhood(name = "Cole Valley", geo=cv)
db.session.add(cole_valley)
om = str((37.741597, -122.424195, 37.748056, -122.407544)).strip("()")
outer_mission = Neighborhood(name = "Outer Mission", geo=om)
db.session.add(outer_mission)
inner_sun = str((37.750590, -122.476208, 37.766367, -122453034)).strip("()")
inner_sunset = Neighborhood(name = "Inner Sunset", geo = inner_sun)
db.session.add(inner_sunset)
ws = str((37.779732, -122.438786, 37.84413, -122.431147)).strip("()")
western_addition = Neighborhood(name="Western Addition", geo = ws)
db.session.add(western_addition)
ph = str((37.787397, -122.446725, 37.795503, -122.425053)).strip("()")
pacific_heights = Neighborhood(name = "Pacific Heights", geo = ph)
db.session.add(pacific_heights)
cstr  = str((37.754220, -122.436726, 37.762804, -122.428529)).strip("()")
castro = Neighborhood(name ="Castro", geo = cstr)
db.session.add(castro)
ir = str((37.773078, -122.471852, 37.789155, -122.459579)).strip("()")
inner_richmond = Neighborhood(name="Inner Richmond", geo = ir)
db.session.add(inner_richmond)
ori = str((37.778641, -122.513394, 37.786170, -122.472968)).strip("()")
outer_richmond = Neighborhood(name="Outer Richmond", geo= ori)
db.session.add(outer_richmond)
noe = str((37.744991, -122.444193, 37.753270, -122.425439)).strip("()")
noe_valley = Neighborhood(name = "Noe Valley", geo = noe)
db.session.add(noe_valley)
bh =  str((37.744991, -122.444193, 37.753270, -122.425439)).strip("()")
bernal = Neighborhood(name = "Bernal Heights", geo = bh)
db.session.add(bernal)
gp =str((37.733242, -122.441897, 37.742134, -122.425332)).strip("()")
glen_park = Neighborhood(name = "Glen Park", geo = gp)
db.session.add(glen_park)
pot = str((37.750143, -122.405934, 37.766293, -122.393661)).strip("()")
potrero = Neighborhood(name = "Potrero Hill", geo = pot)
db.session.add(potrero)
dog =  str((37.750414, -122.392201, 37.766836, -122.388167)).strip("()")
dogpatch = Neighborhood(name = "Dogpatch", geo = dog)
db.session.add(dogpatch)
bay =  str((37.724960, -122.394176, 37.732156, -122.378039)).strip("()")
bayview = Neighborhood(name = "Bayview", geo = bay)
db.session.add(bayview)
som =   str((37.770839,-122.417865,37.782304,-122.399154)).strip("()")
soma = Neighborhood(name = "Soma", geo = som)
db.session.add(soma)
st =  str((37.728491, -122.404819,37.736025,-122.391343)).strip("()")
silver_terrace = Neighborhood(name = "Silver Terrace", geo = st)
db.session.add(silver_terrace)
ex =  str((37.721294,-122.436919,37.729034,-122.419667)).strip("()")
excelsior = Neighborhood(name = "Excelsior", geo=ex)
db.session.add(excelsior)
wp = str((37.734871,-122.475028,37.743627,-122.464299)).strip("()")
west_portal = Neighborhood(name = "West Portal", geo = wp)
db.session.add(west_portal)
ing =  str((37.714437,-122.470737,37.722516,-122.451768)).strip("()")
ingleside = Neighborhood(name = "Ingleside", geo = ing)
db.session.add(ingleside)
 #figre out how to store the boundries of the neighborhood)

db.session.commit()
#lower_haight.boundries => #box(37.770336, -122.436812, 37.774814, -122.424366)

# Lower_Haight = box(37.770336, -122.436812, 37.774814, -122.424366)
# Duboce_Triangle = box(37.765004, -122.435632,37.769482,-122.427049)
# Fillmore = box(37.779590, -122.438722,37.785017,-122.423873)
# Inner_Mission = box(37.758326,-122.424839,37.765586, -122.407801)
# Cole_Valley = box(37.761108, -122.452776, 37.766909, -122.447541)
# # Outer_Mission = box(37.741597, -122.424195, 37.748056, -122.407544)
# Inner_Sunset = box(37.750590, -122.476208, 37.766367, -122453034)
# # Outer_Sunset = box(37.736201, -122.506292, 37.765315, -122.477324)
# Western_Addition = box(37.779732, -122.438786, 37.84413, -122.431147)
# Pac_Heights = box(37.787397, -122.446725, 37.795503, -122.425053)
# # Castro = box(37.754220, -122.436726, 37.762804, -122.428529)
# # Inner_Richmond = box(37.773078, -122.471852, 37.789155, -122.459579)
# # Outer_Richmond = box(37.778641, -122.513394 37.786170, -122.472968)
# # Noe = box(37.744991, -122.444193, 37.753270, -122.425439)
# Bernal = box(37.738135,-122.419260,37.743633, -122.409003)
# # Glen_Park = box(37.733242, -122.441897, 37.742134, -122.425332)
# Potrero = box(37.750143, -122.405934, 37.766293, -122.393661)
# Dogpatch =box(37.750414, -122.392201, 37.766836, -122.388167)
# Bayview =box(37.724960, -122.394176, 37.732156, -122.378039)
# Soma = box(37.770839,-122.417865,37.782304,-122.399154)
# Silver_Terrace = box(37.728491, -122.404819,37.736025,-122.391343)
# Excelsior = box(37.721294,-122.436919,37.729034,-122.419667)
# West_Portal =box(37.734871,-122.475028,37.743627,-122.464299)
# Ingleside=box(37.714437,-122.470737,37.722516,-122.451768)

# coordinates = Point(tweet.coordinates)#['coordinates']
# if coordinates.within(Lower_Haight):
# 	print "Lower_Haight"
# 	content.neighborhood_id = Lower_Haight.id
# if coordinates.within(Upper_Haight):
# 	print "Upper_Haight"
# 	neighborhoods.name = "Upper_Haight"
# if coordinates.within(Duboce_Triangle):
# 	print "Duboce_Triangle"
# 	neighborhoods.name = ""
# if coordinates.within(Fillmore):
# if coordinates.within(Inner_Mission):
# if coordinates.within(Outer_Mission):
# if coordinates.within(Inner_Sunset):
# if coordinates.within(Western_Addition):
# if coordinates.within(Pac_Heights):
# if coordinates.within(Castro):
# if coordinates.within(Inner_Richmond):
# if coordinates.within(Outer_Richmond):
# if coordinates.within(Noe):
# if coordinates.within(Bernal):
# if coordinates.within(Glen_Park):
# if coordinates.within(Potrero):
# if coordinates.within(Dogpatch):
# if coordinates.within(Bayview):
# if coordinates.within(Soma):
# if coordinates.within(Silver_Terrace):
# if coordinates.within(Excelsior):
# if coordinates.within(West_Portal):
# if coordinates.within(Ingleside):




# point = Point(37.771170, -122.441694)
# point2 = Point(20, 20)

# if point.within(Upper_Haight):
#     print "yes yes yes"
# else:
# 	print "nope."