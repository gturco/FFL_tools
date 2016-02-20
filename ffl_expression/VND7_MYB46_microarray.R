library(limma)
library(affy)
library(GEOquery)

setwd("/Users/gturco/Documents/code/Brady/vnd7/GSE16143_RAW")
data <- ReadAffy() 
eset <- rma(data)

targets <- readTargets("/Users/gturco/Documents/code/Brady/vnd7/GSE16143_RAW/targets.txt")
f <- factor(targets$Target, levels=lev)


gse <- getGEO("GSE16143")
eset <- exprs(gse$GSE16143_series_matrix.txt.gz)
targets <- readTargets("/Users/gturco/Documents/code/Brady/vnd7/GSE16143_RAW/targets.txt")
### need to do this following expermental ruls
lev <- as.factor(c("wt.0hr","wt.t1","wt.t3","wt.t6","mu.t1","mu.t3","mu.t6"))
design <- model.matrix(~0+lev)
colnames(design) <- levels(lev)

fit <- lmFit(eset, design)


cont.dif <- makeContrasts(
      Dif1hr =(mu.t1-wt.0hr)-(wt.t1-wt.0hr),
       Dif3hr=(mu.t3-mu.t1)-(wt.t3-wt.t1),
      Dif6hr=(mu.t6-mu.t3)-(wt.t6-wt.t3),
   levels=design)
fit2 <- contrasts.fit(fit, cont.dif)
fit2 <- eBayes(fit2)
topTableF(fit2, adjust="BH")

affy_ids = read.table("/Users/gturco/Documents/code/Brady/vnd7/affy25k_array_elements-2004-06-01.txt", sep="\t", header=TRUE, fill=TRUE)
all <- merge(affy_ids, results, by.x=affy_ids$array_element_name, by.y=ID, all=T)
##### NO REPS CANT DO ANYTHING WITH IT


### VND7

gse <- getGEO("GSE23555")
eset <- exprs(gse$GSE23555_series_matrix.txt.gz)
eset <- eset[,5:8]
design <- model.matrix(~ 0+factor(c(1,1,2,2)))
colnames(design) <- c("VND7Control","VND7XVE")
fit <- lmFit(eset, design)
contrast.matrix <- makeContrasts(VND7XVE-VND7Control,levels=design)
fit2 <- contrasts.fit(fit, contrast.matrix)
fit2 <- eBayes(fit2)
topTableF(fit2, adjust="BH")
results <- topTable(fit2 ,p.value=0.05, number=40000)

affy_ids = read.table("/Users/gturco/Downloads/GPL198-14794.txt", sep="\t", header=TRUE, fill=TRUE)
all <- merge(affy_ids,results, by.x="ID", by.y="ID", all.y=TRUE)
write.csv(all, file = "/Users/gturco/Documents/code/Brady/vnd7/GSE23555.csv", quote=FALSE)



### MYB46
### used timecourse data as reps
gse <- getGEO("GSE16143")
eset <- exprs(gse$GSE16143_series_matrix.txt.gz)
eset <- eset[,2:7]1.25*11
design <- model.matrix(~ 0+factor(c(1,1,1,2,2,2)))
colnames(design) <- c("WT", "MYB46OE")
fit <- lmFit(eset, design)
contrast.matrix <- makeContrasts(MYB46OE-WT,levels=design)
fit2 <- contrasts.fit(fit, contrast.matrix)
fit2 <- eBayes(fit2)
topTableF(fit2, adjust="BH")
results <- topTable(fit2 ,number=40000)

affy_ids = read.table("/Users/gturco/Documents/code/Brady/vnd7/affy25k_array_elements-2004-06-01.txt", sep="\t", header=TRUE, fill=TRUE)
all <- merge(affy_ids,results, by.x="array_element_name", by.y="ID", all.y=TRUE)

write.csv(all, file = "/Users/gturco/Documents/code/Brady/vnd7/GSE16143.csv", quote=FALSE)



### MYB462
gse <- getGEO("GSE25838")
eset <- exprs(gse$GSE25838_series_matrix.txt.gz)
fit <- lmFit(eset)
fit2 <- eBayes(fit)
topTableF(fit2, adjust="BH")
results <- topTable(fit2 ,number=40000)

affy_ids = read.table("/Users/gturco/Documents/code/Brady/vnd7/affy25k_array_elements-2004-06-01.txt", sep="\t", header=TRUE, fill=TRUE)
all <- merge(affy_ids,results, by.x="array_element_name", by.y="ID", all.y=TRUE)

write.csv(all, file = "/Users/gturco/Documents/code/Brady/vnd7/GSE25838.csv", quote=FALSE)