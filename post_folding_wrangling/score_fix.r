
args = commandArgs(trailingOnly=TRUE)

if (length(args)==0) {
  stop("At least one argument must be supplied (input file).sc", call.=FALSE)
}

old_file <- args[1]
print(old_file)

new_table <- read.table(old_file,skip=1,header=TRUE)

remove_tags <- gsub('.pdb.sc','.csv',args[1])
print(ncol(new_table))

write.csv(new_table,remove_tags, row.names = FALSE)
print(remove_tags)

