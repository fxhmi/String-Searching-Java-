def rabinKarp(text, pattern, q, d):

    n = len(text)
    m = len(pattern)
    p = 0 #hash value for pattern
    t = 0 #hash value for text
    h = 1
    i = 0
    j = 0

    #h is pow(d, m-1)%q, therefore:
    for i in range(m-1):
        h = (h*d)%q

    #preprocessing
    for i in range(m):

        p = (d*p + ord(pattern[i]))%q   #get hash value
        t = (d*t + ord(text[i]))%q      #get hash value

    #matching #slide the pattern over text one by one
    for i in range(n-m+1):
        if p == t: #if hash values are equal
            j = 0
            for j in range(m): #check character by character
                if pattern[j] != text[i+j]:
                    break

            if j == (m-1): #if equal, the pattern exists in the text
                print(pattern + ' is found at index ' + str(i))

        if i < (n-m): #next window is still available
            #calculate hash value of next window
            t = (d*(t-ord(text[i])*h) + ord(text[i+m]))%q #shift window by one character, eg alg to lgo

            if t < 0: #change t to positive value
                t = t + q

text = 'algorithmisfun'
pattern = 'fun'

rabinKarp(text, pattern, 101, 256)

