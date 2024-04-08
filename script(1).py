import argparse


def reg_line(line):
    new_line = [line[0], line[1]]
    for i in range(9, len(line)):
        new_line.append(line[i][0] + line[i][2])
    return new_line


def process_line(line, f):
    # Filter out points that are not the same for white species
    if iden_white(line):
        # Filter out points that are all the same for both species
        tmp = line[-1]
        sample = ""
        is_valid = False
        num = 0
        for i in range(2, 40):
            if line[i] == tmp:
                sample += str(i) + " "
                num += 1
            else:
                is_valid = True
        if is_valid:
            f.write(num + "\t" + line[0] + "\t" + line[1] + "\t" + sample + "\n")


def iden_white(line):
    tmp = line[40]
    for i in range(41, 60):
        print(line[i])
        if line[i] != tmp:
            return False
    return True


parser = argparse.ArgumentParser()
parser.add_argument("--p", required=True, type=str)
parser.add_argument("--out", required=True, type=str)
args = parser.parse_args()


f_out = open(args.out, "w")
with open(args.p, "r") as f:
    for line in f:
        if line != "":
            if line[0] != "#":
                data = reg_line(line.split("  "))
                process_line(data, f_out)
