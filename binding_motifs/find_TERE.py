import re
from flatfeature import Bed
from pyfasta import Fasta
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


def make_graph(floc,rloc, gene):
    element = ["no"] * 3000
    for s,e in floc:
        s = s-1
        element[s:e] = ["yes"] * (e - s)
    for s,e in rloc:
        er = 3000- s
        sr = 3000- e
        element[er:sr] = ["yes"] * (e - s)

    #for n in range(0,3000):
    #    print "{0},{1},{2}".format(n,gene,element[n])


def find_seq(promoter):
    tere_locations = []
    tere_element = "[T/A]..[C/T][T/C/G]T.......A[A/C]G.[A/C/T][A/T]"
    #tere_element = "CTTC?.AAAC?GC.AT?"
    #tere_element = "ACC[A/T]A[A/C][T/C]"
    #tere_element = "[T/C]ACC[A/T]A[A/C][T/C]"

    for m in re.finditer(tere_element,promoter):
        tere_locations.append((m.start(), m.end()))
    print len(tere_locations)
    return tere_locations


def get_prom(f,gene):
    seqid = str(gene["seqid"])
    if gene["strand"] == "+":
        prom_start = max(0,int(gene["start"]) - 3000)
        promf = f.sequence({'chr':seqid, 'start': prom_start, 'stop': int(gene["start"])})
        s = Seq(promf, generic_dna)
        promr = s.reverse_complement()
 
    elif gene["strand"] == "-":
        prom_start = int(gene["end"]) + 3000
        promr = f.sequence({'chr':seqid, 'start':int(gene["end"]), 'stop': prom_start, 'strand': '+'})
        s = Seq(promr, generic_dna)
        promf = s.reverse_complement()
    return str(promf),str(promr)

def main(bedfile,seqfile, gene_list):
    print "position,gene,element"
    b = Bed(bedfile)
    f = Fasta(seqfile)
    for gene_name in gene_list:
        gene = b.accn(gene_name)
        promf, promr = get_prom(f, gene)
        print gene_name
        mf = find_seq(promf)
        mr = find_seq(promr)
        make_graph(mf,mr, gene_name)
main("/Users/gturco/Documents/code/Brady/tair_gobe/gobe/data/pair/tair.bed","/Users/gturco/Documents/code/FreelingLab/find_cns/pipeline/data/thaliana_v10.fasta",["AT3G08500","AT5G12870","AT5G03260","AT4G18780","AT5G67210"])
