# !/usr/bin/env python
# encoding=utf-8
# author: Xingwang Wang(sivanwangwang@126.com)
# 2017-06-14 13:34
import sys

args = sys.argv  # 实现从程序外部向程序传递参数


class Genome_info:
    def __init__(self):
        self.chr = ""
        self.start = 0
        self.end = 0


class Gene(Genome_info):
    def __init__(self):
        Genome_info.__init__(self)
        self.orientation = ""
        self.id = ""

def main(args):
    list_chr = {}
    with open(args[1]) as fp_gene:
        for line in fp_gene:
            if line.startswith('#'):
                continue
            lines = line.strip("\n").split("\t")
            id = lines[0]
            chr = lines[1]
            start = int(lines[2])
            end =int(lines[3])
            orientation =lines[4]

            if not chr in list_chr:
                list_chr[chr] = {}
            gene = Gene()
            gene.chr = chr
            gene.start = start
            gene.end = end
            gene.id = id
            gene.orientation = orientation
            list_chr[chr][id] = gene

    with open(args[2]) as fp_pos:
        for line in fp_pos:
            gene_list =[]
            lines = line.strip('\n').split('\t')
            (chr,start,end) = (lines[0],int(lines[1]),int(lines[2]))
            for gene_id,gene in list_chr[chr].items():
                if gene.start <= start <= gene.end or gene.start <= end <= gene.end or start <= gene.start <= end or start <= gene.end <= end:
                    gene_list.append(gene_id)
            print(gene_list)

if __name__ == '__main__':
        main(args)



