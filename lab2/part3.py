#loop through rows from 0 to 6
for i in range(7):
    #loop through columns from 0 to 6
    for j in range(7):
        #check if row index equals column index
        if i == j:
            #print dollar sign, spaces(equal to row index), another dollar sign
            print("$"+i*" "+"$")
