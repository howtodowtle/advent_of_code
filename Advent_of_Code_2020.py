#!/usr/bin/env python
# coding: utf-8

# In[60]:


get_ipython().system(' jupyter nbconvert --to python Advent_of_Code_2020.ipynb')


# # 1

# ## 1.1

# In[2]:


url = "https://adventofcode.com/2020/day/1/input"


# In[3]:


get_ipython().system(' curl {url}')


# In[4]:


inp = """1962
1577
1750
1836
1762
1691
1726
1588
1370
1043
1307
1552
1813
1804
1765
1893
1610
764
1512
1404
1711
1000
1694
1546
1880
1721
2006
1787
1510
1850
1420
1712
1926
1707
1983
1680
1436
389
1448
1875
1333
1733
1935
1794
1337
1863
1769
1635
1499
1807
1326
1989
1705
1673
1829
1684
1716
456
1696
1398
1942
1851
1690
1328
1356
1775
1564
1466
1273
1896
766
1814
1810
1537
1463
1755
1341
1665
1520
1366
1387
1976
1717
1737
1551
1760
1496
1664
1450
1319
1674
1630
1301
1330
1658
1637
1655
1439
1832
1948
1339
1656
1449
1296
1489
1758
1939
1857
1402
1394
1882
1446
1412
1430
1212
1377
1501
1873
1812
1667
1560
1654
1575
1999
1581
1792
1299
1843
1383
1351
1297
1822
1801
1977
1316
1477
1980
1693
1220
1554
1607
1903
1669
1593
1955
1286
1909
1280
1854
2005
1820
1803
1763
1660
1410
1974
1808
1816
1723
1936
1423
1818
1800
1294
857
496
1248
1670
1993
1929
1966
1381
1259
1285
1797
1644
1919
1267
1509
399
1300
1662
1556
1747
1517
1972
1729
1506
1544
1957
1930
1956
1753
1284
1389
1689
1709
1627
1770
847"""


# In[5]:


import itertools as it


# In[6]:


def aoc_1a(inp=inp, sum_is=2020):
    list_of_numbers = [int(n) for n in inp.splitlines()]
    check = lambda x, y: x + y == sum_is
    for pair in it.permutations(list_of_numbers, 2):
        if check(*pair):
            print(*pair)
            return pair[0] * pair[1]
    print("No combination found!")
    return None


# In[7]:


aoc_1a()


# ## 1.2

# In[8]:


def multiply_nums(nums):
    product = 1
    for num in nums:
        product *= num
    return product


# In[9]:


def aoc_1b(inp=inp, n_numbers=3, sum_is=2020):
    list_of_numbers = [int(n) for n in inp.splitlines()]
    check = lambda nums: sum(nums) == sum_is
    for nums in it.permutations(list_of_numbers, n_numbers):
        if check(nums):
            print(*nums)
            return multiply_nums(nums)
    print("No combination found!")
    return None


# In[10]:


aoc_1b()


# # 2

# ## 2.1

# In[11]:


