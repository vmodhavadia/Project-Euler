from time import time
start = time()
from statistics import mode
triples = [[3,4,5],[5,12,13],[21,20,29],[15,8,17],[7,24,25],[55,48,73],[45,28,53],[39,80,89],[119,120,169],[77,36,85],[33,56,65],[65,72,97],
[35,12,37],[9,40,41],[105,88,137],[91,60,109],[105,208,233],[187,84,205],[95,168,193],[207,224,305],[117,44,125],[57,176,185],[299,180,349],
[175,288,337],[165,52,173],[51,140,149],[275,252,373],[209,120,241],[115,252,277],[273,136,305],[85,132,157],[133,156,205],[63,16,65]]
sums = []
for triple in triples:
    multiplier = 1
    while multiplier * sum(triple) <= 1000:
        sums.append(multiplier * sum(triple))
        multiplier += 1
print (mode(sums))
print (time() - start)   

    
