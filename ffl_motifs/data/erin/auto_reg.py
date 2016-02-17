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
    return len(shared_children)


def get_auto(network):
    auto = []
    for X in network.keys():
        for Y in network[X]:
            if X == Y: auto.append(X)
    return len(auto)

def main(network_file):
    promoters, tfs, onetwork, edge_number = get_network_info(network_file)
    random_threes = get_shared_children(promoters,tfs)
    rnetwork =  build_random_network(promoters, tfs, edge_number)
    network_auto = get_auto(onetwork)
    random_auto = get_auto(rnetwork)
    print network_auto,  random_auto
    test_stat, pval = chisquare([network_auto, random_threes], f_exp=[random_auto, random_threes])
    print pval, len(onetwork.keys()), len(rnetwork.keys())
    ## pretty close to being same number
main("GT-GRN_Interactions.csv")
