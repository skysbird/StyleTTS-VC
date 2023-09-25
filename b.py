with open("symbol","w") as sym: 
    with open("b") as s:
        lines = s.readlines()
        i = 0
        for l in lines:
            ll = f"{l[0:-1]}:{i}"
            i = i + 1
            sym.write(ll+"\n")
