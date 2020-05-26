#Dictionaries are unordered list of objects
#Let's create a dictionary
LATAM_presidents={"Brasil":"Bolsonaro", "Colombia": "Duque", "Ecuador": "Moreno", "Peru": "Vizcarra"}
#we can print the dictionary by using the print command
print(LATAM_presidents)
#we can verify the data type LATAM_presidents is
print("LATAM_presidents is a "+ str(type(LATAM_presidents)))
#let's check who is the president of Brasil
print("The president of Brasil is "+LATAM_presidents["Brasil"])
#Upss, we've forgotten the president of Mexico. Let's add it
LATAM_presidents["Mexico"]="AMLO"
print("The president of Mexico is "+ str(LATAM_presidents["Mexico"]))
#We can also check if a key(country) is in the dictionary
print("Ecuador" in LATAM_presidents)
#It is also possible to embed a list as a value of a key
#Let's do that with Venezuela
LATAM_presidents["Venezuela"]=["Guaidó","Maburro"]
print(LATAM_presidents)
