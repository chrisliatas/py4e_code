# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# the sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
mails = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith("From") and (not line.startswith("From:")):
        pieces = line.split()
        mails[pieces[1]] = mails.get(pieces[1], 0) + 1
popular = None
numails = None
for k, v in mails.items():
    if numails is None or v > numails:
        popular = k
        numails = v
print(popular, numails)
