from bs4 import BeautifulSoup


def getheader(xgmml,outfile):
    """copies the the header from the imput file, thus copies everything up
    till the term node """
    for line in xgmml.split("\n"):
        if "node" in line: break
        outfile.write(line + "\n")

def writetofile(des,outfile,arrow):
    """write to outfile goes through each line of section and adds tabs. Before
    tabing was off when attpt to just write back to file. Also adds arrow info
    in edge"""
    for line in str(des).split("\n"):
        line = str(line)
        if "node" not in line and "edge" not in line:
            ## tabing was okay for headers and ends
            if arrow and "<graphics" in line:
                # if graphics and a edge line add arrow info
                line = line.split("></")[0]
                line = line.split("<graphics")[0]
                line = "\t" + line  +  arrow +  "/>"
            else:
                ## just fix tabbing
                line = line.split("></")[0]
                line = "\t" + line + "/>"

        outfile.write("\t" + line + "\n")

def write_nodes(soup, outfile):
    """creates a list of nodes from the xgmml file. for each node in file if
    the node is also in mysubset then its added to a the new xgmml file  """
    arrow = False
    ## only need arrow info when an edge
    for nodes in soup.find_all("node"):
        writetofile(nodes,outfile,arrow)

def match_edge(soup, interactions, outfile):
    """creates a list of all the edges in xgmml file. For each edge if both
    genes are present in my subset list then it adds it to the new xgmml file"""
    seen = []
    for edges in soup.find_all("edge"):
        connected_genes = edges.get("label")
        gene1,gene2 = connected_genes.split(" (pd) ")
        #gene1,gene2 = connected_genes.split(" (pd) ")
        connection = "{0}_{1}".format(gene1,gene2)
        
        if connection in interactions:
            print connection
            print "WINNING"
            ###if seen  and they interact....
            color = "<graphics fill=\"#eb2200\" width=\"2\" cy:sourceArrow=\"0\" cy:targetArrow=\"0\""
            writetofile(edges,outfile,color)
        else:
            writetofile(edges,outfile,False)
    
def get_interactions(my_subset):
    interactions = []
    for line in open(my_subset,"rb"):
        args = line.strip().split("\t")
        print args
        interactions.append("{0}_{1}".format(args[0],args[1]))
        interactions.append("{0}_{1}".format(args[1],args[2]))
        interactions.append("{0}_{1}".format(args[0],args[2]))
    
    return interactions


def main(xgmml_file, my_subset, outfh):
    fh = open(xgmml_file)
    ###corr_dic = parse_corr(corr_fh)
    xgmml = fh.read()
    soup = BeautifulSoup(xgmml)
    outfile = open(outfh, "wb")
    header = getheader(xgmml,outfile)
    interactions = get_interactions(my_subset)
    write_nodes(soup,outfile)
    match_edge(soup,interactions,outfile)
    ### only wanna use edge and want to change color...
    outfile.write("</graph>\n")
    outfile.close()






main("CytoscapeSession-2014_07_07-14_43/Sheet1.xgmml", "FFL_xylem_only_network_03_14_13.txt", "xylem_ffls.xgmml")

