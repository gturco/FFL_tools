
from collections import defaultdict, Counter

def read_network(network_csv):
    d = defaultdict(list)
    for line in open(network_csv):
        X,Y,sign = line.strip().split(",")[0:3]
        #args = line.strip().split(",")
        #X = args[0]
        #Y = args[1]
        #if float(cor) < 0:
        #sign = "NEG"
        #else:
        #    sign = "POS"
        
        #$if Y == "": 
        #    Y = args[9]
        #for w in Y.split(";"):

        d[X].append((Y,sign))
    return d



def get_shared_children(X_network, Y_network):
    X_children = set([XC for XC, Xsign in X_network])
    Y_children = set([YC for YC, Ysign in Y_network])
    shared_children = Y_children.intersection(X_children)
    return shared_children

def get_FFL(XYsign,YZsign,XZsign):
    if XZsign == "POS":
        if XYsign == "POS" and YZsign == "POS":
            return "C1"
        elif XYsign == "NEG" and YZsign == "NEG":
            return "C4"
        elif XYsign == "POS" and YZsign == "NEG":
            return "I1"
        elif XYsign == "NEG" and YZsign == "POS":
            return "I4"
    elif XZsign == "NEG":
        if XYsign == "NEG" and YZsign == "POS":
            return "C2"
        elif XYsign == "POS" and YZsign == "NEG":
            return "C3"
        elif XYsign == "NEG" and YZsign == "NEG":
            return "I2"
        elif XYsign == "POS" and YZsign == "POS":
            return "I3"
 
def main(network_csv):
    network = read_network(network_csv)
    FFL = []
    for X in network.keys():
        for Y, XYsign in network[X]:
            if X == Y: continue
            if Y in network.keys():
                shared_children = get_shared_children(network[X],network[Y])
                if len(shared_children) > 0:
                    for child in shared_children:
                        if Y == child: continue
                        if X == child: continue
                        YZsign = filter(lambda i:i[0] == child, network[Y])[0][1]
                        XZsign = filter(lambda i:i[0] == child, network[X])[0][1]
                        FFL_type = get_FFL(XYsign,YZsign,XZsign)
                        print "{0}\t{1}\t{2}\t{3}".format(X,Y,child,FFL_type)
                        FFL.append(X)
    print len(FFL)
    #print Counter(FFL)

main("subnetwork.txt")
#main("/Users/gturco/Documents/code/Brady/mallorie/stelexylem/MallorieData_New/CytoscapeSession/fe_cyto_corr.tsv")
#main("/Users/gturco/Documents/code/Brady/mallorie/stelexylem/MallorieData_New/CytoscapeSession/nacl_cyto_corr.tsv")
###main("/Users/gturco/Documents/code/Brady/mallorie/stelexylem/MallorieData_New/SteleXylemNetwork.txt")
#main("/Users/gturco/Hussey Network direct/Sheet1-Table 1.csv")
#main("/Users/gturco/Hussey et al network/Sheet1-Table 1.csv")


#main("xylem_only_network_03_14_13.csv")
