
from collections import defaultdict, Counter

def read_network(network_csv):
    d = defaultdict(list)
    for line in open(network_csv):
##        X,Y,cor = line.strip().split("\t")[0:3]
        args = line.strip().split(",")
        X = args[0]
        Y = args[4]
        if "x" in args[7]:
            print "{0}\t{1}".format(X,Y)
        #else:
        #    sign = "POS"
        
        #$if Y == "": 
        #    Y = args[9]
        #for w in Y.split(";"):



##main("/Users/gturco/network.csv")
#main("/Users/gturco/Documents/code/Brady/mallorie/stelexylem/MallorieData_New/CytoscapeSession/fe_cyto_corr.tsv")
#main("/Users/gturco/Documents/code/Brady/mallorie/stelexylem/MallorieData_New/CytoscapeSession/nacl_cyto_corr.tsv")
###main("/Users/gturco/Documents/code/Brady/mallorie/stelexylem/MallorieData_New/SteleXylemNetwork.txt")
read_network("10_8_13_NETWORK_locus.txt-Table 1.csv")
#main("/Users/gturco/Hussey et al network/Sheet1-Table 1.csv")


#main("xylem_only_network_03_14_13.csv")
