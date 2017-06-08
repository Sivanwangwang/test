import sys
import re
 
args = sys.argv    #实现从程序外部向程序传递参数
 
 
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
        self.name = ""    #这个是我加的
        self.catag = ""   #这个也是我加的
 
 
class Transcript(Genome_info):
    def __init__(self):
        Genome_info.__init__(self)
        self.id = ""
        self.parent = ""
        self.name = ""    #这个也是我加的
 
 
class Exon(Genome_info):
    def __init__(self):
        Genome_info.__init__(self)
        self.parent = ""
 
 
def main(args):
    """
    一个输入参数：
    第一个参数为物种gtf文件
 
    :return:
    """
 
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
            lines = line.strip("\n").split("\t")   #去掉换行符，以tab健进行切片
            chr = lines[0]
            type = lines[2]                        #gene,transcript,exon,CDS,start_codon,stop_codon,five_prime_utr,three_prime_utr,Selenocysteine
            start = int(lines[3])
            end = int(lines[4])
            orientation = lines[6]
            attr = lines[8]
            #if not re.search(r'protein_coding', attr):     #不要没有protein_coding的行
                #continue
 
            if not chr in list_chr :                       #把染色体号加入列表中
                list_chr.append(chr)
 
            if type == "gene":                             #如果类型为基因
                gene = Gene()                              #初始化一个基因的对象，Gene是一个类，gene是Gene类的一个实例，这个实例有5个属性
                id = re.search(r'gene_id "([^;]+)";?', attr).group(1)   #在属性attr里边匹配gene_id,以gene_id,以0个或者1个;结尾，中间匹配至少一个非;字符
                name = re.search(r'gene_name "([^;]+)";?', attr).group(1)
                catag = re.search(r'gene_biotype "([^;]+)";?', attr).group(1)   #对基因的类型进行分类
                gene.chr = chr
                gene.start = start
                gene.end = end
                gene.id = id
                gene.name = name
                gene.catag = catag
                gene.orientation = orientation   #chr,start,end,orientation是通过切片直接获得，而id通过正则表达式获得  
                list_gene[id] = gene             #以gene_id为健，有5个属性的gene为值放入名为list_gene的字典
                # print(id)
            elif type == "transcript":
                transcript = Transcript()
                id = re.search(r'transcript_id "([^;]+)";?', attr).group(1)
                parent = re.search(r'gene_id "([^;]+)";?', attr).group(1)          #这里的gene_id就成了transcript的parent
                name = re.search(r'gene_name "([^;]+)";?', attr).group(1)	
                catag = re.search(r'gene_biotype "([^;]+)";?', attr).group(1)   #对基因的类型进行分类				
                if not parent in list_gene:                                        #如果这个转录本没有gene_id就不进行统计
                    continue
                transcript.chr = chr
                transcript.start = start
                transcript.end = end
                transcript.id = id
                transcript.parent = parent
                transcript.name = name 
                transcript.catag = catag
                list_transcript[id] = transcript                              #
 
            elif type == "exon":
                exon = Exon()
                parent = re.search(r'transcript_id "([^;]+)";?', attr).group(1)
                if not parent in list_transcript:
                    continue
                exon.chr = chr
                exon.start = start
                exon.end = end
                exon.parent = parent
                list_exon.append(exon)                                         #
 
    #chr_gene(list_gene)
    #gene_len(list_gene)
    #gene_transcript(list_transcript)
    #transcript_exon(list_exon)
    #exon_pos(list_exon)
    #gene_exon_pos(list_gene, list_transcript, list_exon)
    gene_exon_pos1(list_gene, list_transcript, list_exon)
    gene_exon_pos2(list_gene, list_transcript, list_exon)
    #gene_exon_pos3(list_gene, list_transcript, list_exon)
 
def chr_gene(list_gene):
    """
    染色体上基因数量分布
 
    :param list_gene:
    :return:
    """
 
    print("染色体上基因数量分布")
    count_gene = {}                          #新建一个字典(染色体号为健，基因数为值）
    for info in list_gene.values():          #对于字典list_gene中的值(有5个属性的gene)
        chr = info.chr
        catag = info.catag
		#提取gene这个类的chr属性
        #print(chr)		
        if chr in count_gene:
            count_gene[info.chr]['all'] += 1        #对已经存在的染色体就累加1
            if catag in count_gene[info.chr]:
                count_gene[info.chr][info.catag] +=1
            else:
                count_gene[info.chr][info.catag] =1
        else:
            count_gene[info.chr]={}
            count_gene[info.chr]['all'] = 1         #对于没有的染色体就是赋值1初始化
            count_gene[info.chr][info.catag] =1
			
    with open("chr_gene.txt", 'w') as fp_out:
        for chr, catag_set in count_gene.items():		
            for catag, num in catag_set.items():
            #print("\t".join([chr, str(num)]) + "\n")
                fp_out.write("\t".join([chr, catag, str(num)]) + "\n")  #用\t间隔合并字典的键值对为一个字符串
 
