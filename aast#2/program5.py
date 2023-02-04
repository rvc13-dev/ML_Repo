def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print("The Original String is:", s)
    print( "No. of Upper case characters is :", +u);
    print( "No. of Lower case characters is :", +l )

print(up_low("The quick Brow Fox"))