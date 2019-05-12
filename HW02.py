import sys
from Bio.Seq import Seq
from Bio.Data import CodonTable


def main():
    if len(sys.argv) < 2:
        print("Usage: task.py <seq>")
        exit()

    seq = Seq(sys.argv[1])
    print("\nOriginal sequence is: ", seq)
    print("Length of the sequence is: ", len(seq))
    print("CG content is: ",
          round(100 * float(seq.count("G") + seq.count("C")) / len(seq)),
          "%")
    print("\nCodon table:\n ", CodonTable.unambiguous_dna_by_id[1])

    proteins = []
    seq1 = seq[1:]
    seq2 = seq[2:]
    proteins.append(str(seq.translate(to_stop=True)))
    proteins.append(str(seq1.translate(to_stop=True)))
    proteins.append(str(seq2.translate(to_stop=True)))

    rev_seq = seq.reverse_complement()
    print("Complementary reversed sequence is: ", rev_seq)

    rev_seq1 = rev_seq[1:]
    rev_seq2 = rev_seq[2:]
    proteins.append(str(rev_seq.translate(to_stop=True)))
    proteins.append(str(rev_seq1.translate(to_stop=True)))
    proteins.append(str(rev_seq2.translate(to_stop=True)))
    proteins.sort(reverse=True, key=lambda x: len(x))

    print("Amino sequences in decreasing length order are: ",
          *proteins, sep="\n")


if __name__ == '__main__':
    main()


# "AGTACTAGAGCATTCTATGGAG"
# Usage:  /usr/local/bin/python3.7 HW02.py "AGTACTAGAGCATTCTATGGAG"