def gene_len(list_gene):
    """
    基因长度分布情况
 
    :param list_gene:
    :return:
    """
 
    print ("基因长度分布情况")
    with open("gene_len.txt", 'w') as fp_out:
        for gene_id, info in list_gene.items():
            len = info.end - info.start + 1                 #用list_gene字典中的值gene的属性end和start
            fp_out.write("\t".join([info.chr,gene_id,info.name,info.catag,str(info.start),str(info.end),str(len)]) + "\n")
            #print("\t".join([gene_id, str(len)]) + "\n")
 
def gene_transcript(list_transcript):
    """
    基因的转录本数量分布
 
    :param list_transcript:
    :return:
    """
 
    print("基因的转录本数量分布")
    count_transcript = {}
    for info in list_transcript.values():
        gene_id = info.parent
        if gene_id in count_transcript:
            count_transcript[gene_id] += 1
        else:
            count_transcript[gene_id] = 1
    with open("gene_transcript.txt", 'w') as fp_out:
        for gene_id, num in count_transcript.items():
            #print("\t".join([gene_id, str(num)]) + "\n")
            fp_out.write("\t".join([gene_id, str(num)]) + "\n")
 
 
def transcript_exon(list_exon):
    """
    转录本的外显子数量统计
 
    :param list_exon:
    :return:
    """
 
    print("转录本的外显子数量统计")
    count_exon = {}
    for exon in list_exon:
        transcript_id = exon.parent
        if transcript_id in count_exon:
            count_exon[transcript_id] += 1
        else:
            count_exon[transcript_id] = 1
    with open("transcript_exon.txt", 'w') as fp_out:
        for transcript_id, num in count_exon.items():
            #print("\t".join([transcript_id, str(num)]) + "\n")
            fp_out.write("\t".join([transcript_id, str(num)]) + "\n")
 
def exon_pos(list_exon):
    """
    外显子坐标统计
 
    :param list_exon:
    :return:
    """
 
    print("外显子坐标统计")
    count_exon = {}
    for exon in list_exon:
        transcript_id = exon.parent
        if transcript_id in count_exon:
            count_exon[transcript_id] += ",%s-%s" % (str(exon.start), str(exon.end))
        else:
            count_exon[transcript_id] = "%s-%s" % (str(exon.start), str(exon.end))
    with open("exon_pos.txt", 'w') as fp_out:
        for transcript_id, pos in count_exon.items():
            #print("\t".join([transcript_id, pos]) + "\n")
            fp_out.write("\t".join([transcript_id, pos]) + "\n")
 
def gene_exon_pos(list_gene, list_transcript, list_exon):
    """
    根据exon的parent将所有exon对应到transcript
    根据transcript的parent将所有transcript对应到gene
    根据gene按chr分组得到chromosome列表
 
    从chromosome中输出某个指定基因的所有外显子坐标信息并画图
    生信编程直播第五题
 
    :param list_gene:
    :param list_transcript:
    :param list_exon:
    :return:
    """
    print("基因——转录本——外显子坐标统计")
    gene_transcript_exon = {}
    count_exon = {}
    count_transcript= {}
    for exon in list_exon:
        transcript_id = exon.parent
        if transcript_id in count_exon:
            count_exon[transcript_id] += ",%s-%s" % (str(exon.start), str(exon.end))
        else:
            count_exon[transcript_id] = "%s-%s" % (str(exon.start), str(exon.end))
    print("count_exon_finished")
    for transcript_id,transcript in list_transcript.items():
        gene_id = transcript.parent
        if gene_id in count_transcript:
            count_transcript[gene_id].append(transcript_id)
        else:
            count_transcript[gene_id]=[]
    print("count_transcript_finished")
    for k1,v1 in count_transcript.items():
        gene_transcript_exon[k1]={}
        for i in v1:
            for k2,v2 in count_exon.items():
                if i==k2:
                    gene_transcript_exon[k1][i] = v2                                    #这种写法要耗费50min
                    #print(k1+i)
    #print(gene_transcript_exon)        
    with open("gene_transcript_exon.txt", 'w') as fp_out:
        for gene_id, transcript in gene_transcript_exon.items():
            for transcript_id, exon_pos in transcript.items():
            #print("\t".join([transcript_id, pos]) + "\n")
                fp_out.write("\t".join([gene_id, transcript_id,exon_pos]) + "\n")
