# this seeds the neighborhood table. it has it's own app.py needed in order to run. if it is necessary to reseed or to create a
# another neighborhood table, these two files need to go into the file one leve above. 

#runs once to create all neighborhoods and populate neighborhoods table with geo data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, types 
from app import db

from models import Neighborhood, Source, Content

#populate sqlalchemy class with name
#geo = "37.3343,34.23423,32.3434,-23.445"
neighborhoods = [
	{'name': 'Lower Haight',
	 'left_lat': 37.770336,
	 'left_long': -122.436812,
	 'right_lat': 37.774814,
	 'right_long': -122.42436
	},
	{'name': 'Upper Haight',
	'left_lat': 37.768269,
	'left_long': -122.453849,
	'right_lat': 37.773154,
	'right_long': -122.436790
	},
	{'name': 'Doboce Triangle',
	'left_lat': 37.765004,
	'left_long': 122.435632,
	'right_lat': 37.769482,
	'right_long': -122.427049
	},
	{'name': 'Fillmore',
	'left_lat': 37.779590,
	'left_long': -122.438722,
	'right_lat': 37.785017,
	'right_long': -122.423873
	},
	{'name': 'Inner Mission',
	'left_lat': 37.758326,
	'left_long': -122.424839,
	'right_lat': 37.765586,
	'right_long': -122.407801
	},
	{'name': 'Outer Sunset',
	'left_lat': 37.736201,
	'left_long': -122.506292,
	'right_lat': 37.765315,
	'right_long': -122.477324
	},
	{'name': 'Cole Valley',
	'left_lat': 37.761108,
	'left_long': -122.452776,
	'right_lat': 37.766909,
	'right_long': -122.447541
	},
	{'name': 'Outer Mission',
	'left_lat': 37.741597,
	'left_long': -122.424195,
	'right_lat': 37.748056,
	'right_long': -122.407544
	},
	{'name': 'Inner Sunset',
	'left_lat': 37.750590,
	'left_long': -122.476208,
	'right_lat': 37.766367,
	'right_long': -122453034
	},
	{'name': 'Western Addition',
	'left_lat': 37.779732,
	'left_long': -122.438786,
	'right_lat': 37.84413,
	'right_long': -122.431147
	},
	{'name': 'Pacific Heights',
	'left_lat': 37.787397, 
	'left_long': -122.446725,
	'right_lat': 37.795503,
	'right_long': -122.425053
	},
	{'name': 'Castro',
	'left_lat': 37.754220,
	'left_long': -122.436726,
	'right_lat': 37.762804,
	'right_long': -122.428529
	},
	{'name': 'Inner Richmond',
	'left_lat': 37.773078,
	'left_long': -122.471852,
	'right_lat': 37.789155,
	'right_long': -122.459579
	},
	{'name': 'Outer Richmond',
	'left_lat': 37.778641,
	'left_long': -122.513394,
	'right_lat': 37.786170,
	'right_long': -122.472968
	},
	{'name': 'Noe Valley',
	'left_lat': 37.744991,
	'left_long': -122.444193,
	'right_lat': 37.753270,
	'right_long': -122.425439
	},
	{'name': 'Bernal Heights',
	'left_lat': 37.744991,
	'left_long': -122.444193,
	'right_lat': 37.753270,
	'right_long': -122.425439
	},
	{'name': 'Glen Park',
	'left_lat': 37.733242,
	'left_long': -122.441897,
	'right_lat': 37.742134,
	'right_long': -122.425332 
	},
	{'name': 'Potrero Hill',
	'left_lat': 37.750143,
	'left_long': -122.405934,
	'right_lat': 37.766293,
	'right_long': -122.393661
	},
	{'name': 'Dogpatch',
	'left_lat': 37.750414,
	'left_long': -122.392201,
	'right_lat': 37.766836,
	'right_long': -122.388167 
	},
	{'name': 'Bayview',
	'left_lat': 37.724960,
	'left_long': -122.394176,
	'right_lat': 37.732156,
	'right_long': -122.378039
	},
	{'name': 'SOMA',
	'left_lat': 37.770839,
	'left_long': -122.417865,
	'right_lat': 37.782304,
	'right_long': -122.399154
	},
	{'name': 'Silver Terrace',
	'left_lat': 37.728491, 
	'left_long': -122.404819,
	'right_lat': 37.736025,
	'right_long': -122.391343
	},
	{'name': 'Excelsior',
	'left_lat': 37.721294,
	'left_long': -122.436919,
	'right_lat': 37.729034,
	'right_long': -122.419667
	},
	{'name': 'West Portal',
	'left_lat': 37.734871,
	'left_long': -122.475028,
	'right_lat': 37.743627,
	'right_long': -122.464299
	},
	{'name': 'Ingleside',
	'left_lat': 37.714437,
	'left_long': -122.470737,
	'right_lat': 37.722516,
	'right_long': -122.451768
	}
]

for neighborhood in neighborhoods:
	db.session.add(Neighborhood(**neighborhood))
	
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