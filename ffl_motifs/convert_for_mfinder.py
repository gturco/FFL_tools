
def parse_data(network_file):
    names = []
    interactions = []
    for line in open(network_file):
        if line[0] == "P": continue
        args = line.strip().split(",")
        tf = args[2]
        names.append(tf)
        prom = args[0]
        names.append(prom)
        interactions.append((tf,prom))
    return set(names), set(interactions)


def main(network_file):
    names, interactions = parse_data(network_file)
    int_names = [i+ 1 for i in range(0,len(names))]
    rename = dict(zip(names,int_names))
    for tf,prom in interactions:
        print "{0}\t{1}\t1".format(rename[tf], rename[prom])


main("xylem_only_network_03_14_13.csv")
