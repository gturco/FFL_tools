library(ggplot2)
library(grid)
file_name = "/Users/gturco/Documents/Data/FFL/myb83_qpcr_neg.csv"
x = read.csv(file_name, header=TRUE)
x$Expression <- factor(x$Expression, levels = c("Low","Med","","High"))
x$Name <- factor(x$Name, levels = c("MYB83","CESA8","IRX15-L","LAC11"))
ggplot(data=x[4:12,], aes(x=Expression, y=avg_CT, colour=Name, group=Name)) +  geom_line(size = 0.3) +
  theme_classic() + theme(legend.position ="none", text=element_text(size=8), panel.margin = unit(0, "cm"), plot.margin = unit(c(0, 0, 0.01, -0.1), "cm"),axis.ticks = element_line(size = 0.1), axis.line = element_line(size = 0.1), axis.ticks.length = unit(0.05, "cm"), axis.ticks.margin =unit(0, "cm")) + xlab(NULL) + ylab("Fold Change") + scale_colour_manual(values= c("Black","Blue","#003333"))
ggsave("/Users/gturco/Documents/Data/FFL/myb83_targets.pdf", width=5.60, height=3.2, dpi=600, units="cm")  


ggplot(data=x[0:3,], aes(x=line, y=avg_CT, colour=Name, group=Name)) +  geom_line(size = 0.3) +
  theme_classic() + theme(legend.position ="none", text=element_text(size=8), panel.margin = unit(0, "cm"), plot.margin = unit(c(0, 0, 0.01, -0.1), "cm"),axis.ticks = element_line(size = 0.1), axis.line = element_line(size = 0.1), axis.ticks.length = unit(0.05, "cm"), axis.ticks.margin =unit(0, "cm")) + xlab(NULL) + ylab("Fold Change") + scale_colour_manual(values= c("Red"))
ggsave("/Users/gturco/Documents/Data/FFL/myb83.pdf", width=5.60, height=3.2, dpi=600, units="cm")  

file_name = "/Users/gturco/Documents/Data/FFL/vnd7_qpcr.csv"
x = read.csv(file_name, header=TRUE)
x$line <- factor(x$line, levels = c("Low","Med","","High"))
x$Name <- factor(x$Name, levels = c("VND7","CESA8","IRX15-L","LAC11","MYB46","MYB83"))
ggplot(data=x[4:18,], aes(x=line, y=avg_CT, colour=Name, group=Name)) +  geom_line(size = 0.3) +
  theme_classic() + theme(legend.position ="none", text=element_text(size=8), panel.margin = unit(0, "cm"), plot.margin = unit(c(0, 0, 0.01, -0.1), "cm"),axis.ticks = element_line(size = 0.1), axis.line = element_line(size = 0.1), axis.ticks.length = unit(0.05, "cm"), axis.ticks.margin =unit(0, "cm")) + xlab(NULL) + ylab("Fold Change")  + scale_colour_manual(values= c("Black","Blue","#003333","#663300","red"))
ggsave("/Users/gturco/Documents/Data/FFL/vnd7_targets.pdf", width=5.60, height=3.2, dpi=600, units="cm")  


ggplot(data=x[0:3,], aes(x=line, y=avg_CT, colour=Name, group=Name)) +  geom_line(size = 0.3) +
  theme_classic() + theme(legend.position ="none", text=element_text(size=8), panel.margin = unit(0, "cm"), plot.margin = unit(c(0, 0, 0.01, -0.1), "cm"),axis.ticks = element_line(size = 0.1), axis.line = element_line(size = 0.1), axis.ticks.length = unit(0.05, "cm"), axis.ticks.margin =unit(0, "cm")) + xlab(NULL) + ylab("Fold Change") + scale_colour_manual(values= c("#0066CC"))

ggsave("/Users/gturco/Documents/Data/FFL/vnd7.pdf", width=5.60, height=3.2, dpi=600, units="cm")  


### elements

file_name = "/Users/gturco/Documents/code/Brady/TERE/test_file.txt"
x = read.csv(file_name, header=TRUE)
ggplot(data=x, aes(x=position, y=gene, colour=SNBE, group=gene)) +  geom_point(size=15, shape=0) + theme_classic()  + scale_colour_manual(values= c("black","#7f0000")) + ylab("") + xlab("Region Upstream Gene")

