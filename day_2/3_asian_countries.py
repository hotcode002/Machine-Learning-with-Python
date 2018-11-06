import csv

file = open( "./data/asia_countries.csv" )
asia_countries_f = csv.reader ( file )
asia_countries = []

for row in asia_countries_f : 
    asia_countries.append ( row [0])

print ( asia_countries )
del asia_countries[0] 
asia_countries.remove(0)
print ( asia_countries )
    