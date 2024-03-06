
# STRING FUNCTIONS


def stringmatcher(word,possibilities,cutoff,n):
    dict={}
    list=[]
    output=[]
    for i in possibilities:
        word=word.lower();i=i.lower()
        a=len(word)/len(i)*0.9
        if (word[0],word[-1])==(i[0],i[-1]):
            b=1.3
        else:
            b=0.7
        count=0
        for j in word:
            if j in i:
                count+=1
        c=count/len(word)*1.3
        d=a*b*c
        if d>=cutoff:
            dict[d]=i
            list.append(d)
        else:
            pass
    list.sort(reverse=True)
    if not list:
        return None
    elif len(list)<n:
        for i in range(len(list)):
            output.append(dict[list[i]])
        return output
    else:
        for i in range(n):
            output.append(dict[list[i]])
        return output



# DICTIONARY FUNCTIONS


def get_max_value_key(d):
    if not d:
        return None

    max_value = max(d.values())
    return max(k for k, v in d.items() if v == max_value)