def gene_exon_pos1(list_gene, list_transcript, list_exon):
    """
    根据exon的parent将所有exon对应到transcript
    根据transcript的parent将所有transcript对应到gene
    根据gene按chr分组得到chromosome列表
 
    从chromosome中输出某个指定基因的所有外显子坐标信息并画图
    生信编程直播第五题
 
    :param list_gene:
    :param list_transcript:
    :param list_exon:
    :return:
    """
    print("基因——转录本——外显子坐标统计")
    gene_transcript_exon = {}
    count_exon = {}
    count_transcript= {}
    for exon in list_exon:
        transcript_id = exon.parent
        if transcript_id in count_exon:
            count_exon[transcript_id] += ",%s-%s" % (str(exon.start), str(exon.end))
        else:
            count_exon[transcript_id] = "%s-%s" % (str(exon.start), str(exon.end))
    print("count_exon_finished")
    for transcript_id,transcript in list_transcript.items():
        gene_id = transcript.parent
        chr = transcript.chr
        name = transcript.name
        catag = transcript.catag
        all = "\t".join([str(chr),name,catag,gene_id])
        if all in count_transcript:
            count_transcript[all].append(transcript_id)
        else:
            count_transcript[all]=[]
    print("count_transcript_finished")
    #print(count_transcript)
    for k1,v1 in count_transcript.items():
        gene_transcript_exon[k1]={}
        for i in v1:
            gene_transcript_exon[k1][i] = count_exon[i]                                  #这种写法只要几秒钟
            #print(k1+i)
    #print(gene_transcript_exon)        
    with open("gene_transcript_exon1.txt", 'w') as fp_out:
        fp_out.write("Chr"+"\t"+"Gene_Symbol"+"\t"+"Type"+"\t"+"Gene_ID"+"\t"+"Transcript_ID"+"\t"+"exon_pos"+"\n")   #加个列名
        for gene_id, transcript in gene_transcript_exon.items():
            for transcript_id, exon_pos in transcript.items():
            #print("\t".join([transcript_id, pos]) + "\n")
                fp_out.write("\t".join([gene_id, transcript_id,exon_pos]) + "\n")
def gene_exon_pos2(list_gene, list_transcript, list_exon):
    """
    根据exon的parent将所有exon对应到transcript
    根据transcript的parent将所有transcript对应到gene
    根据gene按chr分组得到chromosome列表
 
    从chromosome中输出某个指定基因的所有外显子坐标信息并画图
    生信编程直播第五题
 
    :param list_gene:
    :param list_transcript:
    :param list_exon:
    :return:
    """
    print("基因——转录本——外显子坐标统计")
    gene_transcript_exon = {}
    count_exon = {}
    count_transcript= {}
    for exon in list_exon:
        transcript_id = exon.parent
        if transcript_id in count_exon:
            count_exon[transcript_id] += ",%s-%s" % (str(exon.start), str(exon.end))
        else:
            count_exon[transcript_id] = "%s-%s" % (str(exon.start), str(exon.end))
    print("count_exon_finished")
    for transcript_id,transcript in list_transcript.items():
        gene_id = transcript.parent
        if gene_id in count_transcript:
            count_transcript[gene_id].append(transcript_id)
        else:
            count_transcript[gene_id]=[]
    print("count_transcript_finished")
    for k1,v1 in count_transcript.items():
        gene_transcript_exon[k1]={}
        for i in v1:
            if i in count_exon:
                gene_transcript_exon[k1][i] = count_exon[i]
    #print(gene_transcript_exon)        
    with open("gene_transcript_exon2.txt", 'w') as fp_out:
        for gene_id, transcript in gene_transcript_exon.items():
            for transcript_id, exon_pos in transcript.items():
            #print("\t".join([transcript_id, pos]) + "\n")
                fp_out.write("\t".join([gene_id, transcript_id,exon_pos]) + "\n")
				
def gene_exon_pos3(list_gene, list_transcript, list_exon):
    """
    根据exon的parent将所有exon对应到transcript
    根据transcript的parent将所有transcript对应到gene
    根据gene按chr分组得到chromosome列表
 
    从chromosome中输出某个指定基因的所有外显子坐标信息并画图
    生信编程直播第五题
 
    :param list_gene:
    :param list_transcript:
    :param list_exon:
    :return:
    """
    print("基因——转录本——外显子坐标统计")
    gene_transcript_exon = {}
    count_exon = {}
    count_transcript= {}
    for exon in list_exon:
        transcript_id = exon.parent
        if transcript_id in count_exon:
            count_exon[transcript_id] += ",%s-%s" % (str(exon.start), str(exon.end))
        else:
            count_exon[transcript_id] = "%s-%s" % (str(exon.start), str(exon.end))
    print("count_exon_finished")
    for transcript_id,transcript in list_transcript.items():
        gene_id = transcript.parent
        if gene_id in count_transcript:
            count_transcript[gene_id].append(transcript_id)
        else:
            count_transcript[gene_id]=[]
    print("count_transcript_finished")
    for k1,v1 in count_transcript.items():
        gene_transcript_exon[k1]={}
        for i in v1:
            for k2,v2 in count_exon.items():
                if i in count_exon:
                    gene_transcript_exon[k1][i] = count_exon[i]
                    #print(k1+i)
    #print(gene_transcript_exon)        
    with open("gene_transcript_exon3.txt", 'w') as fp_out:
        for gene_id, transcript in gene_transcript_exon.items():
            for transcript_id, exon_pos in transcript.items():
            #print("\t".join([transcript_id, pos]) + "\n")
                fp_out.write("\t".join([gene_id, transcript_id,exon_pos]) + "\n") 
if __name__ == "__main__":
    main(args)