file_name = "/Users/gturco/Documents/code/Brady/TERE/SMRE.txt"
x = read.csv(file_name, header=TRUE)
ggplot(data=x, aes(x=position, y=gene, colour=element, group=gene)) +  geom_point(size=15, shape=0) + theme_classic()  + scale_colour_manual(values= c("black","#7f0000")) + ylab("") + xlab("Region Upstream Gene")

file_name = "/Users/gturco/Documents/code/Brady/TERE/MYB46RE.txt"
x = read.csv(file_name, header=TRUE)
ggplot(data=x, aes(x=position, y=gene, colour=element, group=gene)) +  geom_point(size=15, shape=0) + theme_classic()  + scale_colour_manual(values= c("black","#7f0000")) + ylab("") + xlab("Region Upstream Gene")

file_name = "/Users/gturco/Documents/code/Brady/TERE/elements_targets.txt"
x = read.csv(file_name, header=TRUE)
x$Element <- factor(x$Element, levels = c("MYB46RE","SMRE","","SNBE","MYB46RE and SMRE","MYB46RE and SMRE and SNBE","MYB46RE and SNBE","SMRE and SNBE","None"))
ggplot(data=x, aes(x=position, y=gene, colour=Element, group=gene)) +  geom_point(size=10, shape=0) + theme_classic() + scale_colour_manual(values= c("yellow","purple","red","green","#0000ff","#ff0080","black")) + ylab("") + xlab("Region Upstream Gene")

### bar graph

file_name = "/Users/gturco/Documents/Data/FFL/myb83_qpcr_neg.csv"
x = read.csv(file_name, header=TRUE)
x$Expression <- factor(x$Expression, levels = c("Low","Med","","High"))
x$Name <- factor(x$Name, levels = c("MYB83","LAC11","CESA8","IRX15-L"))
ggplot(data=x, aes(x=Expression, y=avg_CT, fill=Name)) +  geom_bar(position="dodge",stat="identity")  + theme_classic() +  xlab(NULL) + ylab("Fold Change") + scale_fill_manual(values= c("Black","Blue","#003333","red"))
ggplot(data=x[4:12,], aes(x=Name, y=avg_CT, fill=Expression)) +  geom_bar(position="dodge",stat="identity")  + theme_classic() +  xlab(NULL) + ylab("Fold Change") + scale_fill_manual(values= c("#b9d2e2","#6aacd4","#1d66a3"))
ggsave("/Users/gturco/Documents/Data/FFL/myb83_targets_bar.pdf", width=5.60, height=3.2, dpi=600, units="cm")  
ggplot(data=x, aes(x=Name, y=avg_CT, fill=Expression)) +  geom_bar(position="dodge",stat="identity")  + theme_classic() +  xlab(NULL) + ylab("Fold Change") + scale_fill_manual(values= c("#F97976","#F82F2B","#B92320"))
ggsave("/Users/gturco/Documents/Data/FFL/myb83_all_bar.pdf", width=5.60, height=3.2, dpi=600, units="cm")  

file_name = "/Users/gturco/Documents/Data/FFL/vnd7_qpcr.csv"
x = read.csv(file_name, header=TRUE)
x$Expression <- factor(x$Expression, levels = c("Low","Med","","High"))
x$Name <- factor(x$Name, levels = c("VND7","LAC11","CESA8","IRX15-L","MYB46","MYB83"))
ggplot(data=x, aes(x=Expression, y=avg_CT, fill=Name)) +  geom_bar(position="dodge",stat="identity")  + theme_classic() +  xlab(NULL) + ylab("Fold Change") + scale_fill_manual(values= c("Black","Blue","#003333","#663300","red","#0066CC"))
ggplot(data=x[4:18,], aes(x=Name, y=avg_CT, fill=Expression)) +  geom_bar(position="dodge",stat="identity")  + theme_classic() +  xlab(NULL) + ylab("Fold Change") + scale_fill_manual(values= c("#b9d2e2","#6aacd4","#1d66a3"))
ggsave("/Users/gturco/Documents/Data/FFL/vnd7_targets_bar.pdf", width=5.60, height=3.2, dpi=600, units="cm")
ggplot(data=x, aes(x=Name, y=avg_CT, fill=Expression)) +  geom_bar(position="dodge",stat="identity")  + theme_classic() +  xlab(NULL) + ylab("Fold Change") + scale_fill_manual(values= c("#b9d2e2","#6aacd4","#1d66a3"))
ggsave("/Users/gturco/Documents/Data/FFL/vnd7_all_bar.pdf", width=5.60, height=3.2, dpi=600, units="cm")
