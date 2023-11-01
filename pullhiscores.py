import pandas as pd     # table processing shit
import requests as req  # html getting
import time

unix_time = str(time.time())[:10]
# file processing
infile = open('rsns.txt','r')
outfile = open('rsns-levels-'+unix_time+'.txt','w', buffering=1)

# read all the rsns in from file
rsns = infile.read().splitlines()
infile.close()

i=0
# get the hiscores overall level (if possible)
for rsn in rsns:
    try:
        url = req.get('https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal.ws?user1='+rsn)
        content = pd.read_html(url.text)[2]
        tl = (content[(content == "Overall").any(axis=1)][3]).values[0] # where the overall level should be in the request (it looks like shit)
    except:
        tl = 'NOT_FOUND'

    out = rsn + ':' + tl
    outfile.write(out+'\n')
    print('['+str(i)+'/'+str(len(rsns))+']\t'+rsn+' has total level '+tl)
    i = i+1

infile.close()
outfile.close()