inp = """5-10 b: bhbjlkbbbbbbb
3-4 j: hjvj
8-9 p: pmljtsttp
3-4 t: hvtttqhdjmmnbqwbgfs
4-6 m: mblwtzmvmdjkkmmtsckm
6-9 f: ffffftfff
1-3 g: xggg
3-10 k: rwkhttkxxdpnlkq
3-11 w: wwmwwwwwwwww
5-7 f: fffffffff
1-4 l: lglllbc
2-5 n: njnnn
6-8 t: tcjtltttttdttjttbt
10-20 d: djddddccdbdddddddndd
2-5 z: gzppzhrhzdthnpcr
13-14 p: plvppptppppzppbkpk
11-13 t: jjtjvzfhsrtsmkdhj
11-12 r: rtrdvrrxrrxrzr
2-6 x: dxsvxgvk
7-11 x: hcxxpvxrnmxckkq
12-17 s: sssssssssssrssssss
2-4 v: vvpvvvjvvjvvqbvv
15-18 h: thqhhhgjjqhhnhhznz
8-11 j: jbmgbtmjtbb
2-4 d: xxdfvp
2-7 p: fftlppz
9-13 d: dfddddddsdddds
5-7 d: ddddddz
2-3 h: hfbhhh
1-4 k: rmkvkkkk
16-17 w: wwwhwwwwwwwwwwwwq
5-8 l: gllxllnlqlglrplk
1-7 p: mhnpspp
5-13 f: qhwffbtfzmdffztfjs
2-8 f: fkjhvcbflbwhggtbbcb
2-3 m: bcmldxmdh
6-7 p: ppcpppw
3-10 m: mmmmmmmmmj
4-12 s: ssjssssssssmsss
2-5 j: rmjnjtjjjj
2-3 q: qqdqq
10-15 v: vvvvvvvvvvvvvvdvvvvv
1-4 w: wwwc
4-14 m: mmsmmmvmmmmmqqmmmmm
7-10 d: ddcdddzdddddd
4-5 h: hhhhh
9-17 p: ppppppppqppppppppp
6-7 m: mqtmnms
4-5 s: pssss
2-6 t: tdttttpwttt
7-8 l: llsxsllzlwl
7-10 f: fflffffkqffffm
3-4 f: cdfp
3-4 z: zzzz
6-7 s: sbssdvs
3-4 g: ggdv
11-16 l: lllllnbsqlfzwrfljkh
3-4 k: tqkxxfk
3-17 s: xshmvlmzrjdpnvlssn
1-16 l: lzzvllgktckllmlltl
5-6 l: qlltvl
6-7 p: npvbpcp
4-6 g: gmgvgn
12-13 r: rrnlrrwrtvrrrrcrrrv
11-12 h: hhvxhhhhwjhd
13-14 p: pdppcsjtppppppvtwpj
10-14 l: hljjkjxlfwzlllclzq
18-19 z: zzzzzzzzzzzzzzztzhn
11-12 p: hpspwrkqbnpp
16-18 h: hhhhhhghhhhhhhhwhbh
1-2 p: vpxnqqbgrxprmh
13-19 m: mmmmmmmmmmmmqmmmmqm
1-2 n: ncndsnl
9-10 x: xxxxxxxxxgxxd
9-12 w: wwwwwwwwwwzwwdfgwwp
3-5 h: nqhvhzb
4-5 j: jjjns
10-12 f: ffffffffffff
7-10 v: mgvrwvvsjw
3-5 m: wpmmm
3-10 s: ffsbvjdslsnshqs
9-10 z: mgzzbjzqsz
3-13 d: ddjdddddddddnd
2-4 l: tqkfhpwvvmc
1-3 z: zzzzzn
3-5 l: ctljlckdpnlchrzbc
6-7 v: hqvcvvv
11-13 v: vvvvcvvvvvvvvvv
8-9 t: ztndmlwdb
5-6 v: fdxxrvwpw
1-4 n: xnkb
16-17 v: vvvvvvvvvvvvvvvvnvv
12-14 b: bbbbbxbbbdbgbcb
1-7 w: wwwwwwrwwjtwk
3-10 d: bxnhbhrmgd
4-5 k: kkknkk
2-4 n: bndln
3-10 p: vpkppcppppcplpksp
9-10 d: fhbzbdzqsdxlhnbt
11-13 z: zzmzzzzwzpzzz
12-17 b: hkbcbbhthbrbbdgbl
11-13 c: cpccnxccxbjtm
5-6 n: nnrmnfnsnn
3-8 l: sslkllwljcgl
1-9 p: fpppzzpppppphtrhppp
4-11 h: kskbvrqhdjph
3-9 r: rsrvxnrchtrrrr
4-5 n: nwbln
3-4 g: gjgv
13-14 r: rrrrrrsrtrrrrrrrr
10-15 m: mmmmmmmmmtmmgmm
5-6 k: wkpkkqk
10-11 l: wlbllglkbltblrqlllm
6-7 d: ddddsrddd
17-18 v: vvvvvvvvvvvfvgvvsvv
6-10 n: nngnnnnvnknn
7-8 t: qdztnrnt
5-11 d: dfbdxqbmsdd
1-6 n: znnvqdnx
7-9 k: kkkkkkkkl
5-6 m: mmmszmtmmks
1-5 l: wlllllll
13-14 m: mcmmmmmlmmmmjmmm
1-7 k: kklkjvckb
14-15 d: ddddmddddmddddddd
18-19 k: kfkkkkkkkkkkkkkkkpkk
3-4 z: czjzc
17-18 t: btttttjmltrttxctgt
1-4 c: cccscqcccc
9-14 k: tcwcstszkvhjfmrqpkp
3-8 c: ccccccjcscncp
10-11 d: dddddddddmdd
3-5 m: rgmfmkmd
1-5 k: mfhnk
4-5 x: cwnxftlt
1-3 n: flnqmnnhnn
2-5 f: vwlcnsfd
4-8 c: cccccccbc
10-12 v: dhfvlvbvspjldzch
7-16 f: ffsmffffjffqfpffff
10-13 n: njtrrnnqntjtn
13-17 f: frffcfffrjffffdfpff
5-10 m: mmmmvfmmmmmmmmdm
5-6 v: vvvvvzvvvvv
6-12 r: dqrrcrhrhjsrrr
8-14 z: zzzzzzzlzzzgzsz
5-9 q: qkwzsvwdg
12-13 d: vzjfvddgctfdrr
6-7 f: mgndffb
2-5 x: nxxmx
7-9 c: cmxsccccf
1-7 n: nnnnnnnnnn
6-8 g: gggglfgp
2-13 v: kvwxcrfmpfcfdrgv
5-7 p: tpplpffpccpp
8-12 m: mmmmmmmmmmmxm
9-10 v: vvvvvvvvvcv
4-5 m: mbnmmkknmmwshmkthj
8-9 t: cltntrtpqwtcsftttf
8-16 f: ffffrffpffffffffff
6-8 t: sttcctttdttdwjdndtt
5-9 k: ckkkkvdkvkk
1-3 f: ffczfpgmf
2-4 w: wwlwwd
1-9 d: lddbhdddmtfdmdzdrdhd
16-17 h: xfqlbhhpbnclvztzzzx
2-7 r: rrbntqrrsrkrm
1-4 r: qwrr
12-14 b: tvbbzjbbbbbbbn
5-7 h: hhjvghth
2-3 d: dndrcx
8-9 c: ccccscccpc
5-8 s: srcsszcsp
13-15 g: gggggggglggggglggggg
11-13 b: bbbbbfrbfbbgbb
1-8 b: jbbkqbbbpbbbbbbp
11-14 n: nnnnnnnnnnmnnnn
1-4 g: qsggg
14-15 l: sllslllggllljkdlm
1-5 s: pvssbspdsshsssssrs
7-10 c: ccccccmcpgcc
6-14 m: bcfkpmvmcmmjml
1-3 n: ncnnnnn
12-14 j: bjfjxjjpjrjjjxjjk
10-12 v: vfvvvvvvqjvvvwvwt
6-13 d: stddxdnjrddhwgdhrfjf
5-6 w: qcwhnwwk
2-3 x: mcxfxckptzvw
12-20 b: lvgvbxsxxlvbhfcxbtzr
1-2 d: ddbdqd
5-10 h: mhtnjvhhhs
2-6 z: ztzzdxzzzqbvg
2-7 t: ttjkqztr
3-4 g: bgvggrxrhtlklfj
4-5 q: qqqvq
1-3 c: ccpc
4-6 j: jjrdjj
8-11 c: ncvshccccccsb
1-2 z: rzzqxczxbkpvgkxfzgvz
10-11 f: kffsffffbqf
18-19 v: vmvvvvvvvvvvvvvvvql
14-15 m: mmmmmmmmmnmmmpmm
12-17 z: zzzzzzzzczzdlzzzzz
4-6 g: zggggg
12-16 h: hhhfhhrnnkhhmhhtqvh
3-4 n: hxssbnn
6-9 m: mmmmmmmmdmmm
5-6 n: nnwtgn
6-10 c: lppbvxcmjc
7-8 d: dpddzddvdzdddzfddd
1-5 z: xlzmzzz
6-11 h: hjhhhphhhhf
1-9 h: hhdghtsmmjhhnnwz
6-9 t: ctldsstttstrz
3-4 t: qvktfwnjcjtqtjqtn
6-7 w: wwwwwwsww
11-12 m: nphmmmpmmmcm
8-9 p: ppppdppdp
12-13 l: cllzzglllbqlll
2-7 s: sslssssgbssbsssnss
6-14 j: jvjrxjjrlgvjzmgj
7-8 p: hxpnjvzqxm
2-10 g: xgzfgvdsxr
4-5 t: lttttxdtp
3-12 c: kkpckmphqfcc
4-7 v: rbsjcpvwgtfjpv
2-4 k: swqfkb
5-9 n: knfdnnnnn
12-14 t: zgwthtdtrxvvftst
3-5 v: vlvqtv
15-19 t: fqwkwbtjdqncnsmnqxr
3-8 c: mxccchksq
3-5 v: jtpvr
5-7 k: kbkkkshkkkzkkkt
8-9 z: zzzzzzzzzzz
6-13 k: kkkkkkkkkkkktkkk
5-7 c: mccchbwc
7-12 x: gxxxxlgmztwsxxxgj
3-12 b: ndsbdfdgvxtbmrqcrjhs
1-3 d: qxdtdt
3-7 b: qbbdbgb
12-15 p: ppmplpptppwppppg
7-8 r: rjrrrrrz
8-10 p: cppppgspsxpvp
1-5 w: wwwpwf
4-8 p: nhqlknppmpplb
1-6 c: cvccccrc
7-8 c: cccccctccccccc
4-12 x: jxrxtnxrxxvsx
9-15 g: jfgxnznpwhccdggnm
2-6 h: jphhphlvhgqbwnl
8-9 f: dfftbfxsxxqfdvlfs
1-12 t: dtttttttttttttt
3-7 h: hshhmhh
3-4 w: wwwj
5-6 z: zzzzzp
8-12 m: jmnwmtjmnqvrj
4-5 f: ffffvff
8-10 l: llllflllxll
4-8 x: zcvxtxxkm
13-15 p: pppppkppppbpppsp
3-6 h: hhhhphlhhghkt
2-13 t: tcttttjtttttltttttt
9-10 b: bbbbbbbbvb
7-8 w: fwbwwwqw
6-9 s: jssssssssssssssssw
13-17 p: pppppppppppppppppp
5-7 q: lqxcqqqqcmgtbqjrqmjg
4-17 t: tttpfttttjttttttvt
13-14 c: cccccccccccccj
1-2 p: pxrpqpmpp
3-8 l: rnlxbwwzjdsh
2-7 w: kwkghnsfcp
9-11 m: mmdrktmzmrzhmgdmg
8-11 z: wzxwzzbfznc
5-7 t: rtbtntt
2-3 v: nqvv
2-3 r: krrwb
10-11 q: qqqqlqqvqqqqqq
3-5 r: drrhh
7-9 f: ffffffffhv
4-13 m: rkmmbjnsjzjcmwmwk
15-17 s: jrrvwtnklssqshzpss
12-13 z: fczzpzzzzzzkl
10-12 z: jshkxzzzrdzj
6-13 k: kkkkkkkkkkfkgkkkkkk
14-15 w: wcjjlzkpbspcwcw
2-5 n: npnnznk
5-15 b: cgqlmxzqmvqzbvb
13-15 r: rrrprrrrrrrrlrr
5-6 z: pgfzxw
4-17 x: xlgxwsxjxdxxhqhtcj
11-16 z: zzjhzzlzrzkzwzlzz
7-8 b: tltbbrbbbkb
2-14 k: pnkkqfxkkqkkmkkdkjkk
1-3 f: hjmvjfxvxtgh
6-8 w: xgrvwwswwxg
16-18 v: vwvvvvvvvvkvvmvvvtv
3-10 w: wwwwwwwwwwwww
2-4 w: zcwwqwtdwj
3-7 r: ttrrnwszwqsp
1-7 m: mjjqlgm
12-15 x: xxxxxxxxxxxlxxnxx
3-6 z: zzzzzjz
8-9 s: sssssssvs
5-7 w: wlwswwd
17-18 z: zzzdzzzzzzzzzzzzzx
5-7 j: dchcjfj
2-5 k: cqpkn
8-10 x: xxxnxxxxxtx
1-5 t: tttttttt
5-6 k: lkkphk
11-13 c: scdtdcghdmcttcc
2-5 h: hhhhhh
4-6 r: clrrrr
2-13 s: szsssssssssssssv
3-11 x: krxmwcznvwrlcx
7-8 m: cmmttmbm
3-4 c: pdwccbxwfvhcgrx
5-8 p: ppppvppq
12-19 l: llfllrllmwlmlllllll
11-15 p: psplppzglptmppp
6-14 m: mmvmmgmmmpmmmxm
5-6 j: jjctdzj
9-10 k: xnkzkkpplpkkkkk
10-14 t: crsttgdtzgfqtx
6-7 j: jbkpsjjjsrzf
1-4 v: vsvvvvm
4-5 f: lhbnfgqmbfltqrxzzx
12-13 q: qrjkxcwqqkdjmsxfnqmf
18-19 q: qqpqqxzqjnqqbhqkqqv
16-20 m: nzbmqjwbmmmnhmlmszbf
5-9 k: kkkkxskkkkk
1-2 x: txhxx
9-12 s: sssssssssssr
3-4 s: qsssssh
19-20 f: mfffmpfhhffwrlkffvff
3-15 b: bbpbbbbbbbbbbbbbb
8-9 h: fbcjphblh
6-9 p: ppppbnpppfppw
6-20 n: nsxzcgbcgqvjwfrgtnsr
5-7 s: cssdjdssr
3-4 g: gggwgg
1-6 s: hsspsss
2-5 z: zlgzb
5-8 l: jsljljtlpqhjl
3-10 n: mznwwnvhgbg
2-3 c: cckcc
1-10 r: rrpcbdrrrr
16-17 q: kqjxngwrpqlsqklnq
2-4 n: mnmnn
8-9 n: nnnnnnnsrnl
2-4 r: qrhlrvwpqsvktzcqms
6-9 v: vbqlvvvhqvqpv
2-8 b: kngrzdbb
10-13 d: dddddddddwdddd
2-6 z: czkzhzqdffh
8-19 n: kngnjnftdsrnhsnmznn
8-10 m: rngxfjlmmvtctp
16-17 k: dlkkxxkkkczkkkkkvs
3-17 n: wllsknnzckmmsjmqnxc
11-12 h: csrhwxwdnkhh
3-7 g: ggggggngg
1-14 s: sssssssssssssssdl
8-16 m: mmmmmmmkmmmmmmmpm
8-9 b: kdbqtknpncbbffd
14-15 z: zjzzszcgnzczszg
12-16 g: jdvgrmdczssgtwsq
2-6 n: lwlklnfxlhwdkn
1-5 c: bnfbdzc
14-15 b: bbbbbbbbjbbbbtb
2-5 v: vnvvvvv
14-17 s: ssssszssssssssshmsss
7-9 h: fhmhjkcrhbl
11-15 g: fwhjldbbprhngcjg
9-15 m: mdcbhmmjlmfmmtmcmm
10-13 j: jjjjsjjjjlwjsjjl
1-5 s: dsssssssssssssssss
5-15 r: rrxprrrrrrrzvhrrrrr
5-7 b: svnbkbb
2-4 w: kwwqws
13-20 q: slgmkqmkvlqqwjfdhqdq
8-12 l: llllllljlllkll
9-20 c: cccccccccccccccccccc
5-6 n: wlcnnh
1-4 w: lzwwv
8-9 h: hhphhhhhhhdhh
8-10 t: mnsnktzgrn
11-16 v: bjvcvfrkgkvzvvvxb
11-18 v: vvvvvvvvvvvvvvvvvxvv
11-14 l: llllkllllrlqll
5-11 q: zwlqcqqnnqq
5-11 p: pftpphptptphtskqp
4-12 p: pvpwpzppppppppdk
2-4 h: hhhqhh
6-12 l: jznsrcnxkllz
13-15 j: vdjkhxjptxzfjjm
4-5 t: vzhft
7-10 m: bmrmztmwxmms
5-7 h: hswmtbhcb
13-17 f: vmhffvvfjtffpllftff
11-16 w: wqntqwmzcwwvhwwsxwlh
2-4 r: wrbb
2-10 b: bbbbbbbbbb
1-11 m: mmmmmmmmmmmmmmmmmmhm
13-14 r: rrrrrrrrrrrrrwrrrr
3-6 n: vnsprwznfn
3-4 v: vvvz
2-11 p: ppxjqmffgtp
7-10 s: sslmsssssss
10-11 j: jjlsjjjjjfjjj
4-7 b: fbbhggbcmr
12-13 s: sssssssssssgxs
8-10 l: lpllllhlcnlllxl
3-4 l: ljxlml
2-14 f: ffffffwfffzfcnfffwrf
7-10 h: kwdcfptcchhhhhgz
2-9 j: jjjjjsmjzjqjjj
4-13 w: wwcwwwmrwwwgqwr
3-5 t: ttmtttt
5-13 d: whpdqwpvkzsxdmgtnz
13-14 x: xxtbcxxxwxxxxx
1-7 t: ttttttdthtttttttt
6-15 x: pxfnxbnmpxgmwzxkv
2-11 m: kmcmjlddbwm
9-14 d: dddddddddddddldd
6-9 x: nxvkxvxxx
18-19 x: xsxxxrdxbkjmbdvfrrx
12-13 j: jnjjjgjjqrjjs
14-16 r: rrrrrmrrrrqrrxrvrvr
5-9 h: hhvvhmzjn
5-6 w: wwgfzt
10-13 v: vvvvvsvvvtvvxvvrvvv
2-4 h: hwhh
4-8 s: ssssssshss
5-12 n: nnnnnnnnnnncn
2-3 x: bxxmxcdzlj
14-16 x: chpxcprsxhxvkxzc
7-9 b: bbbbbbbbbb
10-11 x: xxskpxtfhxd
5-7 w: zwwwrww
1-8 l: splxkhxw
8-9 q: llcbqltqh
2-3 k: kkcckxm
6-11 c: ccccsccccccccccccccc
6-14 k: xkbbnkknkttqpb
12-16 d: dcddddrddnddvprsd
1-3 p: bpplj
4-6 n: nntbnpn
14-15 k: nwcckxptkgrrbkd
12-14 d: dddddddddddddxd
1-11 v: vvvvjvvvvvvvvv
4-6 g: gtgbfg
5-8 h: hhhhdhhhhhhh
13-15 n: nwnnpnftnbnknqn
3-4 m: mpfqmj
3-6 t: ttmtct
2-4 s: sssss
10-16 v: vvszvvgvvvvvvvvcv
11-13 t: stvdjtwjzftrtprpb
5-6 p: pppptp
12-15 d: ddtdjdddxdhxzdcd
12-16 b: bbbbbbbbbbbxbbbbb
12-14 n: qnnnnnnnnzlnnnn
9-11 v: sqkrmzjqvvv
2-5 d: cdpfdtjdkn
7-8 p: pppptppppp
2-4 s: ssszsss
13-15 d: cpdwdbvqxcffdrd
4-5 j: hbjjpppm
5-8 g: gvgmgjgrzz
6-7 s: sssssqn
1-11 p: tpstkbpmtbpg
17-18 m: zmmmsrsrgfpggmmmlgk
2-3 f: ffkhf
2-5 f: ftfff
2-10 m: gqxlmphwcmfc
6-8 v: bvgwwbvlvvvlrvv
13-14 n: nnnnnnnnnnnnnxn
2-7 f: ffffffff
9-10 x: xxxxxxxxxd
1-7 s: mssssdsksssdsssz
11-15 t: jtttttltmttgttthz
5-12 j: jqjjjjfndzjdjjjjjjjn
9-13 r: rrrrrrrrrrrrj
5-9 x: xxjxpcqxxcxznn
2-9 c: psdddswdcpd
4-10 f: fsffxffffmr
7-12 j: jxvjjjrjjhjfc
4-5 q: bqqhj
1-4 f: fwbclqb
1-2 k: skqk
9-11 b: bbbzbkbbhbb
1-2 g: nggv
3-7 m: mmfmmmpm
2-3 m: vpmr
7-10 d: ddddddjddm
2-15 t: hgvsftrbzglvmpwhsmp
1-5 t: qtttt
11-13 p: pppppppppppphp
4-5 p: cvqpzvpppfh
2-3 f: bbftxfnmb
2-3 r: rlrr
1-4 m: mvms
3-14 m: gfmprfxpvzhmhm
2-8 j: jdsjjlfl
8-12 k: kkkkskkvkkkkk
1-7 p: hpfpmpwp
5-8 x: xxxxxxxhxxxxxx
3-10 p: mmctgfppppxplpplppj
3-4 p: zfmpjbhwppk
13-16 z: zzzzzzzzzzzzvzzzz
1-3 d: djddd
2-7 p: nmplwdp
7-9 l: lglllllll
7-8 p: ptvsnpcp
9-10 m: rjnmxthbmg
5-6 j: jjccjv
6-8 t: tvcztdttxzkp
8-12 p: kmrpqdnppskj
6-8 j: lsjkhjjhbgj
11-12 x: hxxxlxmxxxtrxxxxk
3-6 p: pppppcgtpxpppplp
8-10 s: nphsvswsrssxmdh
10-11 p: pppcpptppkp
14-15 z: zzzzzzzzzzzzzcz
14-18 f: mffngzbffffznctfff
6-7 t: tttthhtttq
12-19 l: shqlqnkzwpplqjrwjcv
1-4 k: khkx
9-11 d: ddddddddpdrdddd
3-4 s: mvsssc
6-7 h: hhhhhhphh
8-14 v: vvrvsvwrwmpvlv
2-6 z: zxjvsn
9-12 f: ffffffffpfftf
2-5 s: lssmjh
11-14 k: kkwkkfkbpnjkbkk
4-15 x: ppcxmjmxvbrkxlqcthx
1-2 g: bpggz
3-5 x: vxjxxxnztm
7-8 r: rrrrrrrhr
8-13 n: nnblnxnnrmnnq
1-4 w: wwtxwwwjwwwwdwl
1-10 d: cddddddwfhdrdddqnd
1-8 j: jxmjjjrv
4-7 x: xfxxxxn
16-18 v: vvvvvvvvvvvvvvvvvvv
3-5 h: hhhhhh
9-11 z: zzztvzzhgzr
3-5 w: fcjwwjwwv
6-7 z: hszgzsl
3-9 l: fldswlflrll
10-11 n: fqbxpfncbln
7-14 m: jftmkxqhrmmcqmk
8-9 h: hhqqhkhmh
3-5 l: lnlqlhdjtd
4-11 x: lqjxqzlfsfhzjqqnttp
4-6 c: fccctcc
8-11 c: cccccccccckcr
2-3 k: jkxtkjhnkksksrrzhfkk
7-9 m: nmmmmmmkmrmmdjjms
5-12 m: mmmmprmsmbmmmm
1-2 l: lllll
3-7 m: gmmtchm
11-16 t: vddbsztmpttvsktp
9-13 f: ffffffffffffffffff
3-8 j: hjhldbcznnsx
5-7 v: vrfpvswbmbvvzv
6-15 z: bhlvbzvnlntzzzz
4-6 x: xzjrxcx
3-4 q: qqsw
5-6 r: rrrlrrrrrr
1-7 b: qbbbbbxbbb
6-7 b: bfbbjdd
4-11 f: lfrffpfgzqs
3-5 c: qccncmjgrczzmcz
9-15 x: vxxxxxnxxxxxxxxrxxxj
1-2 s: ssnls
5-9 z: zzpzzzzzszzzzzz
5-16 z: pzgzxgpwqmzwwlzz
6-7 c: ccqxccn
5-6 b: ngmbbs
2-19 d: cdmnqfjfxgtdwlrnhcd
9-12 p: thcvkgpcxptpxpp
3-6 g: sbstjvnhfgdr
1-18 f: fsffffffffffffffffff
2-16 f: rfxzxrjpbvfzcftf
13-14 v: rvxvvnsfcvvvrvvvqg
4-10 d: tqlddkdpdv
12-13 r: rrrrrrrrhrwrjdrlnr
5-6 x: xxvxgnxxxx
3-4 d: sddd
5-11 p: jphgprgjjpp
1-7 f: fjgfdvb
3-8 x: rpxvndgxx
1-17 b: jbbrxbbbtxjbrpbbb
7-10 h: bhhbzmdrkhhvhjx
1-5 v: fzdgv
5-7 f: vfdffftffffhflw
2-20 c: mcbhcvvxwxfvxqlgxpdc
5-8 w: vwktjwdsccgj
3-4 d: nntd
1-7 n: nnncmhnkgqn
2-6 r: bdvvbrr
1-15 b: bbbzwbbbbkbgkbp
3-8 f: slfvsmvftsstff
3-4 z: pvzzggdnhwzjzgp
8-9 n: nnnnvnnfn
4-10 n: nnnlnngnncnn
8-10 l: vktfwjrmslbh
3-6 n: nflmqn
4-5 s: svggkxz
3-4 w: wwjt
5-6 t: nbbbdt
3-8 d: jrjkdghxqwq
7-8 q: qqqqqqgq
7-8 k: qxgnkvckpkchqnmxb
1-5 v: vvvvvv
6-16 s: stmjwhvrrkfgrsxs
3-4 s: sdrswqnsjrnhrlds
12-15 r: rgdrrrrrrrrrrrgtg
12-14 g: gggggggggggjgggggggg
1-7 h: phhhhhdnhj
3-4 v: tknvv
10-11 j: jjbvjjxjjjjj
2-5 c: bcbff
7-11 r: rrrrrrxrrrdrrrrr
13-16 p: ppppppppppppdppr
14-16 t: tttttttvtttttttwttt
3-6 c: hclhccxhmxtjcbmjc
1-2 x: gxxxxx
2-3 w: wrwcqt
2-6 g: gmblggxgg
1-4 l: lllxpkml
1-2 d: mdddddd
4-8 q: qqqxqqqqq
3-4 v: mwvfvlqvv
3-6 w: wswwgc
2-4 d: bdfd
17-19 l: llllsldlbllllnlllzr
10-18 j: tjhgvshtbqjtcfcvlr
4-9 t: ttttttttttfttttttt
8-9 g: ngsggnbgqgtgglnjgcg
9-10 d: dddhdddvgbdbd
8-9 g: gtggvpgmq
11-15 j: jjqkjsmjkgfvjns
6-9 t: tqthttvtnttttttg
1-7 j: sjjjjjjjjjjjjjj
15-16 g: gggggggzgghgggqd
10-16 n: nnnnnjnnngnnnnnnnn
1-6 p: pppppppp
1-2 k: kdkk
1-2 b: bjvzqrgbhmgm
2-4 x: xvxxx
1-5 j: zjjjjjjj
2-5 f: lfnpwfz
1-12 j: hjjjjjjjjjjj
7-10 l: lllllqhlllllmmlpllll
11-12 m: mmmnmnmmmmmmmm
6-8 z: dzzzzfzzpz
14-15 c: cshjrbzhmmpckcwf
3-5 q: qqqqz
11-12 z: zzzzdzczzkprvztzfrdd
4-5 t: ttstbt
14-15 k: kkkkkkqkkkkkksr
1-12 j: jjjjjjjjjjjwgcjzj
2-3 k: rhkhkkg
1-16 z: zrzzzzkkhzzflzzzlzzq
12-13 h: hhhhhhhhhthgjhh
1-5 j: qqjjczwttz
11-12 h: hhhhhhhhhhmk
1-3 p: qpspbpjfq
1-3 f: ffzf
11-16 f: qdfmgnfnfvffflfhff
12-14 b: btwsgnvvljknbbdf
7-15 b: wdrgltbgdqscbhh
3-13 j: vwjpjjwjtcpjk
2-4 l: clxdsfqfdvkfhcgdswl
9-13 m: mmmmmmgmmpnmmmzmmk
4-5 x: hxxxx
1-4 b: bbbb
4-5 r: rrrrwfrv
6-9 n: nnnnnnnnsn
4-7 m: mvmmmmdmm
4-12 t: ttttttjtttttjttttt
1-3 c: bccc
2-3 m: mmcxbw
1-4 r: rrrrrr
8-10 l: lllllllplllllllll
18-19 h: hbhjdhhnnhfshkhhhgh
6-8 h: hfhwhwph
1-4 z: cfmz
2-3 m: vtmmznmvmrs
7-8 l: llhlwzlmjll
1-2 m: mmskncxdc
1-4 d: ndddd
1-3 m: mmgmmm
14-15 r: nzrgmcrrgmrxlbr
2-13 h: htkhhhhhhqhhlhhhkh
2-4 w: wkwsw
3-4 w: wmwr
2-9 v: kdzkhvnkv
8-9 t: wltttttkbktftk
9-14 n: vnhdtndfnsncpnf
3-10 n: jfnwcngtdz
13-15 j: nqzdlvnvvgnmhjj
1-12 q: qqqqqqqqqqqqq
10-12 c: cccdcmscbhcqccc
1-3 w: bzwwgg
2-14 d: pdkrpmxxzgcvqkzvvzqd
6-11 t: tfqvhtbmdztsnwnt
5-9 l: xllmllvjdds
6-14 h: pkhthnhxhhhjnscb
5-7 m: mmmmrmmm
8-10 x: xxxxxxxwxkxxx
4-5 k: lmkkkkkskg
1-2 d: dtdd
5-7 f: frfwsfr
4-5 w: rclww
4-5 g: gkkmtnlhbkgb
4-6 q: qqqfqqq
3-4 d: ddjb
11-13 n: nnnnnnnnnnnnnnnn
4-6 f: jvkxcffdgd
3-4 g: ktsgxzn
14-15 g: gggggggggggggggg
2-3 n: nqnnn
2-12 k: kbkpppkrkkjkkkk
5-7 c: ccccbcccc
9-10 l: plmrklsclx
4-11 m: mmmtmmmmmmqlm
6-7 b: bbbbbbq
7-9 g: kcgggklzg
3-6 p: ptxpppppppppppp
2-4 s: swsss
7-10 c: cccccccccpcc
5-7 d: dbddlddddcsdd
6-7 k: kkkkkkk
2-4 h: hwnvcj
1-9 g: nggggggggg
9-19 b: dzzpzvgwbdbmthmzfbhb
1-6 v: vrclmqxpvkhbvrfdmc
4-7 k: sgwktwtttmktrfjzn
13-16 x: whxxxxxxxxxxxxxsxx
4-9 z: zzzpzzzzzz
7-9 t: mwvtbhtxt
2-3 j: jfjdj
3-9 t: nrkffvgmtdstkkhtfpn
3-4 g: ggggxxdjsgrbf
4-10 x: kgbxbqnqmc
7-10 t: ztndqctmtttthxkwtlm
8-12 h: fbvccdshdvhhh
9-12 f: ffffsfffffjd
1-3 q: qkqqrvmmkh
13-14 r: rrrqrrrrrrrrrrrrrrr
2-3 g: bmdgkz
6-7 k: kkkkkkjk
4-9 q: qgzrflqqqd
12-13 s: brsswsfsvsfssps
5-9 q: drjcqnmwqbncmqqvcjgh
7-9 x: xxpxxgzxxxnx
2-13 s: ssdsssssjshsjsjswn
1-11 m: fmmmmmmmmsmmmh
3-8 f: zffrqqhflhvl
4-11 l: lqfwlxlllnl
12-16 k: kkkkkkkkkkkdkkkgkkkk
1-5 s: sssslss
3-13 n: ntnnnnpnnlndsnn
13-16 f: nzpfvhfrxpxjfmcfff
2-3 f: ffbf
3-7 r: nxrrrqrqnrrlbj
1-10 p: mppptppppcpppppppd
9-11 l: ftmflbbljjf
6-8 r: rrrrrlrrrr
10-16 k: zqknmwppdtckmpgk
10-13 t: dpqxttttttttb
2-4 f: ftff
9-14 k: krkkkqkkkkdkkrn
12-17 b: mbxbczbbbbdbbbbbpbnb
8-9 j: bjjjjjjjqjvxjfjjjjjj
1-3 s: lspsh
2-7 p: zpqlvwpmdp
6-8 q: qqqqqqqtqq
15-16 z: cxzmdcdzckrhzxzz
13-17 v: vvvvvvvvvvvvvvvvzv
6-8 c: ctcccccc
6-7 v: xjzvvfvjmnrvtvncjmdv
3-8 m: sqmfbqlm
3-9 p: bpqpxpfpzqpjjgv
8-10 n: clxnnnxvnnxnnnnnn
8-9 m: mmmmmmmmm
2-6 s: scssss
9-10 t: xtttttttftttt
3-5 c: rksck
16-17 h: ldhchxlhphlnmhvhh
3-6 b: bnbvlb
4-5 j: mjjjx
2-4 j: sklkmtrjpgprqdn
3-8 l: nllnlnll
1-6 g: jgbgpt
14-17 d: cqddcfsjddddxlcdd
4-6 h: qcqhwc
6-14 j: fzrkcjrqjssjdjjjjj
3-4 j: jdfj
1-3 k: fkpkkkck
11-12 w: wwwwbwwwwwfg
6-7 g: wngnhsg
4-13 d: bddjdddddddddpdddddd
7-8 k: kmkfkkkp
5-9 b: btmlgzbbdb
4-7 j: dxlzwsjdbjcqjsnwq
9-13 p: pppppmfhpptppp
16-17 v: vvvvvvvvvvvvvvvxn
1-7 m: mmmmmmtmm
1-8 v: vvvvvvvbv
9-15 t: tttttttttttttttt
15-17 r: rwrqrrhdrtvrfszrj
4-9 m: mfddknmcmqhglr
7-10 k: kkkkkkkkpkklkk
18-19 c: hpqwwkgtqbrcjxptwnc
2-3 p: xwppdp
5-11 r: vnrhrmknrrr
10-15 f: ffmfffffcfftfdfff
10-13 m: mmtsmmmmmmmmhmm
4-16 j: pjlplfvtgrjhvcdjjdmb
8-14 v: kxrjvdbbmxvrzdp
6-7 w: wwwwwwgwww
9-16 f: hhkvlfrvfvpvlzvcfsg
1-3 k: kkbk
9-12 d: ddddddddtdddd
13-16 w: wwwgwwwwwwwxwwwwwww
4-5 t: swtttpkkpwdt
5-7 z: zzfzzzp
1-5 g: grghg
3-4 n: wjsnnnwsxrx
8-10 x: xxxxxxpqxc
4-13 t: tttbtttttttttttt
1-3 w: wswwn
1-6 d: dddtddddd
12-13 x: xxflxxpxxxxxwgrxxx
1-2 m: mxghmm
6-11 j: jjjjjjjjjjxj
1-3 n: nnfnnnnnnnn
7-11 w: wxwwwwpwwwww
1-2 q: nqmqfxql
9-12 m: mmmmvmnmfmmp
5-7 m: mmmmmmms
3-4 s: ssqsssssssj
6-9 c: ccvcmnccccl
1-17 b: gbbbbbbbbbbbbbbbqbb
7-10 q: vqqqqxqqql
9-12 v: vzvvnvtblzrq
7-8 q: qqqqqqqs
4-8 q: qtzqcgbqwq
7-9 c: ccncdmxsccchcxxj
3-6 q: qqqjlqqxcqdkzqqj
3-4 k: qckk
10-12 c: cccccccccccc
10-18 g: gggggggggggggbgkggn
2-3 w: wwww
1-4 k: kkglkqkgzbn
6-7 l: lklksztlzllllp
8-10 x: xxxxltxwxnxdvcg
1-5 w: tvmjw
3-9 z: hvqqhmpzz
6-8 x: qzxxdxnxmlgp
13-17 s: ssssqsssssssjssssxs
2-8 f: qfhnhfzc
3-4 v: vvbv
4-6 j: jjjmjj
3-4 q: lqqd
12-14 j: jjjjmjjjjjjcjjjj
6-9 c: whjbsclch
14-15 j: jgjjcjkljjmfpjqjjjk
2-3 z: jbzt
12-13 b: bbbbbbbbbbbqj
3-9 s: jhcsgnsscs
6-8 h: hhhlhlhf
3-4 j: jmjjcwjpj
10-11 c: cccccccccdcccccc
11-12 w: wswwwwwwvwww
17-18 k: rmzbkcsxrmdwkksstk
7-8 h: hhhhhthh
1-2 n: nnqcqlxdsc
4-11 l: llllllllldlql
14-20 h: hhhhhhhhhhhhhhhhhhhh
4-8 r: bhwrrrrrrgrwcmr
5-16 m: lmdbtwhnzszltgjmhfcb
4-12 m: mmmvmmmmmmmmm
1-5 t: qtwnztcftsqjh
4-12 s: ssdszsssssvslx
16-18 w: wwwwwwwwwwwwwwwrwq
7-8 t: ttttttttt
8-10 r: mxrrrrrrrc
10-12 g: gggggtpghggsgvcdpjlg
7-13 q: qlqqpqdqqqqqnqqqq
7-9 z: zzzzzgzzd
13-16 c: ccccccccccccxccb
4-9 l: jbsssqpjl
7-12 s: sslsssdksnsssqmrsc
9-14 w: cwqsssmkbgwmqzrw
1-5 v: vljdvzqvgjhcgbn
4-7 w: nxqxgww
7-9 w: wwwtwlwqxwww
14-18 q: qwncqqqjmmlzqqqqnq
2-8 g: ggggggggg
5-6 g: ggpgkgg
12-13 r: rrrrrrrrrrrph
14-15 c: cswccccccvccmcs
11-15 p: jppxbqzcdzppxjv
6-9 f: fffnfffdcc
7-10 x: xnrdxxtwxx
2-6 s: gdshsbcsssss
5-9 d: dwtcdddffsdzdzcvbdd
2-3 l: kqlfjqj
7-9 s: tmsklsfsp
2-4 c: lkbck
2-9 x: jtxslmdpxpkqfjjb
18-19 v: vvvvvvvvvvvvvvvvvmd
9-10 x: zgxdjvxqxgxkcm
11-12 d: dddqddddddvdddd
1-4 d: ddlvd
2-4 t: tztfwtjwt
5-6 j: gjjsfjgvjjcwzjm
8-11 g: kvsqgmqgdmgxdpg
6-11 b: bpjbfrrpbvb
1-10 j: tmjjjjjjbjcjjjjjj
14-18 t: tttttttttttttttttttt
11-12 r: rjjvggmpwvrhn
10-12 t: tttttttttctttt
1-8 s: lbssjsssgsss
4-12 h: pchchhtthdhhch
7-8 m: mhrpkbmdmj
5-6 f: sffdsf
4-7 z: zzzkzzkzzzz
1-5 c: nccjw
1-2 l: wsgllckll
1-9 k: mwvhwgvfkvmpwnntjbk
1-6 v: vvvvvvvvvvv
2-8 m: ttzhlrrmbt
3-4 x: xqklgxxx
12-13 v: rvvvvvvvfvvmvv
6-13 n: nnnnnnnnnnnnnn
5-6 s: bpnsssj
3-9 q: xtddtwfcstjrqbslmjsz
8-9 g: xxkxxgzgg
1-12 w: gwwwwwwwwwwtw
4-5 p: pppppp
1-2 x: jpxvxxxxxnmkx
3-4 n: ddnn
5-6 t: ztkmttmb
2-5 j: rrcjj
2-5 s: lccgw
5-6 f: fffflfff
3-4 h: ptbh
2-3 s: sssgm
6-8 g: gggggpggg
3-4 d: qrll
8-15 b: zbxpbbbbbbhbbbpbp
2-3 r: rrrr
13-15 c: cdccqkcvckcccvc
10-15 z: hxctzzvzzzzbfzz
3-4 q: qwtqqncqcdxq
1-6 l: jlllsl
5-6 g: ggggbxggggrggggg
4-6 m: mmmsmdmpmmmm
5-9 d: ddddddqdgddd
2-19 d: dxdddddddddddddddddd
8-9 z: zzzzztzpzqzzdh
7-12 j: jjfjsmsxjwjjvtcbjb
2-10 l: dxkrwjbvlsgpzcmk
13-14 h: hhhhrqlhhhhhhhh
2-8 v: jvvvvvvjv
13-14 q: qqjqqqfjqqqqqz
5-12 d: pllddwcgctfbkfx
17-18 f: ffffffffffffffffmjff
7-17 w: sqmbczwtwpwkhngtw
15-17 l: lllllllllllzllplllll
5-8 c: cccqfccccccc
8-14 k: xnjcftlkvhkmkr
4-5 q: qqqqqj
8-11 m: wzxcmwgmmvmgq
11-15 h: hnhtnhnhhkghhzhh
11-13 g: rgdgqgvmqjggg
8-13 v: mtjkbnvvvhvvv
4-5 v: vcvhv
5-12 w: fqvwnzcwlntwpcwf
1-15 j: jjjjjjjzjjjjspwj
2-4 x: jmrxxkpncwdcftw
1-2 b: gbbqbf
8-11 k: kxkkkkzpkkzkkm
1-4 v: mpqp
6-7 p: lxdptfp
3-4 s: sxss
16-18 d: gxzglqmddffqxqvppr
4-6 f: fffmfff
13-16 m: zfmcnzxfvmcmqmhcctv
1-8 n: nnnnnnnm
8-9 v: vvvvvvvvvg
"""


