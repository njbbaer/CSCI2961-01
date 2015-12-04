library(arules)
library(arulesViz)

titanic <- read.table("Dataset.data", header=F)
names(titanic) <- c("Class", "Age", "Sex", "Survived")

rules <- apriori(titanic,
                 parameter = list(minlen=3, supp=0.002, conf=0.2),
                 appearance = list(rhs=c("Survived=yes"), lhs=c("Class=1st", "Class=2nd", "Class=3rd", "Age=child", "Age=adult"), default="none"), control = list(verbose=F))
rules.sorted <- sort(rules, by="confidence")

plot(rules.all)
plot(rules.all, method="grouped")
plot(rules.all, method="graph")
plot(rules.all, method="graph", control=list(type="items"))
plot(rules.all, method="paracoord", control=list(reorder=TRUE))
