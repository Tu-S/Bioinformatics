ref = "ref"
CONDITIONS, = glob_wildcards("{condition}.fastq.gz")
rule all:
    input: expand("{condition}_answer.txt", condition=CONDITIONS)
rule fastqc:
    input: "{condition}.fastq.gz"
    output: "{condition}_fastqc.html"
    shell: "fastqc {input}"
rule index:
    input: "ref.fa"
    output: "ref.fa.amb", "ref.fa.ann","ref.fa.bwt","ref.fa.pac", "ref.fa.sa"
    shell: "bwa index {ref}.fa"
rule mem:
    input: rules.index.output
    output: "{condition}.sam"
    shell: "bwa mem {ref}.fa {condition}.fastq.gz > {output}"
rule flagstat:
    input: rules.mem.output
    output: "{condition}_stat.txt"
    shell: "samtools flagstat {input} > {output}"
rule python:
    input: rules.flagstat.output
    output: "{condition}_answer.txt"
    shell: "python main.py {input} | comp.sh > {output}"