# In[12]:


import re


# In[13]:


def parse_line(line):
    min_ = int(line.split("-")[0])
    max_ = int(re.findall(r"\d+-(\d+) \w: \w+", line)[0])
    letter = re.findall(r"\d+-\d+ (\w): \w+", line)[0]
    passwd = re.findall(r"\d+-\d+ \w: (\w+)", line)[0]
    return min_, max_, letter, passwd


# In[14]:


def check_line(line):
    min_, max_, letter, passwd = parse_line(line)
    this_many = passwd.count(letter)
    return min_ <= this_many <= max_


# In[15]:


def aoc2a(inp=inp):
    lines = inp.splitlines()
    return sum(check_line(line) for line in lines)


# In[16]:


aoc2a()


# ## 2.2

# In[17]:


def check_line_2(line):
    pos1, pos2, letter, passwd = parse_line(line)
    lp1, lp2 = (passwd[pos1 - 1] == letter), (passwd[pos2 - 1] == letter)
    return (lp1 or lp2) and not (lp1 and lp2)


# In[18]:


def aoc2b(inp=inp):
    lines = inp.splitlines()
    return sum(check_line_2(line) for line in lines)


# In[19]:


aoc2b()


# # 3

# ## 3.1

# In[20]:


inp = """.#......##..#.....#....#.#.#...
.#.#...#.##.#..........#...##..
.........#.....#.####........#.
.......#.#...#.#...............
..#....#...#.#...#.#...#.#.....
...#...........#..#.........#.#
....#..#....#..#..#.#...#..##..
#...........#..#.....#.......#.
#..#...#...#.###...#...#.#...#.
#...#.#.......#...#...#...##.##
..#..................#.#.#....#
..#.##....#........##..........
.....#....#....#.#.......#.....
##.#..##.#.....###.......#.....
......#...###....#..#.#...#....
..............#.........#.##...
#......#.............#....#...#
.#..#......#.###....#...#.....#
..#........#.....#.....#...#..#
.......#...#..............#..#.
..#...#........#...##........#.
.#........#....#......#......#.
....#..#.###.......##....#.#..#
..#..###..#....................
......#...#....#.........#.#...
....#.##................#..#...
....#......######.....#........
.#......##.......#....#..##.###
..#...##.###..#.......#....#...
....#.###...#.#.#........#.....
...###...#.......#..........#.#
..........#...#..........##.#..
..#....#........#.....#....#..#
..#...#.#....##..#...##....#...
........##...#..##.....#.......
###.......#.#...#...#.......#.#
....#.#....##.###........#.....
.....#..............#....##..##
#......#.#....#.#......#.....##
.....#....#..#......#...#......
..#.##..#.....#..#....#......#.
.....#.#.#..........##....#....
.........#..#..........#.#.....
.##..#...#......#.#..#....#....
#.#..##.......#.#......##......
..#.#....#.#.....#.............
.#.........#.......#..#.#......
##.........#..##.#......#......
#..#.....#...#.....#.........#.
..........#..##..##.#..##...###
..##.....#...#..##...##.#.#....
..#..........#.#.....##.#....#.
.##..#..#.........###.......#..
......##....#...##....##.......
.....#.#.##...............#....
#..#......#.....#..#..#.#.....#
.....##.#....#.#.....#.#.#.....
....#..#.#..##....#.....#....#.
#...#.....#....#....#.#.#......
.....#................#.......#
.......#..#.#...#.#......#..#.#
...........#....#....###...#.#.
#.##....##..###.#.#......#.##.#
..##...#.#..#..#...#.....#.#.#.
#.....###.#..#.#...#.#......#.#
..##.#...#...#.#.....#.#.......
#....#...#.##......#.#......#..
..#.....##.....#...............
.....###...##.#...........#....
...#..##.....##....#...........
.....#..#......#..........#....
....##..##.#...#...#.#.....#.##
.#.....###..###.#...#.#..#....#
.#..........#...#..#.#.#..#...#
.##.##..#..#....#....####......
....#..#.#..........#..........
###...#.#..#..#...#..###.......
####.#...#....#..#...#..#......
.....##....#.#...#....##....##.
....#.#.##....#.##..#....#.#.#.
#......#..#.###....#####.##....
..##..#.#.#..#........##.##..##
#.#...#..#..#......#..#.....#..
.###.....#.#....#.#..##.....#.#
....#......#.#...#...#.#....#.#
.....#.###.##..................
.#..........#........#.#...##.#
.##......#.#.#..#....##.###..#.
..#.##....#....#.........#.#..#
........#..#..#.#.####.....##..
#..#.##.#......#.#..##.#...#..#
..#.#.##..#.##..........#......
##.#.....#.#.##..#..##.....##.#
.##........#..#.....#...#.##.##
...#....#.#.#.........##.....#.
...#....#.#....#...#..#........
.....#...#..#...#.##......##...
##.........#......#..........##
.#......#.....##....#.#.#.....#
..#.###......#..#.#....#.....#.
.#.......#...#...#.#.#.#..##...
...#..............#...###.....#
...##......#.#..#.#........#.#.
..##.#....#..........##...#.#..
..#...#.....#.######...##...#..
#...#...#............#.....#...
.###..###.##..#.........#......
.#........##..#....#...#.#..##.
#.#.##.#.#...###...............
..#.#.#......#.#.#....#.....#.#
.#...........#.##.#..#.###.....
.###.#....#...........##.#.#...
.#...#...........#..##.........
.#...#.#...........#..###....#.
.##.......#.....#.....##....#..
#.......#........#...##.##..#.#
....#..###..#.....##.......#...
......###.#...#..#....#.#...#..
..#..#.......##...#.#.#...#....
......#..#.......#.......##.#..
#.#....###.....#...#..#...#....
#...#.##.#........#..........##
.....#.#.##.#.#..#..##.......##
.#.#.......##....#.#...........
#..##.............##...#.#..#..
#...........#.#......#.##.##..#
...#...#...........#....###.#.#
.##..#.#.#....#....#####.......
..#...#.....#.#....#...........
.#..#........#.....#.#......#..
.#.........#...#...#.#.#..#....
.##.##......#.#...#.......#...#
.##...#..#..........#...#.....#
#..........#..#...#.#......#...
....##......#...##..##..#....#.
.##.......#...#.#..##..#..#....
.#.#................#....#.....
..#..#..###.......#............
...##.....#..#......#....#.....
....#...###...#....#..##...#.#.
#.........#.......#...#....#...
.#.#...#.#....##....#.#..##.#..
...#..#..#....#..#.#..##.....##
..#..#.#.#....#...#....#..#....
......###.....#...##.#..#.#...#
.#.#.#..#.##........#.#....#...
.#..........#....#.#.......#...
#.....#........#........#....#.
.#.#..#...#...................#
....####..#..#..#..#....#..#.#.
..##.#..........#.##..#.....##.
..................##..........#
....##....###.....#..#...#.#...
.##.........#..#...............
....##..###....#.##............
#.#...###.#..##...#...........#
.....#..#......#.....#.........
..#..##...#.....#.....#.#......
......#....###.#..#.#.#....#..#
#...#.......#.##.....#.........
.#.#..#...#.............##.....
......#..............#.....#..#
......#......###....#...#......
.....#.....#...#.......###.....
#..........##......##.#.#.....#
....#.......#..#......#.......#
..#...#.###...........#..#.###.
.....#...#.#...........#.#...##
........#.#.#........#.#.....#.
....##..##.#.#..#.#....#.#.##..
..#.#.#......##.....#...#.#...#
##...#..#......#.#.#..#...#....
....#..##...........#..#..#..#.
.#..##...#...#...##.#..#.#....#
.#.....####.#..#..#....##..#.#.
.#....#..#......#.....#.#.#....
....#..#.....#......#..........
..#.#..###.....#...#...#.....##
..#.#...##..#...........####...
.#.##....##.#......#.....##.#..
#.##..#....#.###..........##...
.###...#......#.#....##........
...................#..#.....#..
#.#...#.#..#.....#...#..####.##
....#.##..##...##.##.....#.....
.#...#.##...........#.......##.
###..#.....##...#.........##...
.###....##...###...............
.#....#####........#.#.#.##....
.#.#....####.##........#.......
.....#......#..................
......###.....##......#..##.#..
....#.#...........##.#....##.#.
...................#.#.#.......
#.#.#........#..#.......##.....
..#...#...#....#......#....##.#
#..#..............#......#....#
......#.........##.............
.....#.#....##..#.......#......
......#.......#...........#....
....#....#.#..##.#....#...#....
#.#.#..#..#.#.#.#...#....#....#
.#.#....#...#.#..#......#.....#
.#...........#.#....##.....#...
........#...#....#....##.....##
#..#..........#..#..#.....#....
#.#.###..........#.##....#...##
..#................#.##.##.....
..#...#.##...##...#.........#..
#....#......#......#.........#.
##...#...##.#.........#......#.
.......#.....#.................
...#...#.....##.........#.#..#.
..#......#...#.......#......#.#
#.......#...#.##.#..##..#......
.#.#............#...###..#.....
...#.......##.......#....#..#..
.....#..#.#....#.#.............
#....#...##.##....#....##......
........#......#.......#....#..
..#..#..##......##.#..#.#..##..
....##......#.##.##......#.....
........##.#...#.....#.......#.
..##.#....#..#......#.##.......
..##.####.#...#.#....#.........
.#........#.....#..#....#...#.#
###....##......#..#..#.##..#...
..........###.#..#..#....#.....
..#.........#....#.....#....#.#
.#...#.#.....##.#...#...#.#..#.
....##......##.##.#.....#..#...
....#.##...##.......#..##......
#..........#..#....#.......#.#.
..#.....#.................#....
..........#.#.#.....#.#....#..#
.......#..........#.##....#....
#..#.....#.......#........#....
#.....##..#.........##..#..#.#.
.##.#...#..........#....#......
....#..#.#......#.##..#..#.##..
...##.####....#.....#.#...##...
..#.#....#.#........#..........
#...#.#.##.##....##..#...#...#.
...#.#.......#..#...#..#..##..#
.....#....#........###.....#...
.......#..#.##....#.#.....#....
....##....#....#.......#.....#.
.........#........###...##.....
#.#..#...##.........#.#..#....#
...##...........#.........#...#
......#.#.#.........#..#.#.#...
........##.###....#..#.......#.
....#.#...#......#..#........##
.#....##....#...#.##.........#.
####.#..#...........##.#.#.....
...#....#..#.....#..##.####.#..
.##...#...........#.#.........#
#.#..#..#...#.#.#.........#..#.
#......###............#...#....
..#.......#....#...#...#..#...#
#.#.#...##..#...#...#.......##.
......#.#.......#..........#.#.
...............#...#..#...#.#..
.#.#...##.####..##.##....#..##.
#..####.......##.#........#...#
......###....##...#.#..#.##....
.##.....###..#...#.###.###.....
..#...#.....#...#..#..##..#....
...#...##.....##........#.#.##.
.#...#..#....#....#..###....#.#
..#.#.#.#.#..........#.#..#..##
.......###.....................
##.#......#.##.....#.........#.
......................#.#.....#
#..#........##.......#..##..#.#
#.#.#.....##.#.##.##.#....##...
.#...#.....#.........#.....#...
..#.........#.##.#.###.#......#
.........#..#.##...#.......###.
.....##........#......#........
...#.#...##...#........#.##....
.........##............#.####..
#....#...#...#..#....#..#.#.#.#
..#.........#......#.##........
....#.....#........#........#.#
.##.#..#.#..#..###......###....
#.###.....#.#.#.##........#..##
#.#..#...##.....#....#...#.#...
......#....#.....#...#.........
...#........##.......#.##..####
..#..#....#....#..#..#...#.##..
.##.....#............#...#.....
......#.......#.....#...#.#.#..
.........#.....#...##..........
.....#........##...........#...
#.#..##.#...#....#....#........
#.##..#.#.......#...#......#...
...........#.#..#..#.....##.#..
#....#.##.......#......#.##..#.
.....#........#.##.#...#.....#.
.....###..#.......##...........
.........#.#.#.....#.##.......#
.......#....#......#.#.....#...
##........#...#..#.#.........#.
##...........#.##...##......#..
..#.###.#.#.#...####..#....###.
.........#...#.....##....#.#.##
.###..###.#.#.....#.##.........
#..#...#.#.................##.#
##.........#.#....#.#...#.###..
#.#....#..............#.##.#...
...#..#....##.#..#.......#..##.
.#..#.###......##..........#..#
.##....#.#....#....#.#..#......
.......#.....#..#....#.##...#..
#.#.#.........###..#..#.....#..
...##..##...##....#..#......#..
..........#....#..........#....
#..##..#...#......#.....#.#....
#..##..#....#.#.#...#..........
......##..#.........#........#.
.##..#..#......###.....#..#....
.....#..#.##..........#.#..#...
"""


