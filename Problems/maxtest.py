d = { "a" : -1,
      "b" : -2,
      "c" : 3,
      "d" : -8,
      "e" : 0,
      "f" : -15
      }
z,y = 0,0                      

for key in d.keys():        
    x = d[key]              
    if x > z:           
        z = x           
        val_key = key     
    elif x < y:
        y = x
        value_key = key

if z > y and z > 0:
    print(val_key,z)
elif z==0 and y<0:
    print(value_key, y)

