with open("data.txt", 'w') as newf:
    with open("cstimer.csv", 'r') as f:
        frl = f.readlines()[1:]
        for l in frl:
            l.rstrip()
            l_list = l.split(';')
            try:
                final = ';'.join([l_list[1], l_list[3]]) + "\n"
                newf.write(final)
            except:
                pass
    with open("cubetime.csv", 'r') as g:
        grl = g.readlines()[1:]
        for l in grl:
            l.rstrip()
            l_list = l.split(",")
            final = ';'.join([str(round(float(l_list[0]),2)), l_list[2]]) + "\n"
            newf.write(final)
                    

