districts=['ST' ,'BD' ,'BTL','CG ','DD '',HBT']
population=[150.300,247.100,330.300,266.800,420.900,318.000]
km2=["117.43","9.224","43.55","12.04","9.96","10.06"]
d=[]
a1=list(population)
a2=list(districts)
print("Quan| Dan So  | Km2")
for a,b,c in zip(districts,population,km2):
        print(a,"|",b,"|",c)
print("The distric have the less populations : ",min(population),end="")
print("The distric have the less populations : ",max(population),end="") 

















