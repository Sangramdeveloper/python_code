odisha={"capital":"bhubneswar","population":43742753}
Delhi={"capital":"New delhi",'population':3382959}
Westbengal={"capial":"kolkata","population":184235627}

India={"OD":odisha,"WB":Westbengal,"DL":Delhi}

total_population=0
for state in India.values()
total_population += state["population"]

print("India",India)
print("Total population of India:",total_population)