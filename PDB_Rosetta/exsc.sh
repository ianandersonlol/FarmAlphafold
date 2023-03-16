#!/bin/bash
if [ $# -lt 3 ]; then
    echo "USAGE: extract_best_score_decoys.sh <silent file> <score term name> <number of best scoring models> "
    exit
fi
file=$1
score=$2
num_models=$3
grep "SCORE:" $file > score_"$file".txt
head -1 score_"$file".txt > head
findColumn.pl $score head > c.txt
column=`awk '{print $4}' c.txt`
grep "SCORE:" $file |sort -nk $column | head -$[$num_models+1] | tail -1 > line
cut_off=`awk '{print($'"${column}"')}' line`
cull_silent.pl $file ""$score"<"$cut_off""
mv *_SELECT.silent "$num_models"_best_"$score"_"$file"
rm head line c.txt score_"$file".txt
