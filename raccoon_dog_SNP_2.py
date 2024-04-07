# -*- coding: utf-8 -*-

import argparse
import gzip

# 0~8: info, 9~46 white dogs, 47~66 black dogs
black_start = 9
black_end = 46
white_start =47
white_end = 66
skip_case = "./."

def comp_diff(line):
    # 用一个列表dog_gene装一行里貉子基因表达的部分（例：0/0, 1/1, 0/1, ./., ...）
    tokens = line.split("\t")
    dog_gene = tokens[black_start:]
    dog_gene = [sample.split(":")[0] for sample in dog_gene]

    #一个set装了黑毛的所有基因类型
    black_gene_types = set()
    for i in range(black_start-black_start, black_end-black_start+1):
        black_gene_types.add(dog_gene[i])
    black_gene_types.discard(skip_case)
    #遍历白毛，有一样的就返回false
    white_gene_types = set()
    for j in range(white_start-black_start, white_end-black_start+1):
        white_gene_types.add(dog_gene[j])
        if (dog_gene[j] in black_gene_types):
            return (0, 0)
    return (len(white_gene_types), len(black_gene_types))


parser = argparse.ArgumentParser()
parser.add_argument("--p", required=True, type=str)
parser.add_argument("--out", required=True, type=str)
args = parser.parse_args()

print("Process started...")
f_out = open(args.out, "w")
with gzip.open(args.p, "r") as f:
    for line in f:
        if line != "":
            if line[0] != "#":
                (white_num, black_num) = comp_diff(line)
                if (black_num != 0):
                    f_out.write(str(white_num) + "\t" + str(black_num) + "\t" + line)
