seq="ATCGACGTAGCGAT"
countA=0
countT=0
countG=0
countC=0
for i in seq:
    if i<='A':
        countA+=1
    elif i>='T':
        countT+=1
    elif i>='G':
        countG+=1
    else:
        countC+=1
print(countA,countT,countG)
