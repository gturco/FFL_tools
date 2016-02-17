
def get_AGI_dic(mallorie_data):
    d = {}
    for line in open(mallorie_data,"rb"):
        args = line.strip().split("\t")
        d[args[2]] = args[0]
    d["NST1"] = "AT2G46770"
    d["NST2"] = "AT3G61910"
    d["SND1"] = "AT1G32770"
    d["PAL1"] = "AT2G37040"
    d["IRX14-L"] = "AT5G67230"
    d["UXS3"] = "AT5G59290"
    d["CesA8"] = "AT4G18780"
    d["SCPL48"] = "AT3G45010"
    d["CesA4"] = "AT5G44030"

    return d

def FFL_h(d,FFL_hdata):
    new_list = []
    for line in open(FFL_hdata):
        args = line.strip().split("\t")
        if "C3H14" in line : continue
        new_list.append("{0}_{1}_{2}".format(d[args[0]],d[args[1]],d[args[2]]))
    return new_list

def matches(h_list,mallorie_ffl):
    not_unq = []
    unq = []
    for line in open(mallorie_ffl,"rb"):
        args = line.strip().split("\t")
        ffl = "{0}_{1}_{2}".format(args[0],args[1],args[2])
        if ffl in h_list: not_unq.append(ffl)
        else : unq.append(ffl)
    print len(not_unq)
    print len(unq)


def main(mallorie_data,FFL_hdata,mallorie_ffl):
    d = get_AGI_dic(mallorie_data)
    h_list = FFL_h(d,FFL_hdata)
    matches(h_list,mallorie_ffl)

main("/Users/gturco/Documents/code/Brady/mallorie/stelexylem/MallorieData_New/SteleXylemNetwork.txt","Hussy_direct_FFL.txt","FFL_xylem_only_network_03_14_13.txt")
