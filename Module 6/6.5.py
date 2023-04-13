text = "X-DSPAM-Confidence: 0.8475"
atpos = text.find('0')
sppos = text.find('5',atpos)
host = float(text[atpos:sppos+1])
print(host)
