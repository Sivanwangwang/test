# !/usr/bin/env python
# encoding=utf-8
# author: Xingwang Wang(sivanwangwang@126.com)
# 2017-06-14 13:34

import sys
import re
args = sys.argv


class Genome_info:
    def __init__(self):
        self.chr = ""
        self.start = 0
        self.end = 0


class Gene(Genome_info):
    def __init__(self):
        Genome_info.__init__(self)
        self.orientation = ""
        self.id = ""  # gene_id
        self.name = ""  # 这个是我加的（基因名）
        self.catag = ""  # 这个也是我加的(基因分类）


class Transcript(Genome_info):
    def __init__(self):
        Genome_info.__init__(self)
        self.id = ""  # transcript_id
        self.parent = ""  # gene_id
        self.name = ""  # 这个也是我加的(基因名字）


class Exon(Genome_info):
    def __init__(self):
        Genome_info.__init__(self)
        self.parent = ""


def main(args):
    list_chr = []
    list_gene = {}
    list_transcript = {}
    list_exon = []
    # l_n = 0
    with open(args[1]) as fp_gtf:
        for line in fp_gtf:
            if line.startswith("#"):
                continue
            # print ("in %s" % l_n)
            # l_n += 1
            lines = line.strip("\n").split("\t")  # 去掉换行符，以tab健进行切片
            chr = lines[0]
            type = lines[2]  # gene,mRNA,exon,CDS
            start = int(lines[3])
            end = int(lines[4])
            orientation = lines[6]
            attr = lines[8]
            # if not re.search(r'protein_coding', attr):     #不要没有protein_coding的行
            # continue

            if not chr in list_chr:  # 把染色体号加入列表中
                list_chr.append(chr)

            if type == "gene":  # 如果类型为基因
                gene = Gene()  # 初始化一个基因的对象，Gene是一个类，gene是Gene类的一个实例，这个实例有5个属性
                id = re.search(r'Dbxref=GeneID:(\d+);?', attr).group(1)  # 在属性attr里边匹配gene_id,以gene_id,以0个或者1个;结尾，中间匹配至少一个非;字符
                name = re.search(r'gene=([^;]+);?', attr).group(1)
                catag = re.search(r'gene_biotype=([^;]+);?', attr).group(1)  # 对基因的类型进行分类
                gene.chr = chr
                gene.start = start
                gene.end = end
                gene.id = id
                gene.name = name
                gene.catag = catag
                gene.orientation = orientation  # chr,start,end,orientation是通过切片直接获得，而id通过正则表达式获得
                list_gene[id] = gene  # 以gene_id为健，有5个属性的gene为值放入名为list_gene的字典
                # print(id)
            elif type == "mRNA":
                transcript = Transcript()
                id = re.search(r'transcript_id=([^;]+);?', attr).group(1)
                #print(id)
                parent = re.search(r'Dbxref=GeneID:(\d+);?', attr).group(1)  # 这里的gene_id就成了transcript的parent
                name = re.search(r'gene=([^;]+);?', attr).group(1)
                if not parent in list_gene:  # 如果这个转录本没有gene_id就不进行统计
                    continue
                transcript.chr = chr
                transcript.start = start
                transcript.end = end
                transcript.id = id
                transcript.parent = parent
                transcript.name = name
                list_transcript[id] = transcript

            elif type == "exon":
                exon = Exon()
                try:
                    parent = re.search(r'transcript_id=([^;]+);?', attr).group(1)
                except:
                    continue
                #print(parent)
                if not parent in list_transcript:
                    continue
                exon.chr = chr
                exon.start = start
                exon.end = end
                exon.parent = parent
                list_exon.append(exon)
    #chr_gene(list_gene)
    gene_len(list_gene)
def chr_gene(list_gene):
    """
    染色体上基因数量分布

    :param list_gene:
    :return:
    """

    print("染色体上基因数量分布")
    count_gene = {}  # 新建一个字典(染色体号为健，基因数为值）
    for info in list_gene.values():  # 对于字典list_gene中的值(有5个属性的gene)
        chr = info.chr
        catag = info.catag
        # 提取gene这个类的chr属性
        # print(chr)
        if chr in count_gene:
            count_gene[info.chr]['all'] += 1  # 对已经存在的染色体就累加1
            if catag in count_gene[info.chr]:
                count_gene[info.chr][info.catag] += 1
            else:
                count_gene[info.chr][info.catag] = 1
        else:
            count_gene[info.chr] = {}
            count_gene[info.chr]['all'] = 1  # 对于没有的染色体就是赋值1初始化
            count_gene[info.chr][info.catag] = 1

    with open("chr_gene.txt", 'w') as fp_out:
        fp_out.write('chr' + '\t' + 'type' + '\t' + 'num' + '\n')
        for chr, catag_set in count_gene.items():
            for catag, num in catag_set.items():
                # print("\t".join([chr, str(num)]) + "\n")
                fp_out.write("\t".join([chr, catag, str(num)]) + "\n")  # 用\t间隔合并字典的键值对为一个字符串


def gene_len(list_gene):
    """
    基因长度分布情况

    :param list_gene:
    :return:
    """

    print("基因长度分布情况")
    with open("gene_len.txt", 'w') as fp_out:
        fp_out.write('chr' + '\t' + 'gene_id' + '\t' + 'gene_symbol' + '\t' + 'type' + '\t' + 'start' + '\t' + 'end' + '\t' + 'length' + '\n')
        for gene_id, info in list_gene.items():
            len = info.end - info.start + 1  # 用list_gene字典中的值gene的属性end和start
            fp_out.write("\t".join([info.chr, gene_id, info.name, info.catag, str(info.start), str(info.end), str(len)]) + "\n")
            # print("\t".join([gene_id, str(len)]) + "\n")
    id_number = {}
    with open("gene_len.txt",'r') as fp_out:
        for line in  fp_out:
            if line.startswith('chr'):
                continue
            lst = line.strip("\n").split("\t")
            id = lst[1]
            symbol =lst[2]
            if symbol not in id_number:
                id_number[symbol] = id
            else:
                id_number[symbol] += "| %s"%(id)
    with open("id_number.txt",'w') as fp_out:                  #对单个symbol对应多个id进行统计
        for symbol,number in id_number.items():
            fp_out.write("\t".join([symbol,number]) + "\n")


if __name__ == "__main__":
    main(args)
