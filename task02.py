#SEE HW02.py! Upgraded

import sys
from Bio.Seq import Seq


def main():
    if len(sys.argv) < 2:
        print("Usage: task.py <seq>")
        exit()

    seq = Seq(sys.argv[1])
    print("Original sequence is: ", seq+"\n")

    seq1 = seq[1:]
    seq2 = seq[2:]
    print(seq.translate())
    print(seq1.translate())
    print(seq2.translate())

    rev_seq = seq.reverse_complement()
    print("Complementary reversed sequence is: ", rev_seq+"\n")

    rev_seq1 = rev_seq[1:]
    rev_seq2 = rev_seq[2:]
    print(rev_seq.translate())
    print(rev_seq1.translate())
    print(rev_seq2.translate())



if __name__ == '__main__':
    main()


# "AGTACTAGAGCATTCTATGGAG"
