import random as r
from collections import defaultdict
from scipy.stats import chisquare

#### def with input number of nodes for subgraph get all permutations [AB,BC], [CB,BC]
### then count the number of times this is seen in my network....
### probalities of directionality of node


def get_network_info(network_info):
    """takes network file with promoter and TF info might be better if use list of everything screened """
    promoters = []
    tfs = []
    onetwork = defaultdict(list)
    enum = 0
    for line in open(network_info):
        enum += 1
        args = line.strip().split(",")
        promoters.append(args[1])
        tfs.append(args[0])
        onetwork[args[0]].append(args[1])

    return set(promoters), set(tfs), onetwork, enum

def build_random_network(promoters, tfs, edge_number):
    promoters = list(promoters)
    tfs = list(tfs)
    rnetwork =defaultdict(list)
    for edge in range(0,edge_number + 1):
        tf = r.choice(tfs)
        p = r.choice(promoters)
        rnetwork[tf].append(p)
    return rnetwork



def get_shared_children(X_network, Y_network):
    X_children = set([XC for XC in X_network])
    Y_children = set([YC for YC in Y_network])
    shared_children = Y_children.intersection(X_children)
    return shared_children


def get_threes(X, Y, X_network, Y_network):
    X_children = set([XC for XC in X_network if XC != X])
    Y_children = set([YC for YC in Y_network if YC != Y])
    ### count the combinations of X,Y,Z
    return len(X_children) +  len(Y_children)
    ## number of combinations 


def get_FFLs(network):
    FFL = []
    three_combos = []
    for X in network.keys():
        for Y in network[X]:
            if X == Y: continue
            if Y in network.keys():
                shared_children = get_shared_children(network[X],network[Y])
                XYs = get_threes(X, Y, network[X], network[Y])
                three_combos.append(XYs)
                if len(shared_children) > 0:
                    for child in shared_children:
                        if Y == child: continue
                        if X == child: continue
                        FFL.append(X)
    return len(FFL), sum(three_combos)

def main(network_file):
    promoters, tfs, onetwork, edge_number = get_network_info(network_file)
    rnetwork =  build_random_network(promoters, tfs, edge_number)
    network_ffl, network_threes = get_FFLs(onetwork)
    random_ffl, random_threes = get_FFLs(rnetwork)
    print network_ffl, network_threes, random_ffl, random_threes
    test_stat, pval = chisquare([network_ffl, network_threes], f_exp=[random_ffl, random_threes])
    print pval, len(onetwork.keys()), len(rnetwork.keys())
    ## pretty close to being same number
main("GT-GRN_Interactions.csv")
