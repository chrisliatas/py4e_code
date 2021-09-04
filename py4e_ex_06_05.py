text = "X-DSPAM-Confidence:    0.8475"
apos = text.find('0')
num = float(text[apos:])
print(num)