# In[21]:


import itertools as it


# In[22]:


def aoc_3_1(inp=inp, debug=False):
    lines = (it.cycle(l) for l in inp.splitlines())
    path, idx = [], 0
    for line in lines:
        if debug:
            print(f"Index: {idx}")
        [next(line) for _ in range(idx)]  # consume rows
        path.append(next(line))
        idx += 3
    return path.count("#")


# In[23]:


aoc_3_1()


# ## 3.2

# In[24]:


test_inp = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


# In[25]:


def aoc_3_2_helper(right=3, down=1, inp=inp, debug=False):
    lines = (it.cycle(l) for l in inp.splitlines())
    path, idx = [], 0
    while True:
        try:
            line = next(lines)
            [next(line) for _ in range(idx)]  # consume rows
            path.append(next(line))
            idx += right
            [next(lines) for _ in range(down - 1)]  # consume cols
        except StopIteration:
            break
    return path.count("#")


# In[26]:


def aoc_3_2(rights=(1, 3, 5, 7, 1), downs=(1, 1, 1, 1, 2), inp=inp, debug=False):
    assert len(rights) == len(downs), "not the same number of downs & rights!"
    product = 1
    for r, d in zip(rights, downs):
        trees = aoc_3_2_helper(right=r, down=d, inp=inp)
        if debug:
            print(f"Right {r}, down {d}: {trees:3}.")
        product *= trees
    return product


# In[27]:


aoc_3_2(inp=test_inp, debug=True)


# In[28]:


aoc_3_2(inp=inp, debug=True)


# # 4

# ## 4.1

# In[29]:


test_inp = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


# In[30]:


inp = """byr:1971
iyr:2017 hgt:160cm
eyr:2020 ecl:hzl
pid:157096267

hgt:183cm
pid:368895060
ecl:oth eyr:2020
iyr:2013
byr:1966

ecl:lzr cid:279 pid:192cm
hcl:1f7352 iyr:2014 hgt:70cm eyr:1983
byr:2004

hcl:#602927 iyr:2018 byr:1938 ecl:blu
eyr:2024 hgt:172cm
pid:839621424

ecl:#12f268
hcl:#6b5442
iyr:2012 byr:2011
eyr:1933 pid:189cm hgt:155in

byr:1954
ecl:gry pid:664227667 eyr:2028
hgt:151cm
iyr:2019

ecl:gry
byr:1931 iyr:2017
pid:459927933 eyr:2028
hgt:67in hcl:#fffffd

cid:322 hgt:163cm
byr:1969 hcl:#a97842 pid:472877556
iyr:2019
ecl:amb eyr:2030

hcl:#733820 ecl:brn byr:2000 eyr:2022 iyr:2014 cid:320 pid:751634349
hgt:180cm

ecl:blu eyr:2028
hcl:#866857 byr:2029 hgt:191cm iyr:2010
pid:170cm cid:123

pid:258660154 byr:1921 hgt:161cm
eyr:2030
cid:217 iyr:2012
hcl:#4dd6d4 ecl:grn

hgt:170cm byr:1978 eyr:2022 pid:399347273
iyr:2010 cid:109 ecl:blu hcl:#602927

pid:172106685
hgt:183cm
ecl:gry iyr:2020 eyr:2025 hcl:#18171d byr:1980 cid:289

cid:77 ecl:#254ad9
byr:2017 pid:169290741 iyr:2003 hgt:85 hcl:z

hgt:155cm byr:1987 ecl:oth hcl:#fffffd
iyr:2010

ecl:brn iyr:2014 cid:74
hcl:#623a2f
hgt:187cm byr:1955 pid:008305281 eyr:2025

pid:428624233 ecl:grn
eyr:2027 hgt:167cm hcl:#623a2f byr:1960 iyr:2016

eyr:2027 pid:358876826 hgt:171cm ecl:oth byr:1957 iyr:2018
hcl:#ceb3a1
cid:314

ecl:grn eyr:2030
hgt:73in iyr:2011 hcl:#602927

hgt:76in byr:2029
pid:2703176 iyr:2020
eyr:2037 ecl:#95d926
hcl:9574d2

eyr:2020 hgt:164cm
byr:1949 hcl:#fffffd pid:591281293 iyr:2014 cid:136

cid:268 hgt:73in hcl:#6b5442 eyr:2025 ecl:brn byr:1988 pid:899417027 iyr:2015

iyr:2020 hcl:#b6652a hgt:177cm
eyr:2028 ecl:hzl
byr:1995 pid:594197202

hcl:#a97842 hgt:179cm byr:1930
ecl:brn pid:010268954 eyr:2020 iyr:2010

iyr:2022 pid:93390086
cid:321 eyr:2034 hcl:#a97842 hgt:168in byr:2006 ecl:#a8f84c

eyr:2028 ecl:blu byr:1935
hcl:#6b5442 pid:187679418
hgt:174cm iyr:2016

iyr:2019 hgt:164cm pid:704379775
ecl:oth hcl:#888785 byr:1930
eyr:2025

hcl:#6b5442 cid:168
hgt:171cm eyr:1944 iyr:2018 pid:675364934
byr:1962
ecl:hzl

hcl:z
eyr:2039
ecl:zzz pid:26281402 cid:144 iyr:1928
hgt:166cm

ecl:hzl hcl:#7d3b0c
eyr:2022 pid:011589584
hgt:64in byr:1945 iyr:2014

byr:1950 hcl:#18171d pid:685748669 eyr:2028 iyr:2010 hgt:176cm ecl:grn

byr:1989
hgt:163cm hcl:#18171d ecl:grn iyr:2020 pid:721397788 cid:308 eyr:2020

pid:443496560 iyr:1999
eyr:2027 hcl:z
hgt:69in ecl:zzz byr:2019
cid:108

pid:#c9d804 eyr:2011
ecl:#574df9 iyr:2027 hcl:z byr:2018
hgt:64

hgt:69cm
iyr:1926 hcl:fdcce6
ecl:#28b358
eyr:2026
byr:1994
pid:76404593

eyr:2020
ecl:hzl pid:978839539 hcl:#efcc98
byr:1935 cid:121
hgt:165cm

ecl:amb
byr:1951 hgt:186cm pid:812513486 iyr:2012 eyr:2029 hcl:#fffffd

hcl:fcdd61 hgt:168in ecl:grt pid:8474140699 byr:1924 iyr:2027 eyr:2023

ecl:oth hcl:#866857
byr:1965 pid:533941934 hgt:166cm iyr:2019 eyr:2040

eyr:2032 pid:0795438812 iyr:2009 hcl:z
byr:2028 hgt:131 ecl:gmt

cid:102 byr:1923 eyr:2025
pid:222102208 iyr:2019 hcl:#341e13
hgt:167cm
ecl:amb

hgt:180cm byr:1956 iyr:2014 eyr:2022
ecl:oth cid:175 hcl:#888785

cid:216 eyr:2022
ecl:brn pid:002875069 iyr:2019 hcl:#cfa07d byr:1991 hgt:164cm

iyr:2014 byr:1933 pid:537809907
hgt:185cm eyr:2029 hcl:#341e13 ecl:blu

cid:286 hgt:166cm byr:1977 iyr:2012 pid:541909675 ecl:oth eyr:2020
hcl:#59eb12

hcl:#18171d cid:329 byr:1921 eyr:2027 iyr:2019
pid:440820443 hgt:75in ecl:blu

hcl:#733820 hgt:177cm
pid:085529831 eyr:2029 iyr:2010 ecl:amb byr:1972

pid:704125918 hcl:#b6652a byr:1981
ecl:#698ae8 cid:141 iyr:2018 eyr:2026 hgt:66in

iyr:2020 eyr:2022
hgt:191cm hcl:#7d3b0c
ecl:blu byr:1943 pid:969407635

pid:10899196
hgt:161cm
ecl:lzr iyr:2023 hcl:#ceb3a1 byr:1986 eyr:2012

hcl:#7d3b0c ecl:utc eyr:2020
byr:2028 pid:#f8c441 iyr:2030
hgt:164cm

byr:2003 hcl:z iyr:2012 hgt:187in
ecl:gry eyr:2030 pid:150cm

pid:427618420 hgt:155cm iyr:2012
ecl:brn
byr:1948 eyr:2029 hcl:#6b5442

ecl:oth hgt:81
byr:2025 cid:66 pid:174cm hcl:z
eyr:2021

byr:2027 ecl:lzr hcl:#888785 eyr:1923 hgt:110 cid:54 iyr:1939

hcl:#341e13 byr:1961 eyr:2022 hgt:163cm cid:137 ecl:amb
iyr:2019

hcl:#866857
iyr:2020
byr:2005
hgt:139 ecl:amb cid:181
eyr:2016
pid:181cm

byr:2030
iyr:2014
hcl:#733820 cid:74 eyr:2021 hgt:179cm
pid:7938817872
ecl:amb

hcl:91a6dd
iyr:2019 byr:2024
hgt:72cm
ecl:gmt eyr:2023
pid:8440093771

ecl:grn byr:1963 cid:60 iyr:2030
hgt:74 eyr:2022
pid:193189388
hcl:#b6652a

pid:403849590 byr:2012
eyr:1951 cid:90 iyr:2023
hgt:69cm hcl:z ecl:gmt

iyr:2010 hcl:#341e13
pid:011326174 hgt:185cm byr:1976 cid:207 eyr:2027 ecl:amb

hgt:64in
pid:499837104 hcl:#3be285
byr:1944
eyr:2024 iyr:2017
ecl:gry

eyr:2032 pid:#850d4e hcl:deddda ecl:brn hgt:172 byr:2004
cid:244 iyr:2022

hcl:a3346d ecl:amb
pid:#505713 hgt:74cm eyr:2010 iyr:2020

byr:1987
ecl:oth iyr:2012 eyr:2023
pid:131199420 cid:112 hcl:#a97842

cid:256 hcl:#a97842 byr:2000 iyr:2018 ecl:oth
eyr:2022 pid:637777693 hgt:160cm

hgt:152cm
cid:164 hcl:#866857 ecl:grn eyr:2025
pid:495224989 iyr:2020 byr:1949

iyr:2010
cid:288 byr:1986 ecl:blu
pid:304077824
eyr:2020

hgt:182cm
ecl:blu
hcl:#18171d pid:047931925 byr:1964
iyr:2012 eyr:2030 cid:167

byr:1958
hcl:#866857 iyr:2019 hgt:165cm pid:553631683
cid:109 ecl:gry
eyr:2023

cid:156
iyr:2014 pid:811368482 eyr:2026 hcl:#b6652a byr:1994
hgt:184cm ecl:brn

hcl:#733820
hgt:183cm ecl:grn
pid:265625165 byr:1943 cid:344
iyr:2011

iyr:2017 hcl:#c0946f pid:716422629 cid:104 byr:1974
hgt:160cm eyr:2021 ecl:brn

byr:2002 hgt:180cm hcl:#602927
eyr:2025 ecl:grn iyr:2011 pid:887584172

hcl:#888785 ecl:brn eyr:2026
pid:14483306 byr:1947
hgt:177cm iyr:2015

hcl:#b6652a
ecl:#64783e eyr:2020 hgt:163 pid:651615946
iyr:2012 byr:1999

iyr:2014 ecl:gry hgt:188cm eyr:2028 pid:503058612 hcl:#a31066

hgt:178cm hcl:z
ecl:amb
pid:17656631
eyr:2031 byr:2023

hgt:166cm pid:783568747 hcl:#341e13
byr:1955 ecl:grn eyr:2023

iyr:2016 hgt:161cm byr:1989
eyr:2023
ecl:amb pid:133770783
hcl:#fffffd

cid:75 byr:1986 eyr:2020 pid:099478576 ecl:blu
hcl:#733820
iyr:2011 hgt:158cm

pid:911200183 hcl:#602927 eyr:2029 iyr:2018 ecl:brn hgt:181cm
byr:1937

iyr:1928 byr:2020 hcl:579202
hgt:60 ecl:utc eyr:1963 pid:157cm
cid:253

eyr:2028 iyr:1949
pid:284455762 hcl:#a97842 ecl:oth byr:1947 hgt:163cm

hcl:#18171d eyr:2025 cid:222
byr:1924 ecl:oth
pid:898594506 hgt:182cm
iyr:2017

byr:1935 iyr:2027
hgt:160in pid:#c090c3
hcl:#623a2f cid:162 eyr:1942 ecl:amb

iyr:2014 hgt:160cm eyr:2028 hcl:#623a2f byr:2010
pid:684765216 ecl:blu

byr:1958
hgt:154cm hcl:#a97842
ecl:oth iyr:2015 eyr:2020 cid:334

pid:636691339 iyr:2018
byr:1930
hcl:#b6652a cid:86
hgt:184cm ecl:oth
eyr:2029

iyr:2025
hgt:76cm ecl:#043004 hcl:z
byr:2009 eyr:1999

eyr:2020 pid:56419390 iyr:2015 hcl:#ceb3a1 ecl:utc
hgt:98

iyr:2014 byr:1927 hcl:#fffffd ecl:amb eyr:2022
hgt:188cm pid:602778565

hcl:#cfa07d eyr:2029 byr:1937 pid:7912057436
ecl:hzl
cid:192 hgt:68in iyr:2012

hgt:155cm
iyr:2015 byr:1954 pid:559203670
ecl:blu hcl:#fffffd eyr:2025

hcl:#341e13 byr:1998 iyr:2019
cid:312
ecl:oth
pid:230874778 hgt:161cm

iyr:2011 ecl:amb
eyr:2026
hgt:163cm byr:1932 hcl:#733820 pid:850176278

eyr:2030
hgt:170cm
iyr:2017 byr:1972
pid:014731313
hcl:#341e13 ecl:brn

pid:133005637
hgt:167cm
cid:317
eyr:2025 hcl:#341e13 iyr:2012 ecl:gry byr:1950

iyr:2029 pid:745014772 hgt:68in
eyr:2034 ecl:hzl
hcl:ec07ce

hgt:165cm
ecl:gry
hcl:#a97842 byr:1921 cid:263 pid:609363367

pid:192cm hcl:18f308
ecl:oth
eyr:2037 cid:239 iyr:2026 byr:2010

hcl:d0e525 eyr:2037 iyr:2019
cid:197
pid:469740743
hgt:186in ecl:brn byr:1977

ecl:hzl cid:254 hgt:165cm
eyr:2024 byr:1996
iyr:2021 pid:797277746 hcl:e286e8

hcl:#b6652a cid:142 ecl:oth hgt:190cm byr:1962 pid:997137384 iyr:2020
eyr:2029

ecl:brn byr:1962 hcl:#866857 iyr:2020 hgt:152cm pid:701556397 cid:121 eyr:2029

eyr:2024 cid:186 hcl:z
byr:1962 hgt:155cm pid:448098321 iyr:2017 ecl:grn

iyr:2016
hgt:168cm byr:1999
cid:286
hcl:#18171d pid:223995430 eyr:2022 ecl:blu

pid:227780276 ecl:blu iyr:2017 byr:1985 hcl:#6b5442 hgt:183cm eyr:2028

hgt:190cm
ecl:oth eyr:2030 cid:223 hcl:#888785 iyr:2010
pid:115829664 byr:1967

eyr:1992 pid:0688674980 hcl:z
byr:2028
hgt:186in ecl:#849f7b
iyr:2029
cid:64

eyr:2025
iyr:2013 byr:1958 ecl:grn
hcl:#ceb3a1
hgt:153cm pid:815357118

pid:038013822 hgt:180cm iyr:2013
hcl:#623a2f
ecl:grn eyr:2029 byr:1949

byr:1923
cid:299 hgt:184cm iyr:2020
hcl:#fffffd eyr:2027
ecl:hzl

byr:1930
iyr:2012
ecl:grn hcl:#87f2c8 pid:787371085

iyr:2019
eyr:2028 pid:107626362 hgt:183cm
ecl:grt hcl:#623a2f byr:1985

byr:2011
hgt:68in iyr:2002 ecl:#5dfa18 hcl:#341e13 pid:205853974

iyr:2014
pid:179cm
hcl:13b9e3 eyr:2022 ecl:#b1759b hgt:184in
byr:1954

hgt:183cm hcl:#efcc98
pid:428260080 cid:231 eyr:2025 ecl:grn
iyr:2010
byr:1957

iyr:2016
ecl:gry
pid:192cm eyr:2026
byr:1956
hgt:174cm hcl:#623a2f

eyr:2021 ecl:blu cid:230
byr:1923
pid:438732879 hgt:167cm
hcl:#602927

byr:1948 ecl:xry
pid:154cm hgt:179cm eyr:2029 iyr:2017
hcl:#dd59ab

hcl:#ceb3a1
iyr:2014 byr:1981 hgt:167cm ecl:grn
eyr:2021
pid:926925947

iyr:1985
pid:652196636 hcl:#18171d ecl:#ff3e10 hgt:162cm byr:2012 eyr:2023 cid:171

eyr:2029
hgt:166cm
pid:499909488 byr:1929 hcl:#866857 ecl:brn iyr:2013

pid:440245122
byr:1992 hgt:179cm iyr:2010 cid:181 ecl:brn hcl:#888785 eyr:2020

eyr:2029 hcl:#888785 pid:274994154 ecl:hzl
iyr:2014 byr:1995

pid:3195072620
hcl:z ecl:hzl cid:130 iyr:2030 eyr:2034 hgt:157

hcl:#1b0a51
pid:129985083 eyr:2029
hgt:192cm cid:236 byr:1996 ecl:blu iyr:2016

ecl:lzr pid:899902347 iyr:1982
hcl:#cfa07d eyr:2028 byr:1927 hgt:155in

cid:187 eyr:2029 hcl:#efcc98 byr:1986 pid:760318090
hgt:169cm iyr:2018 ecl:amb

hcl:#fffffd eyr:2021 pid:532530085 iyr:2019 byr:1995 hgt:169cm

iyr:1980
hcl:z eyr:2019
hgt:72cm pid:6532875244 ecl:#2f2221 byr:2006

hgt:174cm byr:1920
ecl:gry pid:#14fae7 eyr:2026 hcl:#1814d1
iyr:2013

hcl:#ceb3a1 ecl:grn
iyr:2018
byr:1978
hgt:183cm pid:566862236
eyr:2028

iyr:2020 ecl:amb
pid:618246345 byr:1940
hgt:60cm eyr:2027 cid:242 hcl:#b6652a

ecl:grn
hcl:#18171d byr:1957 pid:325895714 iyr:2018
eyr:2023 hgt:162cm

ecl:#a3ed7b
byr:2024
hcl:z eyr:2022 iyr:2016 cid:350 hgt:119 pid:185cm

iyr:2010
byr:2004 eyr:2032 cid:326 hcl:6019c5
ecl:gmt hgt:137

pid:477848102 eyr:2025 hgt:178cm hcl:#e31a3d ecl:brn
byr:1943

pid:#65fca1 eyr:2026 hgt:192cm cid:293 ecl:blu byr:2026 iyr:2024 hcl:#a97842

eyr:2025 cid:181 hgt:186cm byr:1968
ecl:brn pid:318405093 hcl:#341e13 iyr:2015

hcl:#c12f4b eyr:2025 cid:311 pid:652667870
ecl:oth
hgt:166cm
byr:1981 iyr:2016

ecl:hzl
byr:2025 iyr:2014
hcl:138d5c eyr:2037 hgt:160in cid:206
pid:#d9119b

pid:51419740 cid:141
iyr:2012
hgt:90 ecl:#9438f4 hcl:#7d3b0c byr:2021 eyr:2020

pid:#0bc613
hcl:z byr:2017
hgt:91 cid:284 eyr:1966 iyr:2008
ecl:#974ceb

cid:344 iyr:1953 eyr:2020 ecl:hzl byr:2019 hcl:z pid:2969979

ecl:gry
byr:1925 cid:113
hcl:#a97842 pid:744660539 hgt:153cm iyr:2020

hgt:177 pid:856186682 eyr:1968 ecl:blu
cid:167 byr:1986 hcl:#866857 iyr:2015

byr:1937 eyr:2021 iyr:2017
cid:91 hgt:183cm hcl:#a97842 ecl:blu pid:149192621

hgt:154cm hcl:#602927 ecl:oth
byr:1939 iyr:2018 pid:670669747 eyr:2029 cid:301

eyr:2025 pid:249412970 ecl:oth
iyr:2016
byr:1921 hcl:#a97842 hgt:176cm

byr:1969
iyr:2019 hcl:9de0cb
pid:644476999 hgt:75in
ecl:oth eyr:2022

hgt:164cm iyr:2016
byr:1988 ecl:gry
eyr:2030
hcl:#efcc98 pid:393258887

hgt:183cm pid:6930456 eyr:2023 cid:210 ecl:#766482 byr:2023 iyr:2017 hcl:z

iyr:2011 hgt:165cm eyr:2020 byr:1966
hcl:#efcc98 pid:691169980 ecl:blu

iyr:2011 hcl:#602927 eyr:2029
byr:1966
ecl:oth hgt:165cm pid:945383793

pid:567096741 iyr:2025
ecl:gry eyr:1944 hgt:187in byr:2026 hcl:8ac39a

byr:2025
eyr:2025 iyr:2015
hgt:191 pid:1659927272 ecl:grn

iyr:2027 hgt:63in byr:1963 pid:874200881
ecl:oth hcl:#c0946f eyr:2029

hcl:#b37a48
byr:1957 ecl:hzl
eyr:2030
iyr:2013

pid:#38e0fd eyr:2019 cid:103
hgt:153in
ecl:#956d7c
iyr:2029 byr:2029 hcl:z

eyr:2021 pid:956654136
hcl:#854d9d hgt:186cm byr:1960 iyr:2015

eyr:2020
byr:1995
hcl:#b6652a ecl:amb pid:746523744 iyr:2015
hgt:178cm

eyr:2020 hgt:173cm cid:322 byr:1956 iyr:2020 ecl:blu
pid:833595649

ecl:gry iyr:2017 eyr:2020 pid:537816651 hgt:183cm cid:160 byr:1996 hcl:#733820

iyr:1920
byr:2013
hcl:z eyr:1932 pid:169cm

eyr:2030 cid:258 iyr:2020 ecl:grn byr:1947 pid:571610070
hgt:162cm hcl:#888785

byr:2025 hgt:155cm iyr:2030 ecl:amb eyr:2002

iyr:2020 ecl:hzl
pid:090561426 hcl:#a97842
byr:1923

ecl:hzl
iyr:2019
hcl:#c0946f eyr:2025
byr:1999 hgt:178cm pid:026042669

hgt:74in
eyr:2027 iyr:2015 ecl:gry
byr:2005 pid:#28b09d

eyr:1953 byr:2014 ecl:lzr cid:202 hcl:1af88d
iyr:2028

cid:99
pid:706477697 iyr:2018 hgt:171cm eyr:2027
ecl:oth
byr:1978 hcl:#930aef

iyr:2017
byr:1935
eyr:2029
ecl:amb pid:321873254 hgt:179cm hcl:#1b9aea cid:160

iyr:2013 ecl:hzl eyr:2023 cid:233 byr:1996 pid:605962483 hgt:175cm hcl:#ceb3a1

pid:754905579
ecl:brn eyr:2021 hcl:#ceb3a1
byr:1943 hgt:59in

cid:110 byr:1935 eyr:2021 hgt:172cm iyr:2020
pid:643443673 hcl:#888785 ecl:brn

ecl:gmt hcl:#cfa07d
hgt:148 iyr:2024 pid:635827422
eyr:1935
byr:1964

iyr:2012 byr:2016 hcl:z
hgt:178cm pid:213073693 eyr:2005

ecl:#b3cc58 byr:2027 pid:172cm hcl:#888785 hgt:177cm eyr:1988
iyr:2027

eyr:2029
byr:1923
hcl:#d9855b cid:134 pid:068598146 hgt:152cm ecl:blu

cid:309
iyr:2010 ecl:oth hgt:188cm hcl:#18171d eyr:2028 pid:174227992 byr:1931

iyr:2010 hgt:72in cid:266 ecl:brn pid:0090854908
hcl:#623a2f eyr:2032
byr:1967

pid:192554211 eyr:2020 hgt:192cm ecl:gry cid:158 iyr:2015 byr:1940
hcl:#efcc98

cid:248 hgt:75in eyr:2025 byr:1957 hcl:#c0946f
iyr:2019
ecl:brn

pid:96533216 hcl:z ecl:blu eyr:2027 hgt:193cm cid:224
byr:1928 iyr:2014

iyr:2010
eyr:2022 cid:276 hcl:#a97842 byr:1968 ecl:gry pid:808830560 hgt:188cm

hgt:158in
pid:097590485 iyr:2030 eyr:1940 hcl:z cid:274
ecl:#2ea9ec
byr:2024

pid:616947922 byr:1982 iyr:2014 hgt:186cm ecl:oth hcl:#888785

byr:1941 pid:039744699 hcl:#efcc98 hgt:190cm iyr:2011
eyr:2020 ecl:blu

byr:1971
ecl:hzl hgt:65in
pid:076133019 iyr:2019 eyr:2030

ecl:blu iyr:2011 byr:1928 hcl:#c0946f hgt:172cm eyr:2026 pid:171544458

byr:1929 pid:145819079 ecl:hzl
hgt:192cm iyr:2015 eyr:2020 hcl:#b6652a

byr:1981 ecl:amb pid:123467924
eyr:2024 hcl:#18171d
hgt:184cm iyr:2017

byr:1957
ecl:oth pid:881258191 hgt:65in iyr:2010
hcl:#a97842

ecl:amb eyr:2020 hgt:152cm
iyr:2021 pid:9448811025 hcl:#c0946f cid:204 byr:2030

eyr:2022 pid:208725350
byr:1944 ecl:blu hcl:#18171d cid:164
hgt:170cm iyr:2014

hcl:#18171d eyr:1952 iyr:1939 pid:788651896 hgt:157in byr:2007

byr:1944 cid:87 pid:463367304
iyr:2020 hgt:188cm ecl:gry
eyr:2027 hcl:#cfa07d

ecl:hzl
iyr:2018 hgt:164cm byr:1972 cid:272 pid:990204374
hcl:#6b5442

hgt:155cm pid:791416860 iyr:2015
cid:278 hcl:#18171d byr:1994 ecl:brn
eyr:2023

iyr:2017 cid:245 eyr:2026 byr:1932 ecl:blu
hgt:159cm pid:904760812 hcl:#18171d

ecl:blu hcl:#6b5442
iyr:2015 eyr:2023 pid:535891497 hgt:175cm cid:168 byr:1920

byr:2000 hcl:#6b5442 hgt:156cm
pid:765444727 iyr:2012
ecl:brn
eyr:2028

eyr:2005 pid:9092484649
byr:2028
ecl:#5fc7fc hgt:81
iyr:1988 hcl:8280e1

cid:275
byr:1928 iyr:2010 hcl:#888785 pid:596954301 ecl:brn eyr:2020 hgt:166cm

cid:163
byr:1984 eyr:2027 iyr:2020
ecl:gry hgt:166cm pid:650001846
hcl:#602927

iyr:1925 eyr:2030
byr:1985 hcl:#cfa07d ecl:#f16a95 hgt:150cm pid:67853501

ecl:gry
eyr:1949 cid:218 hgt:73cm byr:2004 pid:055108092
iyr:1961

eyr:2024 iyr:2016 pid:133523002
hgt:62in hcl:#d99c14
byr:1996 ecl:hzl

eyr:2026 iyr:2019 hgt:189cm ecl:brn hcl:#623a2f
byr:1979 pid:172111665

iyr:2017
eyr:1937 ecl:#bfd0ee
byr:1964 hcl:#733820
hgt:169cm pid:33181449

eyr:2024 hcl:#6b5442
iyr:2014
hgt:68in pid:577055593 ecl:grn byr:1996

hcl:z cid:150 eyr:2039 byr:2015 pid:2453663020 ecl:brn
hgt:154cm

hcl:#efcc98 eyr:2022
ecl:grn hgt:167cm byr:1978 iyr:2010 pid:180446111

ecl:gry
iyr:2020 hgt:152cm pid:#cce9cf eyr:2028
byr:1942
hcl:z

hcl:#341e13 ecl:brn iyr:2019
pid:589837530 cid:157 byr:1925 hgt:183cm eyr:2020

byr:2009
pid:179cm hgt:164cm
iyr:1927 hcl:#cfa07d eyr:2034

ecl:oth iyr:2012
eyr:2028 hcl:#866857 pid:716964854
byr:1940 cid:113 hgt:193cm

byr:1985 iyr:2011 hcl:#866857 pid:454558712 eyr:2025 cid:301
hgt:62in ecl:blu

hcl:#733820 eyr:2025 ecl:amb
pid:855788635 iyr:2016
byr:1965
cid:140 hgt:183cm

hcl:#efcc98 cid:326 eyr:1961
pid:001357810 iyr:1947 ecl:#8abfc8 hgt:75 byr:2012

hgt:60cm pid:#e28da4 byr:2014 iyr:2019 eyr:2040 ecl:utc

hcl:#733820 eyr:2022 pid:708208638 hgt:162cm cid:326 iyr:2018 ecl:oth byr:1997

iyr:1967 byr:2013 pid:8595504787 hgt:73cm ecl:dne

pid:808787977 hcl:#18171d
cid:205 hgt:181cm
byr:1986
ecl:gry iyr:2013

ecl:dne iyr:2009
byr:2027
hgt:188in hcl:#c0946f
pid:585147305 eyr:2024

hcl:#733820 iyr:2019
eyr:2020
hgt:190cm
pid:042907748 ecl:grn byr:1920

ecl:#603ad1
eyr:2026
hcl:33f9f8
pid:862887360 hgt:156in byr:1993
iyr:2013

ecl:oth eyr:2030 byr:1960
hcl:#a97842 cid:285
hgt:60in pid:655974048 iyr:2016

iyr:2030
hgt:143
pid:65806846 byr:1948 hcl:#72a0d3 eyr:1934 ecl:#7cd402

hcl:z pid:#0f7c0a iyr:2012 hgt:161cm
byr:2022 eyr:1937

hcl:#fffffd ecl:hzl
hgt:191cm byr:1935 iyr:2015 cid:240 eyr:2030 pid:778049989

ecl:amb iyr:2011 hcl:#e196f6 pid:231470794 eyr:2026 hgt:179in byr:1979

ecl:oth hcl:#6b5442 pid:181cm hgt:72cm
eyr:2040 iyr:2010

iyr:2016 eyr:2026 pid:113617276
cid:117 hgt:176cm ecl:grn
hcl:#c5b999

iyr:2016 byr:1941
pid:846760253 hgt:60cm
hcl:#7d3b0c ecl:zzz
eyr:1972

eyr:2023 hcl:#623a2f
cid:103 pid:476193829 hgt:181cm ecl:oth byr:1997
iyr:2014

ecl:#b64a07 hcl:7bb40c byr:2028 eyr:2039 pid:#e2ba33 hgt:189 iyr:1940

pid:#3ecfd8 hcl:#7d3b0c iyr:2014 ecl:#30a5e7 hgt:73cm byr:1954

ecl:dne
byr:2011 pid:512088455
hcl:#18171d eyr:2023
iyr:2024

byr:1996 eyr:2026 pid:268556486 ecl:brn
hgt:150cm
iyr:2013 hcl:#7d3b0c

iyr:2014
ecl:grn pid:222910621 hcl:#602927
eyr:2030 hgt:155cm

pid:530689228 byr:1938
iyr:2015
hgt:185cm ecl:hzl eyr:2022 hcl:#866857

hcl:#b6652a byr:2028 iyr:2018 cid:150 ecl:lzr pid:706073193 hgt:169cm

hgt:171cm ecl:gry hcl:#6b5442 byr:1953
iyr:2011 pid:622763802 eyr:2026

eyr:2032 hgt:137
pid:5033763648
byr:1925 ecl:hzl hcl:#623a2f iyr:2024

byr:1930 pid:6999766453 ecl:#3e3e07
hcl:#602927 iyr:2010 eyr:2039
hgt:160cm

hgt:122 ecl:amb pid:105302121 iyr:2017
hcl:#733820
eyr:2027 byr:1955

hcl:#95f96b
hgt:193cm iyr:2020 pid:719337690
byr:1971
ecl:brn eyr:2024
"""


