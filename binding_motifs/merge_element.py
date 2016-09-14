
def mergefile(file1,file2,file3):
    ## order SNBE, SMRE, MYB46RE
    for i,line in enumerate(file1):
        pos,gene,ele = line.strip().split(",")
        ele2 = file2[i].strip().split(",")[2]
        ele3 = file3[i].strip().split(",")[2]
        if ele == "no" and ele2 == 'no' and ele3 == "no":
            print "{0},{1},{2}".format(pos,gene,ele)
        else:
            es = [ele,ele2,ele3]
            efs = [e for e in es if e != 'no']
            new_ele = " and ".join(efs)
            print "{0},{1},{2}".format(pos,gene,new_ele)





rf1 = open("/Users/gturco/Documents/code/Brady/TERE/MYB46RE.txt","r")
rf2 = open("/Users/gturco/Documents/code/Brady/TERE/SMRE.txt","r")
rf3 = open("/Users/gturco/Documents/code/Brady/TERE/SNBE.txt","r")

f1 = rf1.readlines()
f2 = rf2.readlines()
f3 = rf3.readlines()

mergefile(list(f1),f2,f3)

