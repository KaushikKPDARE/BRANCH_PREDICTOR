address=trace.readlines() 
print "the number of instructions in trace" 
print len(address) 
br=[] 
for index in range(len(address)-1): 
t=int(address[index+1],16)-int(address[index],16) 
if t>15 or t<0: 
br.append(address[index]) 
print len(br) 
def remove_duplicates(br1): 
arr2=[] 
for i in br1: 
if not i in arr2: 
arr2.append(i) 
return arr2 
br=remove_duplicates(br) 
print "list of the unique branched inst. addresses:" 
print br 
print "number of unique branched inst. addresses:" 
print (len(br)) 
dec={} 
for index in range(len(br)): 
key=bin(int(br [index],16))[-5:] 
dec[key]=1 
#counter for prediction 
predict=0 
#counter for misprediction 
mpredict=0 
for i in range(len(address)-1): 
for j in range(len(br)): 
p=int(address[i+1],16)-int(address[i],16) 
if br[j]==address[i]: 
key=bin(int(address[i],16))[-5:] 
if(p>15 or p<0): 
if dec[key]==1: 
predict=predict+1 
else: 
mpredict=mpredict+1 
dec[key]=1 
else: 
if dec[key]==0: 
predict=predict+1 
else: 
mpredict=mpredict+1 
dec[key]=0 
print "number of correct predictions:" 
print predict 
print "number of mispredictions" 
print mpredict 
print "the accuracy of 1 bit br predictor :" 
#accuracy 
print (predict/float(predict+mpredict))*100 
print "the hash table of the 1 bit counter" 
print dec 
#Two bit counter 
for i in range(len(br)): 
key=bin(int(br[i],16))[-4:] 
dec[key]=3 
#counter for prediction 
predict=0 
#counter for misprediction 
mpredict=0 
for i in range(len(address)-1): 
for j in range(len(br)): 
p=int(address[i+1],16)-int(address[i],16) 
if br[j]==address[i]: 
key=bin(int(address[i],16))[-4:] 
if(p>15 or p<0): 
if dec[key]==3 or dec[key]==2: 
predict=predict+1 
else: 
if dec[key]==1: 
mpredict=mpredict+1 
dec[key]=3 
else: 
mpredict=mpredict+1 
dec[key]=2 
else: 
if dec[key]==0 or dec[key]==1: 
predict=predict+1 
else: 
if dec[key]==3: 
mpredict=mpredict+1 
dec[key]=1 
else: 
mpredict=mpredict+1 
dec[key]=0
