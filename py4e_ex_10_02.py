# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
hrs = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith("From") and (not line.startswith("From:")):
        pieces = line.split()
        time = pieces[5].split(':')
        hrs[time[0]] = hrs.get(time[0], 0) + 1

lst = sorted([(k, v) for k, v in hrs.items()])
for x, y in lst:
    print(x, y)
