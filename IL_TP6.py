from collections import OrderedDict

def read_output():
    P = {}
    A = {}
    B = {}
    with open('data/output.txt', buffering=1000) as file:
        i = 0
        for row in file:
            # enlever /n
            row = row[:-1]

            if row.startswith('## Matrice initiale'):
                i=1
                continue
            if row.startswith('## Matrice transition'):
                i=2
                continue
            if row.startswith('## Matrice emission'):
                i=3
                continue

            if i==1:
                # continue
                l = row.split('\t')
                P[l[0]] = float(l[1])
            elif i==2:
                # continue
                l = row.split("\t:\t")
                A[l[0]] = {}
                for k,v in zip(*[iter(l[1].split("\t"))]*2):
                    A[l[0]][k] = float(v)
                    # print k+' -- '+v
            elif i==3:
                # continue
                l = row.split("\t:\t")
                B[l[0]] = {}
                for k, v in zip(*[iter(l[1].split("\t"))] * 2):
                    B[l[0]][k] = float(v)
                    # print k+' -- '+v
    return P, A, B

def read_test():
    L = []
    with open('data/test.txt') as file:
        for row in file:
            row = row[:-1]
            words = row.split(" ")
            l = OrderedDict()
            # l = {}
            for w in words:
                wl = w.split(":")
                # print wl[1]
                if wl[1]:
                    l[wl[0]] = wl[1].split(";")
                else:
                    # print wl[0]
                    l[wl[0]] = [wl[0]]

            L.append(l)
    return L

def viterbi(P, A, B, S):
    # viterbi algorithm
    Q = []
    K = []
    # first element of the row
    first = next(iter(S))
    p = {}
    prev = S[first]
    for lp in S[first]:
        if lp in P:
            p[lp] = P[lp]
        # else:
        #     print '{}\tnot in P'.format(l)
    Q.append(p)
    # print Q[0]
    # print 'S len : {} -> [{}] '.format(len(S),range(1,len(S)))


    # print S
    # for i in range(1,len(S)):
    try:
        it = iter(S)
        # skip the first
        next(it)
        # w : word
        for w in it:
            max = 0

            if len(S[w]) == 1:
                # word have one lemma => only choice
                # K[]
                if not S[w] or S[w] == '-':
                    #
                    continue
            else:
                # l : lemma
                for l in S[w]:
                    if w in B:
                        if l in B[w]:
                            pwl = B[w][l]
                        else:
                            print '{}\tnot in B[{}]'.format(w, l)
                            continue
                    else:
                        print '{}\tnot in B'.format(w)
                        continue
                    # lp : prev lemma
                    for lp in prev:
                        if lp in A:
                            if l in A[lp]:
                                pll = A[lp][l]
                            else:
                                print '{}\tnot in A[{}]'.format(lp, l)
                                continue
                        else:
                            print '{}\tnot in A'.format(l)
                            continue
                        if pll*pwl > max:
                            max = pll*pwl
                        print '{}\t->\t{}\t:\t{}\t'.format(lp, l, pll* pwl)
            print 'max : {}'.format(max)
            prev = S[w]
            print '--------------------'

    except Exception as e:
        print 'Exception : {}'.format(e)

    return K

def Q(Q):
    max = 0


    return max

# try:
P, A, B = read_output()

S = read_test()

# for k, v in P.items():
#     print('{} -> {}'.format(k,v))

# for k, v in A.items():
#     print('{}\t->'.format(k))
#     for l, p in v.items():
#         print('\t{} : {}'.format(l,p))

# for k, v in B.items():
#     print('{}\t->'.format(k))
#     for l, p in v.items():
#         print('\t{} : {}'.format(l,p))

# for s in S[0]:
#     print('{}'.format(s))
    # for k, v in s.items():
    #     print('{}\t:\t{}'.format(k, v))

# for s in S:
#     viterbi(P, A, B, s)

viterbi(P, A, B, S[1])

# except Exception as e:
#     print 'Exception : {}'.format(e)























