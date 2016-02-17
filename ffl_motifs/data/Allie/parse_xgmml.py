from bs4 import BeautifulSoup


def getheader(xgmml,outfile):
    """copies the the header from the imput file, thus copies everything up
    till the term node """
    for line in xgmml.split("\n"):
        if "<node" in line: break
        outfile.write(line + "\n")

def writetofile(des,outfile,arrow):
    """write to outfile goes through each line of section and adds tabs. Before
    tabing was off when attpt to just write back to file. Also adds arrow info
    in edge"""
    for line in str(des).split("\n"):
        line = str(line)
        if "node" not in line and "edge" not in line:
            ## tabing was okay for headers and ends
            if "<graphics" in line:
                line = line.split("></")[0]
                line = "\t" + line
            elif "</graphics" in line:
                line = line.split("></")[0]
                line = "\t" + line

            else:
                ## just fix tabbing
                line = line.split("></")[0]
                line = "\t" + line + "/>"


        outfile.write("\t " + line + "\n")

def write_nodes(soup,my_subset,outfile,write_new):
    """creates a list of nodes from the xgmml file. for each node in file if
    the node is also in mysubset then its added to a the new xgmml file  """
    arrow = False
    ## only need arrow info when an edge
    for nodes in soup.find_all("node"):
        writetofile(nodes,outfile,False)
#        if write_new:    
#            gene = nodes.get("label")
#            if gene in my_subset:
#                node_tag = nodes.graphics
#                node_tag["fill"] = "#eb2200"
#                writetofile(nodes,outfile,False)
#        else:
#            writetofile(nodes,outfile,False)
#
def match_edge(soup, interactions, outfile):
    """creates a list of all the edges in xgmml file. For each edge if both
    genes are present in my subset list then it adds it to the new xgmml file"""
    seen = []
    for edges in soup.find_all("edge"):
        connected_genes = edges.get("label")
        print edges
        gene1,gene2 = connected_genes.split(" (PD) ")
        connection = "{0}_{1}".format(gene1,gene2)
        
        if connection in interactions:
            ###if seen  and they interact....
            graphics_tag = edges.graphics
            graphics_tag["fill"] = "#FF0040"
        #    color = "<graphics fill=\"#eb2200\" width=\"2\" cy:sourceArrow=\"0\" cy:targetArrow=\"0\""
            writetofile(edges,outfile,False)
        else:
            graphics_tag = edges.graphics
            graphics_tag["fill"] = "#A4A4A4"
            writetofile(edges,outfile,False)
    
def get_interactions(my_subset):
    interactions = []
    for line in open(my_subset,"rb"):
        args = line.strip().split("\t")
        interactions.append("{0}_{1}".format(args[0],args[1]))
    
    return interactions


def main(xgmml_file, my_subset, outfh):
    fh = open(xgmml_file)
    ###corr_dic = parse_corr(corr_fh)
    xgmml = fh.read()
    soup = BeautifulSoup(xgmml)
    outfile = open(outfh, "wb")
    header = getheader(xgmml,outfile)
    interactions = get_interactions(my_subset)
    write_nodes(soup,my_subset,outfile,False)
    match_edge(soup,interactions,outfile)
    ### only wanna use edge and want to change color...
    outfile.write("</graph>\n")
    outfile.close()






main("test.xml", "tdnas.txt", "NassimilationNetwork_tdnas.xml")


#main("CytoscapeSession-2014_08_19-00_04/Sheet-1.xml", "FFL_NassimilationNetwork.txt", "NassimilationNetwork_FFLs.xml")