# In[31]:


KEYS = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"))


# In[32]:


OPT_KEYS = set(("cid",))


# In[33]:


REQ_KEYS = KEYS.difference(OPT_KEYS)


# In[34]:


KEYS, OPT_KEYS, REQ_KEYS


# In[35]:


def split_inp(inp=inp):
    yield from inp.split("\n\n")


# In[36]:


def check_passport(pp):
    return all([f"{k}:" in pp for k in REQ_KEYS])


# In[37]:


def aoc_4_1(inp=inp):
    return sum(check_passport(pp) for pp in split_inp(inp))


# In[38]:


aoc_4_1()


# ## 4.2

# In[39]:


from functools import partial


# In[40]:


import re


# In[41]:


REQ_KEYS = ("byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid")


# In[42]:


ECLS = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


# In[43]:


def year_check(y, miny, maxy, digits=4):
    try:
        return len(y) == digits and miny <= int(y) <= maxy
    except:
        return False


# In[44]:


def check_height(hgt):
    if len(hgt) > 5 or len(hgt) < 4:
        return False
    val, unit = hgt[:-2], hgt[-2:]
    if unit not in ("cm", "in"):
        return False
    try:
        val = int(val)
    except:
        return False
    if unit == "cm":
        return 150 <= val <= 193
    else:
        return 59 <= val <= 76


# In[45]:


RULES = {
    "byr": partial(year_check, miny=1920, maxy=2002),
    "iyr": partial(year_check, miny=2010, maxy=2020),
    "eyr": partial(year_check, miny=2020, maxy=2030),
    "hgt": check_height,
    "hcl": lambda hcl: re.fullmatch(r"#[\da-f]{6}", hcl) is not None,
    "ecl": lambda ecl: ecl in ECLS,
    "pid": lambda pid: re.fullmatch(r"\d{9}", pid) is not None,
}


# In[46]:


def parse_passport(pp):
    pp += " "  # append whitespace so regex is easy
    pp_dict = {key: re.findall(fr"{key}:(.*?)\s", pp)[0]
               for key in REQ_KEYS}
    return pp_dict


# In[47]:


def check_passport_2(pp):
    if check_passport(pp) is False:
        return False
    fields = parse_passport(pp)
    assert set(RULES.keys()) == set(fields.keys()), "fields and rules don't match!"
    return all(RULES[field](value) for field, value in fields.items())


# In[48]:


def aoc_4_2(inp=inp):
    return sum(check_passport_2(pp) for pp in split_inp(inp))


# In[49]:


aoc_4_2()


# # 5

# # 5.1

# ```
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# ```

# In[50]:


test_inp = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


# In[51]:


