def LetterChanges(str): 

    abc = "abcdefghijklmnopqrstuvwxyz"
    new_str = []
    for i in str:
        if i in abc:
            ind = abc.index(i)
            new_str.append(abc[(ind+1)%26])
        else:
            new_str.append(i)

    vowels_lower = "aeiou" 
    vowels_upper = "AEIOU"
    ind = 0
    for i in new_str:
        if i in vowels_lower:
            vow_ind = vowels_lower.index(i)
            new_str[ind] = vowels_upper[vow_ind]
        ind+=1
        
            
    
    
    
    return ''.join(new_str)
    



print LetterChanges("kjanasA")