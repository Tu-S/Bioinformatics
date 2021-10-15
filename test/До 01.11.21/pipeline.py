data = "big_data"
ref = "ref"
rule all:
    input: "big_data_fastqc.html",
             "ref.fa.amb", "ref.fa.ann","ref.fa.bwt","ref.fa.pac", "ref.fa.sa", "big_data.sam","big_data_stat.txt", "big_data_answer.txt"
rule fastqc:
    input: "big_data.fastq.gz"
    output: "big_data_fastqc.html"
    shell: "fastqc {data}.fastq.gz"
rule index:
    input: "ref.fa", rules.fastqc.output
    output: "ref.fa.amb", "ref.fa.ann","ref.fa.bwt","ref.fa.pac", "ref.fa.sa"
    shell: "bwa index {ref}.fa"
rule mem:
    input: rules.index.output
    output: "big_data.sam"
    shell: "bwa mem {ref}.fa {data}.fastq.gz > {data}.sam"
rule flagstat:
    input: rules.mem.output
    output: "big_data_stat.txt"
    shell: "samtools flagstat {data}.sam > {data}_stat.txt"
rule python:
    input: rules.flagstat.output
    output: "big_data_answer.txt"
    shell: "python main.py {data}_stat.txt > {data}_answer.txt"