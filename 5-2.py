maxi = 0
mini = 100000

while True:
    line = raw_input('Enter a number : ')
    if line == 'done':
       break
    try:
       tes = float(line)
    except:
       print ('Invalid number')
    else :
      if int(line) > maxi:
         maxi = int(line) 
      elif int(line) < mini:
         mini = int(line)     
         
           
print ('maximum:'), int(maxi)
print ('minimum:'), int(mini)

