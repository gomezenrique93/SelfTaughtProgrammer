# create a dictionary that contains different attributes about you 
# include height, weight, hair color, etc.
# this challennge will suffice for both #3 and #4
enrique_gomez = { 

    "height": "5ft, 5in",
    "weight": "140 lbs",
    "hair color": "brown",
    "age": 29,
    "sex": "male",
    "organ donor": "absolutely not"

}

attributes = input("What would you like to know about me? ")                    
if attributes in enrique_gomez: 
    attribute = enrique_gomez[attributes]
    print(attribute)
else:
    print("you don't know me like that...")
