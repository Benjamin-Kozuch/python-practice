def SimpleSymbols(str): 

    # code goes here
    
    acceptable = "true"
    
    abc = "abcdefghijklmnopqrstuvwxyz"
    
    if len(str) == 1:
        if str in abc:
            acceptable = "false"

    elif len(str)==2:
        if str[0] in abc or str[1] in abc:
            acceptable = "false"  
    elif len(str)>2:
        
        ind = 0
        for i in str:
            if i in abc:
                
                if (ind==0) or (ind == (len(str)-1)): # its on either end
                    acceptable = "false"
                else:
                    if str[ind-1] != '+' or str[ind+1] != '+':
                        acceptable = "false"
                        

            ind+=1
                
        
    
    
    
    
    return acceptable
    
    