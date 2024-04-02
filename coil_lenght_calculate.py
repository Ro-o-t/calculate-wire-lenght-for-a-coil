import math
diameter_initial=float(input("insert initial coil diameter(mm):"))
biggest_diameter=float(input("insert max coil diameter(mm):"))#to see if the final diameter will be to large or not 
actual_diameter=diameter_initial #to calculate final diameter

height=float(input("insert coil height(mm):"))
width=float(input("insert wire width(mm):"))
number_of_spin_initial=int(input("insert the number of spin:"))
if width>height:
    print("ERROR:wire width is larger than coil height press CTRL+C to stop")
    
#see if there is an error with values
pi=math.pi
number_of_spin_actual=0
#variable values 

    


while number_of_spin_initial>=number_of_spin_actual:#stop when enough spin 
    lenght=(height/width)*(diameter_initial*pi)#calculate the lenght of each spin (circumference)
    diameter_initial+=width #because the actual diameter increase 
    number_of_spin_actual+=height/width #the number of spin for each couch 
    actual_diameter+=width#we add wire width each time we do a nex column 
print(f"the total wire lenght you need for your coil is:{lenght} mm so {lenght/1000} m")#print result
if actual_diameter>biggest_diameter:
    print()
    print(f"ERROR:the final diameter is be bigger than the max diameter ({actual_diameter-biggest_diameter} mm extra so ({(actual_diameter-biggest_diameter)/1000} m extra)")
