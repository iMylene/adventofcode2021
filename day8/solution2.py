import sys

data = [ x.split(" | ") for x in sys.stdin.readlines() ]
signal_patterns = []
output_patterns = []
for line in data:
    signal_patterns.append(line[0])
    output_patterns.append(line[1].strip("\n"))


'''
  8:    
 aaaa   
b    c  
b    c  
 dddd   
e    f  
e    f  
 gggg   

  8:    
     upper   
   up     up  
 left     right  
    middle   
lower     lower 
  lef     right  
     lower   
'''