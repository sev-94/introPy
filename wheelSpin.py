import random

physics_1 = 9
website_stuff_and_apis = 9
python_and_or_python_project = 6
machine_learning_and_neural_nets = 6
make_a_website = 5
linear_algebra = 5
bots_runescape_and_trading_or_other = 4
Physical_Project_with_solidworks_and_components = 4
android_studio = 3
calc_review = 3
multisim_and_component_and_hardware = 2
physics_2 = 2
trading_and_charts = 1
matlab = 1
arraylist = []

def fillarray(itemname, times_to_loop):

    for x in range(physics_1):
        arraylist.append(itemname)
        #totalweight += times_to_loop
        #print(totalweight)

fillarray("physics_1",physics_1)
fillarray("website_stuff_and_apis",website_stuff_and_apis)
fillarray("python_and_or_python_project",python_and_or_python_project)
fillarray("machine_learning_and_neural_nets",machine_learning_and_neural_nets)
fillarray("make_a_website",make_a_website)
fillarray("linear_algebra",linear_algebra)
fillarray("bots_runescape_and_trading_or_other",bots_runescape_and_trading_or_other)
fillarray("Physical_Project_with_solidworks_and_components",Physical_Project_with_solidworks_and_components)
fillarray("android_studio",android_studio)
fillarray("calc_review",calc_review)
fillarray("multisim_and_component_and_hardware",multisim_and_component_and_hardware)
fillarray("physics_2",physics_2)
fillarray("trading_and_charts",trading_and_charts)
fillarray("matlab",matlab)

#print(arraylist)

def pickone():
   numberchosen = random.randint(0,len(arraylist))
   print("The number chosen was " + str(numberchosen) + "! Lets do some " + arraylist[numberchosen] + "!!!")

pickone()