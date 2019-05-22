##3


table = {
'A':   71.03711,
'C':   103.00919,
'D':   115.02694,
'E':   129.04259,
'F':   147.06841,
'G':   57.02146,
'H':   137.05891,
'I':  113.08406,
'K':   128.09496,
'L':   113.08406,
'M':   131.04049,
'N':   114.04293,
'P':   97.05276,
'Q':   128.05858,
'R':   156.10111,
'S':   87.03203,
'T':   101.04768,
'V':   99.06841,
'W':   186.07931,
'Y':   163.06333
}

table1 = dict.fromkeys(table.keys())
for key in table1:
    table1[key] = round(table[key], 2)

table2 = dict.fromkeys(table1.values())
for key in table2:
    for x in table1:
        if table1[x] == key:
            table2[key] = x
            break


L = [1988.21104821,
610.391039105,
738.485999105,
766.492149105,
863.544909105,
867.528589105,
992.587499105,
995.623549105,
1120.6824591,
1124.6661391,
1221.7188991,
1249.7250491,
1377.8200091]


n = (len(L) - 3)//2

res = ''
count = 0
i = 1

while i < 2*n+3:
    if count < n:
        for j in range(i+1, 2*n+3):
            diff = round(L[j] - L[i], 2)
            if diff in table2:
                res += table2[diff]
                count += 1
                i = j
                break

    else:
        break


print(res)
