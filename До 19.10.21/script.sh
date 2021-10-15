#!/bin/bash
echo 'file paths= ' $1 $2
fastqc $1.fastq.gz
mv $1_fastqc.html $1.html
rm $1_fastqc.zip
bwa index $2.fa
bwa mem $2.fa $1.fastq.gz > $1.sam
samtools flagstat $1.sam > $1_stat.txt
python main.py $1_stat.txt