inp = """BFBFFFBLRL
FFBFFBFRLR
BBBFFBBRLL
FBFFBBFLRL
BFBBFFFLRR
BFBBFBFRRL
BFFBBBFRRL
BFBBFFBRRL
FFFBFBBLRR
FBBBBBBLRL
FFBBFFBRLR
FFBBFBBRLL
FBFFBFFLRL
FBFBFFBRRR
FBFBBFBRLR
FFBBFBFLRR
BFBBBBFLRL
BFFFFFFLRR
BBFFFBBRLR
BFBFBFBLRR
FFBBFFBRRR
BBFBBFBRLR
FBBFFBFRLR
FBFFFBFLRL
BFFFBFBLRR
BFFFFBFRLR
FBBFFFFRRL
BFFBBBBRRR
FBFBFFFLLR
BBBFFBFRRR
FBFBFBBLRL
FBFBBBFRLL
FBBFBFFLRL
BBBFFBFRLR
FFBBBBFLLR
BFFFBBFRLR
FFBBBFFRRR
BFFFBFFLRL
BFFBBFFRRL
FBFBFFFRLR
BBFBFBBRRL
FFBBBBFRRR
FBBBBFFRRL
FBFFFBFRRR
FBFFFBFLLR
FFBBFBBLLR
BFBFBFFLRR
FBBFBFBRRR
BBFBFFFRRL
BFFBFFBLLR
FBFBFBFRLR
BFFBBBFRRR
FBBFFFBLRL
BBFBFFBRLR
BFBBFBBRRR
FBFBFBBLRR
BBFFFBFRLR
FFBFBBFRLL
BBFFBFBRLR
FBFBFFBRRL
BFFBFBFLLR
BBBFFFBLRR
BFBBBFBRLR
BBFFFFFRRR
BFFBFFFRLL
FBBFBFBLRL
BBFFBBFLRR
BFBBFFBLRL
FFFBBFBLLR
FFBFBFBLLR
FFFBBFFRLR
BFFFFBFLLL
FFBBBBBLLR
BFFFBBFRLL
FBFBBFBRLL
BFFBBFBLRL
FBBBBFFRLL
BFBBBFFLRR
BBFBBFFRLL
FFFBBFFRRR
BBFBBFBRRR
BBFFFBFRLL
BFFBFBFLRL
FBBFBFFLRR
BBFFBBBRLR
FFFBBFBRLL
BFFBFFFLLR
FFBBBBFRLL
FFBBFFBLLR
BFFFFBBLLR
BBFBBBBRRL
BBFFBFBLRL
FFBBFBBLLL
BBFFBFFRLR
BFFFBFBRLR
BFFBBBBLLL
BFFBFFFRRR
BBFFFBBRLL
FBBBFFBLRR
FFBFFBBRLL
BFFFFFBLRL
FBFBFBFRRR
BBFFBBBLLL
BFBFBFBRRR
FBBBFFBLRL
BBBFFBFLRR
BBFFBBBRRR
FBFFFFBRLL
FBFBFBFRRL
BFBBBFFRLR
FBFFFFBRRL
BBBFBFFLLL
FFBFBFBRLL
BFBBFFFLLL
BBBFFFFLLL
BBFFFBFRRR
FFBBBBFLRL
FBFFBBFLRR
BBFBFBBRLL
BFBFBBBLRL
FFBFBBFLLR
BFFFFFBRRL
BFFBFBBRLR
BFBFFFFRLL
BFBBFFFRRL
FBBFFFFRLL
BBFBFBBLLR
FFBBBFBLRL
FBBFFFBRRL
FFBBFBBLRL
BFBFFBBLLR
BBFBFFFLLR
BBBFFFFRLR
BFBBFBFRLR
BFBBFFBRRR
BBFFBBFRRL
BBFBFFBRRL
BFFBFBFRLR
BBFBFBBRLR
FFBFBFFRRL
BFBBFBFLLL
BBFBFFFLRL
BFBBBBFLLR
BFFFFBBRRL
BBFFFFBRRL
BFFBBFBRRR
BFFBBFBLLR
BBFBBBBRLL
FBBFBFFRRR
FBFFFFBLLR
BFBFFBFRLL
FFBFFBBRRR
BFFFBFBRRR
BBBFFFBLLL
BBFFFBBRRR
FBBFFBBLLL
FBFFBBBRLL
BBFBFFFRLR
FBFFFBBRLR
FFBBBFBLLL
BFFFFBFLRR
FFFBBFBRLR
BBFFFFBLRR
FBFFBFBRRR
FBBFBBFLRL
BFBBFFBLLR
BBBFFBFLLR
BFBFFBBRRL
BFFBFBFRRL
BFFFFBFRRR
BBBFFBBRRL
FBBFFFBRRR
BFBFBFFLLL
FFBBFBFLLR
FFBFFBFLRL
BFBFFBFRRR
FBFBBBFLRL
FFFBFBBRLL
BBFBFFBRRR
FBBFBFFRRL
BBFFBFFLRR
BFBFFBBLRL
BBFFBFFLLL
BFFFBBBRRR
BBFBBBBLLL
FBBFBBBRRL
BBFBBBFLLL
BFFBFFFRRL
BFBFFFBRLR
FFBBBBFLLL
BFBFFFFRRR
FFBFBFBLRR
FBFFBFBLRL
BBFFFFBLLL
BFBBFFFLLR
FBBBBFFLLL
BFFBFBFRLL
BBBFFFBLRL
BBFBBFFLLL
FBFBFBBRRR
BBFBFFFRRR
BFBBBFBRRR
FBFFBFFRRL
FBFBBFFRRR
BFFFBBFLLR
FBFFBFBLLL
BFFFFBBLRL
FBFFFFFRRR
BFFFBFFRLR
BBFFBFFLRL
FBFFBBBLRR
FBFBFFFLRR
FFBFBFBRLR
FBFBFFFRRR
FFBFFFFLLR
BFBFFBFLRR
BFBBFBBLLL
BFFBBBFLRL
BFFBFBBLRL
BBFFBBBRLL
BFBFFFBLLL
FFFBBBBLRL
FFBFFBBLLR
BFBBBBBLRL
BFFBBFFRRR
BBFFBBFRLL
FBBBBBFLLL
BFFFBFFLRR
BFBBFFBLRR
FBFBBFFRLR
FFFBFBBRLR
BBFBFFBLRL
FFFBBBBLLR
FBBFFFBRLR
BBFBBFFLLR
FBFBFBFLLL
BFBBFFBRLL
BFBFFBFLRL
BBBFFFFRRL
BFBFFBFRRL
BBFBBBFLRL
BBFBBBBLLR
FFBFFBFRLL
FBBBFBFLLL
BBBFFFBRLR
BBFFBFFRRL
BBFBBBBRLR
BBBFFBBRRR
FBBFBFFLLR
BFBBFBFLRL
FBFBBBFRRL
BFFFBBBLRL
BBFBFBBLLL
FFFBBBBRRR
FBBBFFBRLR
FBBBFBBRLL
FBBBFFFLRL
BFFFBBBLLR
FFFBBFFLRR
BFBFBFBLLL
FFBFFBBLLL
FBBFFBFRLL
FFFBBFFRRL
BFFFBBFLRR
FBFBBBBLRL
FFBBBFFRLR
BBFBFFFLRR
BFBFBBFLLL
BFFFFFBLRR
BFBBFBFRLL
BBFFFFFLRR
BBFBBBFLRR
BFBBBBBRLL
FBBFBFFRLR
FBFBBBBLRR
FFBFBBFRLR
BFFFBBBRRL
BBFBBBBRRR
BFBBBBBRRR
BFFBFFBLRL
FFBFBFBRRL
FBBBBBBRLR
FFBFBFFRLL
FFBFFFBLRR
FFBBFFFRRR
FFBBBFBRRL
BFFFBFFRRL
BFBBFBBRLL
FFBFFBFLLL
FBBBBFBLLR
FBBBFBBLLR
FFFBFBBRRR
FBBBBFBLLL
FFBFBBFRRR
BFBBBFFRRR
FBBFBFBRLR
BFFFFBBRLR
FFBBBFBRLL
BFBFFFFLRL
BFBBFBBLLR
BFFFFFFRLL
FFFBBBBLLL
FBFFBFFLRR
FFBBFFFRRL
FFFBBBFRLL
BFBFFBFLLL
BBFBBFFLRL
BFFBBBBRLR
BBFBBFFLRR
BFFFBBBRLR
FFBBFFBLRR
BBFBBFBLLL
BFFBBFBRLL
FBFBBFFLLL
FBFBBFBLRR
BBFFBFFLLR
BFBBBBFRLL
FFBBFFBLRL
BBFBFBBLRR
BFBFFBBLRR
BFBFBBFRRL
BFFBBBBRRL
BFFBFFBRLR
BFFBFFFRLR
FBFBFFBRLL
FFBFFFBLRL
BFFFBBFLRL
FBBBFFBLLR
BFFBFFFLRR
BBBFFBBLLR
BBFBBFBLRR
FBBFFBFLLL
FFBBBBFRLR
BFFFBFBRLL
BFFBBBBLRL
FBBBBBBLLR
FFBBFBFLLL
FBBFBFBRLL
BFFFFBBLLL
FBFBFFFLLL
FBBBBFFLRR
FBFBBFBRRL
BFFBFFFLLL
BBFFFFBLLR
BFFBFBBRRR
BFBBBBBLLL
FBBBBBFRLR
FFFBBFFLLL
BBBFFFFLRR
FBBFFBBRRL
FFFBBFBRRR
FBFBBFFRRL
FBBFFBFRRR
FBBBBBBRRR
FBFBBBBRLL
FBBFBFBLLR
FBBBFFFLLR
FFBFFFFRLL
FBBBBFBRRL
BFFFFBFLRL
BBFFBBBLRR
BFBFFFBRRR
BFBFFBBRRR
FFBFFBBRRL
FBBBFBBRLR
FBBBBBBLLL
BFBBBBFRLR
BFBBFFFRLR
FBBBFBFRRL
BFFFBFBLRL
BFFFBFBLLR
FBFBFFBLLL
FBBFBFBRRL
BFBFFFFLLR
BBFBBBFRRL
BBFBFBFRRL
BFBFBBFRLL
FBBFBBBLRL
FBBBFBBRRL
FBBBFFBRLL
BFBFBBBRRR
BFBFBFFRLL
FBFBBBFLLR
FBFFBBBRRL
BFFBBBBRLL
BBFFBFFRLL
FFBFBFBRRR
BFBFBFFLLR
FBFFBBBRRR
FBBFBBFRRL
BFBFFFBLRR
BFFBFBBLRR
BBFBBBBLRR
FBFFFBFLRR
BFBBBFFRLL
BFFFFFFLLL
BBFFBFBLLR
FBBFBBFLLL
FBFBFBFLLR
FBFFFBFLLL
BBFFBFBLLL
BFFBFFBLRR
BFFFFBBRLL
BBFFBBFRLR
BBBFFBBLLL
BBFBBBFLLR
BBFBBBBLRL
BFFBBFFLLL
BFFFFBBLRR
BFBFBBFLLR
FFBFBFBLRL
FFBBFFFLRL
FFBBFBBRRL
FBBFFFFRRR
BFBFFFFLLL
BBFFFFFRLL
BBFFBBFLLL
FBFBBBFLLL
FFFBBBFRRR
BFBFBBFRRR
FFBBBBBRRL
FFBFBBFLLL
BFBFBFBRLL
BBFBFFBRLL
BFFFFFFRRL
FBFFBBFRRR
FFBFFFFLRR
FBFFFFBLRR
FBBFBBBLRR
BFBBFBFLRR
BBFBBFFRLR
FBFFFFBRRR
FFBBBFFRLL
BFBFBBFLRR
BFFBBFFRLR
BBFFFFBRLL
FBFBBBFRLR
FBFBFFBRLR
FFBBBFFLLR
BFBBFFBRLR
BFBFBFFRRR
FFBBFFBRLL
FFBFFBFLLR
BBFFBBFLRL
FBBBFBBLRR
FBBFBBFRLL
FFBBBFBRRR
BBBFFFFLLR
FBFFBBBLRL
FBFBFBFLRR
BBFFFFFLLR
FBFFFFFRLR
FBBFFFFLRL
FBBFFFFLRR
BBFFBFBRLL
BBBFFBFLRL
BBFFBFBLRR
FBBBFBFLRL
BFBBBBFRRR
FBBBFFFRRR
FBFFFBBLLL
BFBFBBBLLR
BFFFFFBRLL
FFBBBFBLLR
BFFFBFFRLL
FBFFFBBRLL
BFBFBFFRLR
FFBBFBBLRR
BFBFBFFLRL
BFFFFFBRLR
BFBFBBFLRL
BFFFFBFRLL
FBBBFBFLLR
BFFBBFFLLR
FBBFFBFRRL
FBBBFFFRLR
FFBFFBBLRR
FFBBBBFLRR
FFBBBBFRRL
BBBFFFBRLL
BFFFBBFRRR
BBFBBFFRRR
BFFBBBBLLR
FFFBBFFLRL
BFBBFFBLLL
FBBBBFBRLL
FBBFBBFRRR
BBFFFFFLLL
FFBFFFBRLR
BFFBFBBLLR
BFBBFFFRRR
BFBBBBBLLR
FFBBBBBRRR
BFBBBBFLLL
BFFBBBFLRR
BFFBFBFLLL
FBBFFBBRRR
FFBBFBFRLL
BBFFFFBRRR
FFBFFFFRLR
FFFBBBFLLR
FFBBFFFRLR
BFFBBFFLRR
FFBBFFFLLR
BFBBBFFLLL
FBBBBFBRLR
FBFBBFFLLR
FFBFBFFLLR
BFBFFFBLLR
BFBFFFFLRR
BFFFFFBRRR
FFBFBFFLRL
BFFBFFFLRL
BFFBFBBRRL
BFBBFFFRLL
BFBBBFBLLL
FBBFBFFRLL
FFBBFFFRLL
BFFBFFBRRL
BFBBFBBRLR
FBFFFFBLLL
BBFBFBFLLL
FBBBFBBLRL
BFBBBFBLLR
FFBFBFFRLR
BFBBFBBLRL
BFBFBFBLLR
FBBBFFFLRR
FBFFBBFRLR
FBFFBBFRRL
FFFBBFFLLR
FFBBBFBRLR
FBFBFFBLLR
BFBFBBBRRL
BFFBBBFLLL
FBBFFBFLRL
FBFBFFBLRR
FFBFFBBRLR
BFFFBFFRRR
BBFFFBBLLR
FBBFFBFLRR
FFFBBBFLRL
FBFFBBBRLR
FFFBBBBRLL
FBFFFFBLRL
BFFFFFFRLR
FFBBBBBRLR
FFBBFBFRRR
FBFFBFFRLR
FBFFBFBRRL
FFBFBBBRRR
FFBBBFFLLL
FBFFFBBRRR
FFFBBBFLLL
BFFFFFBLLL
BFBBBBBLRR
BFFFBBBRLL
BFBFFBBLLL
FBFBFBFLRL
BBFFFFFLRL
FFBBFFFLRR
FBFBBBFLRR
FBBFFBBRLL
FBBBFFFRRL
BFFFBBBLLL
FFBFFFBRLL
FBBBBBBRLL
BFBBBBFLRR
FFFBBBBLRR
FFBFFFBLLL
BFFBFBBRLL
BBFFFFBRLR
FBBFBBFRLR
BFFBBBBLRR
FBFFBBFRLL
FBFFFFFRRL
FBBBBFFRLR
BFBFBFFRRL
FBFFFFFRLL
FFBFFFFRRR
FBBBBBFRLL
FFBFFFBRRR
FFBFFBFRRR
BFFFBFBRRL
FBBBBFBRRR
BFFFFBFRRL
FBBFBFBLRR
BFFBBFBRLR
FBBBBBFLRR
BBFBBFBLRL
BFBBBBFRRL
BBFFBBFRRR
FBFBFFBLRL
BBBFFBBLRL
BFBBFBBLRR
FFBFBBBLRR
BBBFFBBLRR
FFBFBFFLLL
FBFBFBBLLR
BFFFBBFLLL
BBFBFBFLRL
BBFFFFFRRL
FFBFFFBLLR
BFFFFFFLRL
BBBFFFBRRR
FBFFBFFLLL
FFBBBBBLLL
BBFBBBFRLR
FFFBBFBLRL
BFFBFBBLLL
BFBFBBBLLL
FBFBBFBLLL
FFBFBBFLRL
FBBFFFBLLR
BFFBBBFRLL
FBFBBFBLLR
FFBFFFFLLL
FBBBBFBLRL
FFBFBBBRRL
FBFFFBFRRL
FBFFBBFLLL
BFBBFBBRRL
FFFBBBFRRL
BBFFFBFLRL
BFFBFFBLLL
BFBBFBFLLR
FBBFBBFLRR
BFBBBFFLRL
FBBFFFFLLL
BFBFBBFRLR
FBFBBBBLLR
FBBBFFFRLL
FFBFBFBLLL
FBBBBBFLLR
FFBBBFBLRR
FFBBFFBRRL
FBBBBBBLRR
FFBBBBBLRL
FFFBFBBRRL
FFBBBFFRRL
FBFBFBBRLR
FFBBFFFLLL
BBFBFBFRRR
BBFBFFBLRR
FBFBFBFRLL
FBFFBFBLRR
BBFBFFBLLL
FBBBFBBRRR
FBFBBFBLRL
FFBBFBFRLR
FBBBFBFRLL
BFFBFBFRRR
FBBBFFBRRR
BBFBBFBRLL
BBBFFBFRLL
FFBFFBBLRL
BFFFBBBLRR
BBFBBBFRLL
FBFFFBBLRR
FBFFFBBLRL
FBBBBBFLRL
BBFBFBBLRL
BBFFBBBLRL
BFFFFBBRRR
BFFBBBFRLR
FBBBFBBLLL
FBFBFBBRLL
BFBFBBBLRR
FFBFBFFLRR
FFBFFBFRRL
BFFBBFBLLL
BFFFBFFLLR
BFBBFFFLRL
FBBFFBBLRR
FBBBBBFRRR
FBBFBBBRLR
BFBFBBBRLL
FBFFFBBRRL
FBBBFFBRRL
BFBFFBFLLR
BBBFFFFRLL
FBFFFFFLRR
FBFFFFBRLR
BBFFBBFLLR
FBFBFFFRLL
BFBBFBFRRR
FBBBFFBLLL
BFBFFBFRLR
BFFBBFFRLL
FBFFBFFLLR
FBBFFBBLLR
BFBBBFFLLR
FBBBBBBRRL
BBFFBBBRRL
BBFBFFFRLL
FBBBFBFLRR
BFBBBBBRLR
BFFBFFBRLL
BFFFFBFLLR
FFBFFFFRRL
BFBFFFFRRL
FBBFBBBRRR
BFFBBFBRRL
FBFBBBBRRL
FBBBFBFRLR
FFFBBFBLRR
BFFFBFBLLL
BBFBBBFRRR
BFFBBFBLRR
FBFFBBFLLR
BBFFFBBLRR
BFBFFFFRLR
FBFFFBFRLL
FBFBFFFRRL
FFBBBBBLRR
FBBBBFBLRR
FFBBFBFRRL
BBBFFFBLLR
FFBFBBBRLR
FFFBBBFRLR
BFFFFFBLLR
FBBFBFBLLL
BBFFFBBLRL
FBFFBFBRLL
BFBFBFBRLR
BBFFFBFRRL
FFBFBBFLRR
FBBFFFBRLL
FBBBFBFRRR
FFBBBFFLRL
FBBFBBBLLR
FBBFBBBRLL
BBBFFBBRLR
FBBFFFFLLR
FBFBBBFRRR
FBFFFFFLLR
FBFBFFFLRL
BBBFFFBRRL
BFBBBFBRLL
FFBFBBFRRL
FFBBBBBRLL
BBFFBBBLLR
BBFBFBFLRR
FBBFFBBRLR
FFBFBBBLLR
FBFBBFFLRL
BFFFFFFRRR
FBFBBFFRLL
FFBFBBBLRL
BBFFFFBLRL
FBFFBFFRRR
FFFBBFBLLL
BBBFFBFRRL
FBFFBFFRLL
FBBBBBFRRL
BBFFFBFLLL
FFBFFBFLRR
BBFFFBBLLL
FBBFFBBLRL
FBBFFFBLLL
BBFBBFBLLR
FFBBFBBRLR
FBBFFBFLLR
BBFBFBFRLR
BFFFFFFLLR
FBFFFBFRLR
BFBFFFBRRL
FFBFBBBLLL
FBFBBBBRLR
BFFBFBFLRR
BBFBBFBRRL
FFBBFFBLLL
BFBFBFBLRL
FFFBBFFRLL
FBFBFBBRRL
FFBBBFFLRR
BFBBBFBRRL
FBFBBBBRRR
BFBBBFFRRL
FBFFFFFLRL
BBFBFBFRLL
FFBFFFFLRL
FFFBBBBRLR
FFBFBBBRLL
FBFBFBBLLL
BFBBBFBLRR
FBFFBBBLLR
FFFBBBBRRL
FBBBBFFLLR
FBBBFFFLLL
BBFFFBBRRL
BFBBBFBLRL
FBBFFFBLRR
FBFFFFFLLL
BFBBBBBRRL
BBBFFBFLLL
FBBBBFFRRR
FBBFFFFRLR
FBFFFBBLLR
FBBFBBFLLR
FBFBBFFLRR
FBBFBFFLLL
BBFBBFFRRL
BBFBFBBRRR
BFFBBBFLLR
BFBFFFBRLL
BBBFFFFRRR
FFBFFFBRRL
FFBBFBBRRR
BBFFFFFRLR
BFFFBBFRRL
BBFFBFBRRL
BBBFFFFLRL
BBFFFBFLRR
FBFFBFBRLR
BBFFBFFRRR
BFBFBFBRRL
BFFBFFBRRR
FBBFBBBLLL
FBFFBFBLLR
BBFBFFFLLL
FFBFBFFRRR
BFBFFBBRLL
BBFFFBFLLR
FFBBFBFLRL
BFBFBBBRLR
FBFBBFBRRR
FBFBBBBLLL
BBFBFBFLLR
BFBFFBBRLR
BFFFBFFLLL
FBFFBBBLLL
FBBBBFFLRL
FFFBBBFLRR
BBFFBFBRRR
BBFBFFBLLR
FFFBBFBRRL
"""


