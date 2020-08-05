
    def prefixTable(pattern, p): 

    
        lps=[0]*p #let lps[0...p] be a new arr
        j = 0  #length of the previous longest prefix suffix
        i = 1
        while i < p:
            if pattern[i] == pattern[j]:#if match
                j += 1  #increment the length in the lps table
                lps[i] = j  #put j into the lps table
                i += 1  #check for the next index
            else:  #mismatched
                if j != 0:
                    j = lps[j - 1]
                else:  #mismatched and j==0
                    lps[i] = 0
                    i += 1
        return lps

    def KMP(pattern, text):  


        p = len(pattern)
        t = len(text)
        lps=prefixTable(pattern, p) #generate prefix table

        i = 0  # index for text
        j = 0  # index for pattern

        while i < t:
            if pattern[j] == text[i]:#if match
                i += 1 #increment both pointers
                j += 1
            if j == p:  #if current index==size of the pattern
                print("Found ", pattern, " at index ",str(i-j))
                j = lps[j - 1] #check for the next match, move j to the position at lps[j-1]

            elif i < t and pattern[j] != text[i]:  #mismatched
                if j != 0:
                    j = lps[j - 1] #move j to the position at lps[j-1]
                else: #j==0
                    i += 1  #check for the next index


       

text="algorithmisfun"
pattern="fun"

KMP(pattern,text)




