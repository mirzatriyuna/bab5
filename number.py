jumlah = 0
lst = 0

while True:
    line = raw_input('Enter a number : ')
    if line == 'done':
       break
    try:
       tes = float(line)
    except:
       print ('Invalid number')
    else :
       jumlah = jumlah + float(line)
       lst = lst + 1

print int(jumlah), int(lst), float(jumlah/lst)