# In[52]:


def split_line(line: str):
    row_b, col_b = line[:-3], line[-3:]
    return row_b, col_b


# In[53]:


def map_to_bin(s, map_0="L", map_1="R"):
    remapped = s.replace(map_0, "0").replace(map_1, "1")
    return int(remapped, 2)


# In[54]:


def calc_seat_num(line):
    row_b, col_b = split_line(line)
    row, col = map_to_bin(row_b, "F", "B"), map_to_bin(col_b)
    return row * 8 + col


# In[55]:


def aoc_5_1(inp=inp):
    return max(calc_seat_num(line) for line in inp.splitlines())


# In[56]:


aoc_5_1()


# ## 5.2

# In[57]:


def all_seats(inp):
    return (calc_seat_num(line) for line in inp.splitlines())


# In[58]:


def aoc_5_2(inp=inp):
    seat_list = list(all_seats(inp))
    min_seat, max_seat = min(seat_list), max(seat_list)
    my_seat = [seat for seat in range(min_seat, max_seat + 1) if seat not in seat_list][0]
    return my_seat


# In[59]:


aoc_5_2()


# # 6

# ## 6.1

# In[1]:


inp = """gsvdkufnoawjmhp
wvhusojpnikgfadb
vshnpfedgwajkou
aujodhskfvnpgw
okpdnwhsfvjguqa

juedvq
vqeduj
veqdju
eqduvj

cdajbuernxm
mnucjearxbd
axrmdejuncb
jrebucmdxna

kutplibdoqzfvhw
qcewmrkdvhl
qobdwvlkgxhpasyjn

psbjhnatxe
pnaxesjhbt
tpxhbnseaj

yskvjqacinfdrphwltxgzomueb
jwprnxzvkeofthuqbyimadgslc

hzwepdg
lwf
wy
lw
rw

sdgateubqmznhjk
xyphltd

dbhl
hdlb
dbhl
hbld

inkxywsbgjuvpztrecadqmhf
qkaxszcujwvmbhdietpgr
krupsdgibzecxwvhqatmj
qtpxerobhisgcumkwjvdaz

bgakcmh
gxasvzu

cjtrvhinaqsbpk
jvxtspaqbhkfnrc

nab
bex
qmkudf

uot
out
tuo
uto
out

sbtkzf
hbkfzs
szbkf
fuzksbx
jskrzbf

dkphfoybsagcrnq
oybunchapqrdks
bokpysdhqnarc

bchumknwairvlf
cvbuhwzirkalfy

bwnseiaoqyjf
josqanfbew
nealmqbfwojs
jqnbfaoesw

sowzuji
wojizu
wzojiu
jwozui
ujiwoz

kcopqbt
tpkudorbc
pmtwogjb

uxkfthszqdbelomwri
tlusezbomwfqrdxhki
rsdfkbteoqilzmxhuw
bwkqmdsxhrfulietoz
izkwomsdlbfxetqhru

kzhwyodlvpt
kvfhldwpo
lvhypokdw
opwjhvdkcl
kpahtdolvw

cldyjpuitah
upcthlijyda
icdauhpytj
haypidtucj
jidaptcyhuo

mi
ti
qjwiz
oudehsxyiv
bpirjl

stlyornuk
cxapqwie

kharunjiebzvoy
gvaihtklnqmcebf

t
lt
t

ohca
lznkumqfgyjsbeot
owxdivpr

dy
yo
xsy
yo
pyrvh

iaxp
afpikux

hpsfqrnevzxl
fnrsvexzhqup

cp
fpc
cp

nbuojxgqckrwzspehf
mhguoxsfkejwcq
kedqujsomfxhwcvg
ouqefsxchgjkw
qcjohwxfseugk

rybnlomq
fmxsngauo
embkon
nlmvob
bomhnv

gptixlduzjeqkorsamwnh
pgzwohfjkuvbtylmc

thcgo
vhrlxmo

kbfgmhpzoqysac
ockazbsmhpgqfy
kmcqfyzhapgsxb
qcfdlwyarzuskhmbg

surovlcihp
irvlpuhosc

rd
d
td
d

koasgulh
kroumtzl
yubkwolnpj

dqykvasneb
easknpbovyjd

wqvop
nwqvpo
wovfrqizh
onqpwv

uskotfndjeplixhycbqrmw
mbxoewypcfdhistn
ydtvpbfemcnsihoxw
ynwbtosmcipxhfde

urgvbqechawznsjltixody
swdbnevcatrflguhziyoqxj
sgiwelhanovrbjuzyqtdcx
vyenojuhxwzbtigsdqarkcl

jxcwblszo
khrwvnbdolgjufyz

n
r
d
r
bd

tolrypvdwmb
lwrmopdvybt
rdybwmvplto
vlwpyrbmotd
ybolwtvprmd

radvoplnq
lrqpondva
lpanovqrd
lpanvoqdr
dqorvalpn

fvxca
vacfx
fvcxa

jbeixdakgolpfhqyntw
purbsxvjfwhetlmcnz

jztfgbmnkadiehv
djhpntcizmkgvbfe
btegdfknizvmhjl
igbdeztjfkhmnv
iqvtgejanzfdbhmk

jpi
ijp
ijp

kydp
viykd
dgyqmftwx
vdye

sewpkrvh
ekorswnp

bplerysifmzvwoncjxqk
nsbeqowitcpjymxvl

nexbskamprd
xsmdbkaupner
dsbnekarctvmpx
nkapxcbsmrlde
ezfdhnakwrsmyxpb

olnuzvxcgpdtfb
tgzcfdbnxp

vjliksorxpmwecaznu
giuoxsvnzewljpmc

fuljpkt
cplftukj
lfptjku
futpjlk

tqcgihveyswu
ywvqecthgs
cqhwetvsyg
qvshwcegty
gyctwqsfvhe

uhezlyxwvpcidr
hvucplszbxywer

jchyntk
revwzsm
kdn

cotikdlpxauzb
uxzptoksqbdiw

nqvruwhtombs
tebfnykzmlgcj

ciwkhzbmgfqo
uwmzgbcoihqkfs
fkwmziohcgbq

shezgrvq
gprveokq

jvqcdiuyrnpgh
dyjqvhrpic
xjiklpfzmthrwdsyqv
pdyvochrunaqjgi

denpjgywacrk
jbypwarecukdgn
zacqyxdgejrmpwkfnh
uwldpkrgaenjcy

q
mq
q

d
c
d
d

cdazeitlrpxnfqs
nrqxelfocsihpz
cnkveyiujlbzfgrpxq
cqznxrfliedp

qicgkpjzlxonv
cijozlhkqxnp
pgkcnloyxzj
japmxlknszotc

bytg
mwetjayhgiup
gyt
ygt
tyg

zx
elxz
z
vncto

nryw
rywn

takqgijzforxpshm
ztmrxfqgsiphjaok

fsaoqe
wcavsldeytn
auoekhzsi
hgseja

whqyvldpintefaxgurjc
xluqrgsvnacykptefbdhmj

oylknhsgmpawziqte
znhmatkpolsw
pkvmtznhlwsoa
onzamhltkpsw

zs
zs
zs
sz

e
a

xmi
gahfrd
yt
jmy
nqy

zkbtfdjom
ot
uoqtr
eot

g
er
g
g

ncvwupezd
cnvdwzpeu
cuwnzvedp
cdnzevwpu

bkuwcsv
bqcsgwve
mbhcovjsw
qwrnbeycsv
lisvbwc

vlys
omvzl
ptlejv
xylv
vxol

mqgohwtz
rqomlcw

rgopxhkslqcjmzbatnd
phgzmojlstadqrxkbn

pcbziv
pivzbc
jilczbpv

gmrecszl
zgrecslm
melzcrgs
gezcrlsm
mcsezrlg

ceotvxaydplfiu
vbzcaxuokwd

gy
g

lj
neocbiqjt

foyawivmhs
fayowsmzrv
mksfowvzayg

sivthk
yh
lh
ybhq
hy

fk
ka
vka
qhjxrzmckpb
kf

s
s
s

iyth
tyhri
yrtaih
htyi
utifydhq

hwxd
xhwd
hxwdb

kfhsvbjdwxcnt
dbfjhsctkvw
sogzdhjqiwmlyuvf

v
nyx
v
i

ncimwelvbudtp
piwvudaer

aktpdrhm
dtapkhr
dhapktri
taprnhdko
krpdhta

fvpaxk
zgmrwja
ar

vxoisla
olisvxa
kioqvrlxjhsya
oixgalsv
savloix

ac
gr
c
tl
c

fndwqsruzagei
dwunqfaesgzri
bzarmfnqwuisgde

jr
rj
jr
jr

zrevhj
xigdmqatk
wjlpzvsy

qijznvobp
nzbojivdpc
vzipojnb

srbtecvpixam
hdvctplmfxuow

bf
bf
bf
bfex

g
g
g
g
mag

b
y
b

vmbwhdfiqteglnpkxucjoa
wmqdconxbuaetjlgphivkf
upadfnhkwtjioqcbvxelmg
gofjubptnmkelihwxacqvd

alev
evla
alve
avel
aelv

uceyogrhl
oqcafluvhewgr
ugcxlhorpez
nduzshrceglox
odmgbeucrplh

ugesfliovyzja
nlizsujfadgo
lfguaszotij
osznifulgadkj
xadguljioszf

kpgve
vqsfezungalxidb
gwteov
gpvcyjrmeh

apuonkxtc
xithys
hfvtsx

pgtzamyqeu
gtiuwpcqzvya
tpqauezyg

souvmglcqbekzi
miuzvksocgqbel
gzqkmsubevolci

ndvahciz
jaoyhepsbirw

bghijfkotcxwu
uaokxsfbleyhgqr
hucfokpwbxg
nbfuztgovhxk

zghianxtlq
qthdvingxalkz
wfqnixgteza

lhzcrodupwqsv
phsvrzcldoqwu
hogspqwcvukdz
hwzpucdsqvrol

txkqmsfbglhnoypaduiv
navlozmpthwsbkiqxdfu

gidnojlbtfpskuwavyxczr
irvsyznbtedxougfwc
sovxhcqdbwytzmugrinf

mcjnraketsgvqyxpbuwlhzdof
kqudanprgiejcftzlywhsoxmb
rcxmkdqfohjzgtsalbpunywe

o
cm
rc
m

tmkbedxgzsw
tdgmsxbzkernw
ktdbxzsemgw
gwkmestbdxz
xzdewgtmskb

evpdgzcu
gepcvzu
vegzpuc
vpuzgec
cvpgeuz

wfsadgtuizejmylxq
aspmuqigbxeljdtwfy

ygbtdp
tye
fryaitjcukhl
ytdm

jfm
m
m

cl
cl
lc

qbodnftrsygi
iztorbfskqdvng
onpsgqrdtif
mnrofcuqwdtils

mhavcgzlrtbo
jrldgavzqbcxoh

pshtdbifrvzqmklyae
tfajgrpkidzyhslebmvq

cuzbjepnvis
isjbenvyzlcup
nagieshzcpqmfuvbj
ezvpsjrnciub

ywgdsafzuxbrmhvqkljnoipc
hjcntvrzwdfbxksyiqolpumag
kwvpybmjeoualxcsqgidhfnrz

zubvkn
cuwfsnv

isknfdalujeg
hikagvpzx

szgfhjtxid
stdgjzxfih
xghsjfdzit
gfjixszhtd
fzjshdtixg

uibgxka
abigukx
xubakgi
gxabiuky
bkaxgui

tjzor
slaore
gxwnoifudmcqvpk
obhr
tyo

q
y
e
r
ifdcxzm

fvtqrjsblkhuoiey
gyfnizlqupvscobt
bouiftlcvqsy
qdvlyfiusgotb
qvbycwsifluto

ifmnxbcvpkylruh
nckrmfphluixvby
vbcmxyhurnpilfk
suiqbvyrxcphmfnlk
ynuxkrfvibclpmh

pmvdyexsoilatqfgk
lpidgatmqevkxyso
gkpsaoleymqxvtdi
gmvxeyplqdoasitk
vkpdylstquegaiomx

ymogxuswkce
vbxznpscg
xlcgs
xclbdsng

zovwtiy
zrjlciov
ksxefuvqdam

cwvsx
xeuwyhsfb

hxwgolksbrdmpifye
lwpyefxmiohdnbksgr
gzoehypbldxikmwtrfs
sdlwpeymxifrbghok
glmbhykiofdxpwervs

ndcphgqfuvsekaxozri
xofkqnbschdaveruizgp

ptkvdhjaw
skhtapidwjn
thunakpjwd
eaglphkdtjcfw

pnezvfgiouahmslkdxcrqb
fpiqsecxaukbvzgnorjhwdm

emcwblgxuvnkzrdsoyjf
rvsxeugkmwzfncojlb
nhbiclvskjrupgxzfeomw
gcxlbjozeiufwnskvrm
eonjkwbzfxgpruvcmsl

ntgia
ia
ai

scoernukhwtigpd
bogiserhpucnkt

eaipzg
gne
lughe

tbipylmnrague
tbargijepmhuynl
triyzgupnbmale
prtnumgaibley
peblaytmgnrui

rqlsepfhiv
fvelqphsri
ilfhvqerps
fheqplsvir
sfpvehirlq

jciwxfbhqkadgzloprnuvsty
qwouetsmhykavxfbjzrglc

fjmz
mjczf
unkzjm

gebyncxsphfokwm
gmchsnbwkpfyxeo
fybkhcesogxpwmn

ud
whjn

ihm
hmi

p
p
yp
sp

ytrwx
yrtxw

p
d

ieltygdukac
yiudeakg
kpegdaiyu
audykegi
aeqydwiguk

lb
ei

zjvctfndgiqbeu
abfwndutvecqigz
fznbdutevigcq
qtvzfnueibdcg

g
i
x
g
g

qhm
lq
nq
pqsb
lvq

qnxpslvajf
xuavcnst
nsyabxv

ocu
uco
acoux
cluo
coun

jtgzodebq
ojztqdgbe
oejrqzgtbda
tjzbqedgo
gzqtejobd

ubglorcsyvmxd
oentwfgulpqikdcbzhj

jwkmxdnyvbiz
qebnoyfz

bepdfi
ikepbof

cofgekndbatpruhqmwvsiy
bsqtrakeudopghvyfmcnw
qgusdwvabytmfkcnehorp
qfhruygwkvmbpaoestcdn
prmkbuvynseatdoqwfhcg

enczdvbkiyjgruqp
bdiqvwjurpycngzk
bnrcejupvqiwgzkyd
pqgybrcjzkudonvi

fygasxjwrb
ijsgafwyrbx
syjawbxgfr
wfbrgvsjyax

xtp
bfnzuadh
xlce

rxmeqcbv

fjtdihkrbyn
htfjyinkgdrb
fibgtkdryhnj
hkbnjrftidy
intbxjrkfdyh

nhkiqjocfgxmrvwetd
ghnfdjvqtxwermokci
xnrtfkhdwcmjvoeigq
mcvfjhwiqtnrekogdx
imhxgjwrodtcknqvef

sabwqu
yqamws

usei
xkvnyfi

rcewysztbiamhpgldj
kibrfndmgeazcsh
adrzgchmwjsbie

pnrwvx
lwjxnu
vwxinb
pfxybwng

wnvxgfdkubzrmip
kmjhoigltwbz

znlgbx
fla
dl
l
l

jgeqcikplduzxrwby
kwplxgcbndjqyizuer
ewrqujilgyxpdzcbk

guteykxsqrfwhz
mhiurkswtqbxz
sdlqxvowujrhkz

zrejn
nzrje
jnerz
rzjen

fvkouigderaqbjth
eqrvwjinfltzpcuag

stqcrpy
ctsqpyr
ptyqrsc
ymsqrcaptb

egftpqosiv
ecjdqlnmwouf
spxaqofre
epogyfqi

oxwgtshjqef
pbtgjfeqhnoxw
jfhewygoxtq

jwavgo
ogevbwdjai
ogvahjw
wrajvog
ogsjwarv

rpucvg
cgpr
htfelpc

hqrwapscubelovxntd
jisztpnbcahlfdoqmvexgk

pmadwutiejznofcgvsbqyxh
qvmzbaisgfcunwjexhpdktyo
xtvsdnqaucyehgzbjiopwmf

vjqih
himjwdv
hsojivb
jtrklivehyg
mvnaizoqpfxhj

j
j
j
j
j

dpnwmtvklc
ndjpkm
ndmpk
ndmpk
ndmpk

ucojsptiqymhewbxvrfdkngl
ebpjwuxrdqkmsochvfgliznt

esroiaqdbxnjhut
xibuqhmensdajo
feukjbahdxwqnsiocv

vkxzclpmtujngerawod
azdrgcenvjxptkuolmw
onrluajvcgewpdzkmtx
xamlobkrvzwpjgnucdte
tvenjdmlzpwugkoracx

ywpfhztklgjmoien
nyelduixgvwmojpzhtk
lehpigtmoknjyzw
gmhwzokylpnteji
tmypejhwgzlniko

fmd
jf
fj

l
v
ntobg

drmzvt
rxtsfuk

vxdlpjkrsz
dgxkprvzsl
dsklxpvzr
pdvxzlrsk

gwip
gakpw

kbcadn
bakcd

mhpstqcgvoalkwxinebryzujd
qwhirveoczyatgjdsmkpxnl
mejazlincwodtshxkrpgqyv
fsaizhnkcvwolgjpdqxtmrye

rxubznovy
yvudnrbz
zvunwcyrkb
ntzbryuav
ndvytuzrb

utvklrxypgbnimsdofwa
fyzliqswjmtpvdka

byctfzx
pxzf

g
ik
ykei

bcajzwogvetd
gedbcwtzvoaj
hcwogaxjbzvted
eoczjagtdwbv
atvdjbcozgew

wsclketugyaz
qvfbjcxtmilgow

amgirw
yf

iletugq
hnoxbfkaspt

qjdfcpvksmxzywahgn
wnzceyskgpoxdhlmravjqf
xjgvhcsqyfankpzmdw
jyncdxwsqkvphfamgz
dvznygwjkcmqsxahfp

fkuwiezpljbdayhsr
rphwbeujdzlfiasyk
erdhpafkzbwjlusiy
jwfhkrzdeabpliusy
wfipeujhylazbsrkd

fqmbwapvouelydgicj
uelvqwomtyfjgcpadi
qkpcsdeyjiwarovnglfum
ijvgqdauoefpcylwbm
ydmqpfewaovlicugj

sgbq
ltqambf
djbuvn
zmtbgy

egvifnsaztxqcrywumj
aqcxujnzvfwetrhgm
fxdmtkgawplobqjenv

bxuwpnl
ztdkau

ecylsbdv
cvzlsbeyd
yqcveblsd
beyvlqcsd
ebsvdycl

eb
xpnyter

cbhqyzresnpxfwm
cwksfvhxqperbimz
whqzpbcsjxafre

beodiasvj
jbisdoave
iedaovbsj
jxovacsiebd

prxsnyehgwifbzo
ozpbsxynfiwrge
ribozypewsxngf
nyoxspzbfihgewr
rxzewpbnimfoysg

shviadjcue
weduziolmcbngp
vqdieycu
cudeif
dicyuqke

nvcwhuo
sltchuwnq
unwhci

ekrisbvx
rsxiev
exnrvsi
srxevi
xhsvnrei

rs
rs
sr

fuzjmek
tihf

ptlzxreqfdchibogvysmku
pceyizvdkqxbhrtulsfmog
gvkrxfsbipqedlyzomhtncu
suyzgrobilxhmcfdtvkeqp

okfvjneqyicuthwsmpxl
wdojlsqknyhmptvicfe
nyfjthmpivqgsulwkboec

ufrpkliqjgwxeybmcztasovh
qvkpyghxblewsaitrmzuonjc
giptzywrejquxkoavslcmhb
peaywubjozmcgrihlqsvxktf
lehjpzguiksacobxywtmvrq

egryz
ergyz
yzegr
yfcgzre

j
j
j
p
j

bjt
tbj
tjb
tbj
jbt

cklp
lpck
lckp

fea
eaf

qgm
dz

yri
yi
zypdi

ekwjxhtmgiudpz
xepuhgwjizkdrmt
ezghmliwtxujdpk
wdhxpjizugkemtl

gyokbspj
kbgsopyj
pykhdsjbgio
opjykusbg
jygbsopakc

ixorlekwgnbcjm
lrjkwxgie
wgeikxjrlh
rlkjxipeqgw

ecgmdrykq
myrclqdgek
guqmzyceprkd
dygckwerqm
yrcgkiqempd

u
u

bcwnvl
fcvsib
hcnvb
cpgveoaby
ivbcn

n
n
n

macuqyp
fs

pbout
suota
cuotm
atmuo

nlravibecfj
eilcjafn
aeibjfl
jxfeilauo
jafesdnli

xfwroij
fxwijor
irxjofw
rfjwboxi

dj
dvj
dj
dj

mikhxcqensrodu
imcvkhewgljupsxonq
kceuqxltinhsom
kzqanoemcxhius
vmuoxineqpzhacbks

hklcsoaywpfrdntmu
xirbzckwjvpfygeno

o
to
o

zvirefunh
ezhirnvfu
runifzhev
ezivhnrfu

zfsoducbpai
cupdisobazf
aozbsucfdiypv
bcfazodiups

njfprukxamlg
kpfrjgynulxma
pijflgnuxkram
pkuxalrmjfgn
nkvrlmxustpfjga

dszgm
rsmu

iaw
aiw
wai
aiw
iwa

s
s
s
sl
s

eyavhnk
keov
qeiwfkcgvrpsld
kuvze

a
mh

ilqchdfsog
igscolmdzq

fnyhxmpct
lchdpamfu

vijz
vj

dhpxjrmyuefclvqgni
uicskweohgvfryxmdq
tqgdifymexbwckruvh

c
c
c

lthidumvycszw
cvpqjeuhlwrfyzg

keocuw
uckowe
oekwcu
cwukoe

c
c

lkxjv
jkvxl
vxklj
jkvxlwg
zkxvjly

sqlamxeuhpgwjbdcioy
bumyjxsiqweholpgcda
gecswjlqhadiuboxmpy
syahibgopexwlucdqjm

igebmv
tawqvezdsmpunk
rimocvgje
evmbhc

ykjisvfatux
jfaisyvktux
itksajfxuvy

fclkush
slcykdbgu
fskuchl

xjhulywagzeioq
oejlfsquhbriayxwg
jiexgylwzhuqao
wyxhqljagieou
hwladixguqejyo

sofcbhuwyqtid
icofdwsb
dfwovimbcs
cwibodnsxf

jqnestpyaczfmxhwrbuvldi
mxanrhbfcujvyzditwlo

ntfgivkyszmarc
qrajdhowuvpclbex

kliwy
ukwlryi
ilkyw

pmgltzsk
ljmipztvgow
zltmgup
umztglp
ftzmlpgk

twepi
teq

ohyd
mytjrwk
hfy
exyh
ye

rzsqhtlowavy
twvhzyrjsqaol

yzagcqrjeimwxokh
fmxtiagboleqcwdrhzk
opvemhasrguxkcqzwi

atcpeyosnrjbg
kcesobgua
fagsev

ca
ac

xahmtil
hximtla

hyutnjdrbsmofl
dswjfyothmblrnq

et
te
eqt
tuje

nbhpwzgtrcx
gqcxobhriznw
hwnbugrejxtczs
cujrbxfhnwzg
gcwzhrxndjb

qwrfxhlyzcptvmkdeauigob
zbchavlkmryxiptegwfouqd
cfhuiptgqkoalrewzmvbyxds
hudmwcgbfepyitovkaqzxrl

eysuozkm
ndgloqyv
ignhwrovy

iqufgnvxspdcjtylkbrozh
inuzqktrvcxyhbgfosljdp

qhfknsyeuirzagvcwd
yfcgqnxewlkrsuazhi

lj
jl
lj
lyj
jl

kpholfxewrdt
opdfhtlmkwex
hpwftoxderlk
ylxhwdofnztkpe
rwfpxlhtdkoe

ubml
yvohg
zeasf
plum
qhnjxg

cjgzwmdyuakvixlprhfe
kmplfuxywergchzjvani
xcvlzmewyujgirhpfka
fwhgrxkjcvpeuilzyam

eclsiqp
ivgspoe
scepi
pmiadtskyze

akmdfivwgct
yvgcwakhdimts
lcvgirakwudtp
aftnckwmidgv

zuqblv
blvzqu
uvbqlz
qbuzvl
bzqxvlmu

by
betlcdvry
yb
bxy
gybjx

waoqdxpkmfnyrhjebcuvzs
qprvfczedowxknhausmyjb
cufdqvknwrajzybospmxeh
qkjzybeadvncwhxumpfsro
nwfkjxumpabzodvqychsre

shdfctjrkwbvemoxluyzipnqag
sgbwpeuqcilxojfynmrdhvktaz
lhgkxfwuzbevojmrpnqydsacti
gflnzjasbuyimxqcvwrdpohetk
ynwedhbskjtvoucgapiqlzfxrm

wlmjxp
ylnxoajk
luxjidte
xjrvlcdeu

pv
vbpw
wvuap
kceavp
rdphvoitqf

dlxzwkhtmc
twzhlmkdc
tcylhkdwzm
zwmlkdcth
gdhikmctlwsz

hpekwtlufyragqvb
kbrwatlupqyfvh
ucbvwlhfqatpkry
hlakvyuqrfpwbt
rubvwpfqlatkhy

npxobl
ckuhnplvx

edkpjycofasulrthw
rpuhcdyxlftosewa

stuvhwaexykzdorbfpi
shjuwgpfqmtacvlbirkzd

frph
wo
h
zumtyngcj
pfse

zivsgurp
szirpvg
gikvsprz
zigpvsrk
nvpsgzir

rfimu
hmqrlfxpbgu
nrmoyftu
nmujfr
rfum

bidzwmearovjkgcl
ogdbirkzqmclejvaw
gealcqozmijkbrvdw
gzakwmdbejclrivo
eolwifvgmrbjdazkc

iurfyqgwk
ymkvqfpwrig
aqrfywikg
bfdryxikgnwoq
cjfgkryiuwq

jvb
x

qkxnvfuopdytrzjgbm
bmqkuyarjgtdpfzsnox
obwjxyeqtingzmdrfkplu
gamupstryfokbzqdxnj

ymanp
npfshjya
pundyklatc
ypfanh

garp
grpa
arpg
argp

inedmtpwrvub
vwibertnudmp
idurbepwtmnv

yczoaplwmxibqgsfn
wbiuxyqzpncvgmsl
gpoltrbisqfznwxcymj

a
a
a
a

cgjviyufped
pcuvygzkjid
ptvigyjdcku

u
i
tqa
j
ul

zitbfuer
uzfithernb
uftbzire
uitefbzr

jcwkroamnegxvqsh
kejhanqmvcrxwsog
gaqmkexjvcsnrowh

taegslmuyqcipz
asytxrgdpfbcqliwz
tpgoschavqjlkyzi

oc
oc
oc
co

mrfvjlykquz
fzmvuleykqt
vykmzlgquf
kqfzuvygetml

a
s

ionve
eailo
jiomexwh
beziqpdco
ihtoe

cfjvrqosnwyedaubmhgtlxzk
olxzjfwrcytkbgudasvqhnme
tuwfnckrzsvjgbxdmyhqlaeo
txnydgufbmjaqkrzlwhoevcs
bgakxqmfsdwyjvelntchzour

njvkobzs
bsjvkwn

qmnluxw
ovgtikpdbrya
nchfsjqez

khtdryej
hdrtv
qnaodtm

as
aus

omjaixvgklq
vgkaxjihdrlq
ycxkzatpusiljqgv

jtepylmrqbiwk
xerlpmynqtkfbjwi
timwpbkegljqry
lqijkebmgpwyrt
qrkljpbytemiw

q
xqint
dkqb

trjmdxpoeqcwf
tfedxqcprwom
kmftwxqporncde

fpcmndhr
dzepjngqikcfrh
nhfpcrd

c
c
c
y
c

t
t
ti

tgfspxdy
sytgpfxd

zov
voz
ovz

ic
ieuc

vhesndkizjgwcpobulam
szjymxwopckfqtgdib

jdfzgqsbrmnticl
fbcdgqtznmjri
doitrczjqfbgmn
otzbjfidmnrqcg

cb
bc
cb
cb

aspjvghyurx
vcarwsbh
laeshvzrb
hsrvia

kpxzdhasfmltouvrc
duvpkascromz
vmcskupzorad

pguayqbwm
gpyaqbwum
ywaqgpmbu

ypdlnjse
elskbyz
jesylo
lyse

zlokqmjiurpwgbn
xzvurhgmlkwqnibjpo

wpzenbojcykqxvt
wnyzlbjkeoqtvcpx
itkjzydbpvoxcewnq

gfuvenodsizwmh
hwfuvsntdg

gkibnpalc
inkcgpal
gnpzliakfc

ibektdpuhg
iwbgjke
iycnergfqkbo
egxadvlmbijk

l
yjg
l

ymuoc
oymcu
oymcu
youcm
ycomu

wifoqy
zksfrict
bdpvhuilgejn
acoi
mqi

qrcukhwvzdjilpto
hqrmwkupclvjtizo

gdizlfawobuk
dihqfswcgukzrbla
gmukawbdfizlo

zwdrpv
dzvpwr

ycidkpfrqjelha
pjahykfecdqrli
kfqlajhdepyirc
pkhaceijlqdfry

pwuxbqotey
okbphqutfx
xvsgodubtlpqijr
puoewaxtbmq

qtbaoex
xpoqa
agiweqtop
nozuadmjrq

huvqdaij
fkuvaijdhq

biewrdlzc
rjlcikbzmdwve
leucwfpoizndbxr

avgtnubqcpxrhwdoml
vrkqgyndcmohtupswa

dmjqfesnxyciz
hfzudcjxsmno
mfjhrcsxznd
lcmbjnxzfadrs

tvayrhpqskd
qrtkvhyus
epjsytzhvrqk
yzqohmvtgsrk
hvlysqtwirbk

ieyd
aipeyg

r
rg
rm
r

qcweajhfmlgyzpv
ouqdxmsphkbatenr

fba
kfba
baf

vxpblsyjnrmkai
vpyhagcwqbzxmik
rpbytexdijnfavkom

fpmytnk
cyaw

jhyimdg
mhyij
hmvyij
mihezcovyj
yhmciej

sqfaopkgze
kxsecfphozq
qsotezpfk

ewcvoaurmjhq
cuqvjwreaohm
ewvjmqacuorh
wauhojecqmvrs

lyieuqdjcb
vkpctdmywzsreubn
delchbujy
jbcyegdou
xduayceb

nidxswarcqtk
kciqdarnbewsxt
acqrdkntipxlsw
ikpawtcdsqnrx

gikrfhwltveap
yeplvatowncgxirf
griadtewmvblpf

htjkmzxlvbygcwqioe
jzwtymxvigbheolckq
cxmvjyklobhtwgqzie
teczbxvlmgojqiwkyh
oxvejlbtiqywhzgmkc

jkfapozdwcie
bmushwjgltrn

rpnbxkoij
exjdri
uirjegxsa

zawoncbymgsrhv
dvctxgeusr
cvizgyhlmrwsfp

shnyujedctwfq
yscahxndftreq

xrnysi
itcluvmd
niqwozjber

gjobshlayxvctnfq
ljcxaonvbstqfgyh
ybhxgntqcsvfaojl
rjoxblqavncusgheytf
sncqlvybxfjtghao

uozb
ldewrck
xbg
xhg
z

yubqaznf
imwhrgnkjls

msvgjrnkcloaup
csxjnkgrpiuoveamy
pknvrajmcudswgzo
tnupacsxrgkvmoji
bpnkfarqumsvhcojg

bzvyuenaihfdcgwk
puchyenmzgksrijoa
ugebciktnlzhay

cedfutpnsivjlobrkaxy
denscvpbmlkxaojrfh

vugjrq
jqgtuwcnrv
grvkuqj
gbmvqsyxjueplzirhf
avudnjqgr

vpidajtmgozxwuksh
ughiwmakpjszdtvox
wugipxzdvastkhmj
sxughjakmnwfpdivzt
wimvaupjhgxstkzd

mqsuwhdxpcozfr
rsdwhfpakzxjmo
eysprldfqzowmhx
fodhrtmswxyzp

vsmzfbjhwqxiugtlc
gcqdsfmpletnhbxr

uxbgkfjwesmlchr
feakldxqnpwcjgvrzbhs
hjosrixfmlcgbkew

dszv
zsvd
vsdz
zvds
sdzv

pdw
lxudjpiwz
advnkpqw
hswpdog

gslpira
neuzf

ifjt
tjif
jfit
jitf
ifktj

jrnzb
unkjshpe
njza

ydigxaqm
iaeokqgmyhr

bkxmngtdlyev
nmbuzoveixlprkys

zjloghmtu
ermvzn
qzdncfm
afczxmp

aptscynieqmfgjhbr
bmsirnafyepthgcqj

q
qlr
fq
qk

v
v

ucrmbsozjkfy
buscrmofkzy
uosmfkryzbc
sqirbfzmocuynk
mbucykofrzs

lrp
plz
lrp
lp
lp

yfzmpgcsw
prycgfm
rfcmgpy
scgmyqpf
flcyvpohmgu

g
g
g
e

lxoaibjch
wudyrfvkzn
gtpmkeyqd

zjhlwbtfuvick
wujtvblzchkif

ksdfpvqbtxaluneo
dqofprhnxamskujeb

hacwigyftqblx
xwlqahitbgcyf
ahyxlwgtqifbc

mb
m
mg
m

ecrasdtyljuqimhnwfb
qleiaydjcugrwn
jdyewaqnrcliu

g
lqfio
adhstybz

gryzuxenhlvopbtmfwqcas
yeqzalmogbncxpsfujwh
mflqzhoaupcseygnbwx
myswzuonfqlaxecbhpgj

uwvzati
uzcjvtai
savuizt
atiuzv

cozuin
abuizo
tiozua
wilfzeoqu
roictxuz

gndpkojqu
gunkpsjoa
rtmzjpgkovwxlnuc

lrj
rjl
mrjl

udlpevjgzrfawitqs
qgrtiujslfeovza
surivgtfqjleaz
ezavgjtlfrusiq

g
fx
mf
tx
iyqd

sljgmdztynvrqexhwfi
gvwdyerlqnxthmjifsz
qgmjlfwrxztynivdhse

zkvuir
kvruiz
vriukz
kriumzv
zruikv

zyqgnvda
kdygvqanz
zyagvqdnu
qnwdmlaxgzyfvo
dnzgyavq

o
s
q

cbroy
qiyocmjdt
uyoc

lkqj
kjql
jqlk
ljqk
"""


# In[10]:


from string import ascii_lowercase as letters


# In[11]:


letters


# In[2]:


def split_inp(inp=inp):
    yield from inp.split("\n\n")


# In[22]:


def aoc_6_1(inp=inp):
    return sum(ltr in grp 
               for ltr in letters
               for grp in split_inp(inp))


# In[23]:


aoc_6_1()


# ## 6.2

# In[15]:


def split_group(grp):
    return grp.splitlines()


# In[46]:


def calc_group(grp):
    return sum(all([letter in person for person in split_group(grp)]) 
               for letter in letters)


# In[53]:


def aoc_6_2(inp=inp):
    return sum(calc_group(grp) for grp in split_inp(inp))


# In[54]:


aoc_6_2()


# In[ ]:




