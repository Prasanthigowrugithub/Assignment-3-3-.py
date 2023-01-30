def string_test(Q):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in Q:
        if c.isupper():
           d["UPPER_CASE"]=3
        elif c.islower():
           d["LOWER_CASE"]=12
        else:
           pass
    print ("Original String : ", Q)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')