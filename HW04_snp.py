import re
import sys
import random
import warnings

def create_snp(n, seq):

    snp_pos = random.sample(range(0, len(seq)), n)
    answer = []
    for pos in snp_pos:
        new_snp = random.choice(('A', 'C', 'G', 'T'))
        while new_snp == seq[pos]:
            new_snp = random.choice(('A', 'C', 'G', 'T'))
        answer.append([seq[pos], new_snp, pos])
        return answer


def process_file(filename, n):
    print("SEQ_ID  |  MUTATION  |  POSITION-OF-MUTATION")

    with open(filename) as f:
        for line in f:
            seq_id, seq = re.split(r'\s+', line.strip())

            mutations = create_snp(n, seq)
            for mutation in mutations:
                print(f"{seq_id: <22}{mutation[0]: >10}->{mutation[1]}\t{mutation[2]}")


def main():
    if len(sys.argv) < 3:
        print("Usage: HW04_snp.py <path_to_seq> <SNP#>")
        exit()

    filename = sys.argv[1]
    n = sys.argv[2]
    n = int(re.sub('\D', '', n))

    try:
        open(filename)
    except FileNotFoundError:
        print(f"No such file: {filename}")
        exit()

    smallest = n
    with open(filename) as f:
        for line in f:
            seq_id, seq = re.split(r'\s+', line.strip())
            smallest = min(len(seq), smallest)

    if min(smallest, n) != n:
        warnings.warn("X in SNPX is bigger than the length of the shortest string in a file", Warning)
        n = smallest

    process_file(filename, n)


if __name__ == '__main__':
    main()


""""Type into console "python3 HW04_snp.py ./prom.txt SNP3 """
