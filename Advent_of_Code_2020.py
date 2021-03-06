#!/usr/bin/env python
# coding: utf-8

# # Setup

# In[1]:


get_ipython().system(' jupyter nbconvert --to python Advent_of_Code_2020.ipynb')


# In[2]:


get_ipython().system(' mkdir -p inputs')


# In[3]:


def put_away_input(inp, day, overwrite=False):
    import os
    filename = f"inputs/inp_day_{day}.txt"
    if os.path.exists(filename):
        print(f"{filename} exists. Overwrite? (y/n)")
        overwrite = input() == "y"
        if not overwrite:
            print("Not overwriting existing file.")            
            return
    print(f"Writing {filename}.")
    with open(filename, "w") as f:
        f.write(inp)


# In[4]:


def read_input(day):
    filename = f"inputs/inp_day_{day}.txt"
    with open(filename, "r") as f:
        inp = f.read()
    print(f"Reading {filename}.")
    return inp


# # 1

# In[5]:


day = 1
#put_away_input(inp, day)
inp = read_input(day)


# ## 1.1

# In[6]:


import itertools as it


# In[7]:


def aoc_1_1(inp=inp, sum_is=2020):
    list_of_numbers = [int(n) for n in inp.splitlines()]
    check = lambda x, y: x + y == sum_is
    for pair in it.permutations(list_of_numbers, 2):
        if check(*pair):
            print(*pair)
            return pair[0] * pair[1]
    print("No combination found!")
    return None


# In[8]:


aoc_1_1()


# ## 1.2

# In[9]:


def multiply_nums(nums):
    product = 1
    for num in nums:
        product *= num
    return product


# In[10]:


def aoc_1_2(inp=inp, n_numbers=3, sum_is=2020):
    list_of_numbers = [int(n) for n in inp.splitlines()]
    check = lambda nums: sum(nums) == sum_is
    for nums in it.permutations(list_of_numbers, n_numbers):
        if check(nums):
            print(*nums)
            return multiply_nums(nums)
    print("No combination found!")
    return None


# In[11]:


aoc_1_2()


# # 2

# In[12]:


day = 2
#put_away_input(inp, day)
inp = read_input(day)


# ## 2.1

# In[13]:


import re


# In[14]:


def parse_line(line):
    min_ = int(line.split("-")[0])
    max_ = int(re.findall(r"\d+-(\d+) \w: \w+", line)[0])
    letter = re.findall(r"\d+-\d+ (\w): \w+", line)[0]
    passwd = re.findall(r"\d+-\d+ \w: (\w+)", line)[0]
    return min_, max_, letter, passwd


# In[15]:


def check_line(line):
    min_, max_, letter, passwd = parse_line(line)
    this_many = passwd.count(letter)
    return min_ <= this_many <= max_


# In[16]:


def aoc_2_1(inp=inp):
    lines = inp.splitlines()
    return sum(check_line(line) for line in lines)


# In[17]:


aoc_2_1()


# ## 2.2

# In[18]:


def check_line_2(line):
    pos1, pos2, letter, passwd = parse_line(line)
    lp1, lp2 = (passwd[pos1 - 1] == letter), (passwd[pos2 - 1] == letter)
    return (lp1 or lp2) and not (lp1 and lp2)


# In[19]:


def aoc_2_2(inp=inp):
    lines = inp.splitlines()
    return sum(check_line_2(line) for line in lines)


# In[20]:


aoc_2_2()


# # 3

# In[21]:


day = 3
#put_away_input(inp, day)
inp = read_input(day)


# ## 3.1

# In[22]:


import itertools as it


# In[23]:


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


# In[24]:


aoc_3_1()


# ## 3.2

# In[25]:


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


# In[26]:


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


# In[27]:


def aoc_3_2(rights=(1, 3, 5, 7, 1), downs=(1, 1, 1, 1, 2), inp=inp, debug=False):
    assert len(rights) == len(downs), "not the same number of downs & rights!"
    product = 1
    for r, d in zip(rights, downs):
        trees = aoc_3_2_helper(right=r, down=d, inp=inp)
        if debug:
            print(f"Right {r}, down {d}: {trees:3}.")
        product *= trees
    return product


# In[28]:


aoc_3_2(inp=test_inp, debug=True)


# In[29]:


aoc_3_2(inp=inp, debug=True)


# # 4

# In[30]:


day = 4
#put_away_input(inp, day)
inp = read_input(day)


# ## 4.1

# In[31]:


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


# In[32]:


KEYS = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"))


# In[33]:


OPT_KEYS = set(("cid",))


# In[34]:


REQ_KEYS = KEYS.difference(OPT_KEYS)


# In[35]:


KEYS, OPT_KEYS, REQ_KEYS


# In[36]:


def split_inp(inp=inp):
    yield from inp.split("\n\n")


# In[37]:


def check_passport(pp):
    return all([f"{k}:" in pp for k in REQ_KEYS])


# In[38]:


def aoc_4_1(inp=inp):
    return sum(check_passport(pp) for pp in split_inp(inp))


# In[39]:


aoc_4_1()


# ## 4.2

# In[40]:


from functools import partial


# In[41]:


import re


# In[42]:


REQ_KEYS = ("byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid")


# In[43]:


ECLS = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


# In[44]:


def year_check(y, miny, maxy, digits=4):
    try:
        return len(y) == digits and miny <= int(y) <= maxy
    except:
        return False


# In[45]:


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


# In[46]:


RULES = {
    "byr": partial(year_check, miny=1920, maxy=2002),
    "iyr": partial(year_check, miny=2010, maxy=2020),
    "eyr": partial(year_check, miny=2020, maxy=2030),
    "hgt": check_height,
    "hcl": lambda hcl: re.fullmatch(r"#[\da-f]{6}", hcl) is not None,
    "ecl": lambda ecl: ecl in ECLS,
    "pid": lambda pid: re.fullmatch(r"\d{9}", pid) is not None,
}


# In[47]:


def parse_passport(pp):
    pp += " "  # append whitespace so regex is easy
    pp_dict = {key: re.findall(fr"{key}:(.*?)\s", pp)[0]
               for key in REQ_KEYS}
    return pp_dict


# In[48]:


def check_passport_2(pp):
    if check_passport(pp) is False:
        return False
    fields = parse_passport(pp)
    assert set(RULES.keys()) == set(fields.keys()), "fields and rules don't match!"
    return all(RULES[field](value) for field, value in fields.items())


# In[49]:


def aoc_4_2(inp=inp):
    return sum(check_passport_2(pp) for pp in split_inp(inp))


# In[50]:


aoc_4_2()


# # 5

# In[51]:


day = 5
#put_away_input(inp, day)
inp = read_input(day)


# ## 5.1

# ```
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# ```

# In[52]:


test_inp = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


# In[53]:


def split_line(line: str):
    row_b, col_b = line[:-3], line[-3:]
    return row_b, col_b


# In[54]:


def map_to_bin(s, map_0="L", map_1="R"):
    remapped = s.replace(map_0, "0").replace(map_1, "1")
    return int(remapped, 2)


# In[55]:


def calc_seat_num(line):
    row_b, col_b = split_line(line)
    row, col = map_to_bin(row_b, "F", "B"), map_to_bin(col_b)
    return row * 8 + col


# In[56]:


def aoc_5_1(inp=inp):
    return max(calc_seat_num(line) for line in inp.splitlines())


# In[57]:


aoc_5_1()


# ## 5.2

# In[58]:


def all_seats(inp):
    return (calc_seat_num(line) for line in inp.splitlines())


# In[59]:


def aoc_5_2(inp=inp):
    seat_list = list(all_seats(inp))
    min_seat, max_seat = min(seat_list), max(seat_list)
    my_seat = [seat for seat in range(min_seat, max_seat + 1) if seat not in seat_list][0]
    return my_seat


# In[60]:


aoc_5_2()


# # 6

# In[61]:


day = 6
#put_away_input(inp, day)
inp = read_input(day)


# ## 6.1

# In[62]:


from string import ascii_lowercase as letters


# In[63]:


letters


# In[64]:


def split_inp(inp=inp):
    yield from inp.split("\n\n")


# In[65]:


def aoc_6_1(inp=inp):
    return sum(ltr in grp 
               for ltr in letters
               for grp in split_inp(inp))


# In[66]:


aoc_6_1()


# ## 6.2

# In[67]:


def split_group(grp):
    return grp.splitlines()


# In[68]:


def calc_group(grp):
    return sum(all([letter in person for person in split_group(grp)]) 
               for letter in letters)


# In[69]:


def aoc_6_2(inp=inp):
    return sum(calc_group(grp) for grp in split_inp(inp))


# In[70]:


aoc_6_2()


# # 7

# In[71]:


day = 7
# put_away_input(inp, day)
inp = read_input(day)


# ## 7.1

# In[72]:


test_inp_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


# In[73]:


import re


# In[74]:


COL = "shiny gold"


# In[75]:


def parse_inside_bags(inside_bags):
    inside_bag_tuples = re.findall(r"(\d+) (.+?) bag", inside_bags)
    return {color: int(n) for n, color in inside_bag_tuples}


# In[76]:


def parse_line(line: str):
    """in: line (str),
    out: outside bag (str), potential inside bags (dict {str: int})"""
    outside_bag, inside_bags = line.split(" bags contain ")
    inside_dict = parse_inside_bags(inside_bags)
    return outside_bag, inside_dict


# In[77]:


def parse_all_lines(inp, verbose=False):
    all_lines = [parse_line(line) for line in inp.splitlines()]
    outside, inside = zip(*all_lines)
    colors = set(color for color in outside)
    for inside_dict in inside:
        colors |= set([color for color in inside_dict])
    if verbose: print(f"Found {len(colors)} unique colors.")
    return colors, outside, inside


# In[78]:


def create_parent_dict(colors, outside, inside):
    parent_dict = {color: set() for color in colors}
    for out_col, in_cols in zip(outside, inside):
        for in_col in in_cols:
            parent_dict[in_col].add(out_col)
    return parent_dict


# In[79]:


def aoc_7_1(inp=inp):
    global COL
    parent_dict = create_parent_dict(*parse_all_lines(inp))
    can_be_inside = set(parent_dict[COL])
    print(f"{COL} can be directly in {can_be_inside}...")
    checked = set()
    while can_be_inside:
        to_check = can_be_inside.pop()
        if to_check in checked:
            continue
        can_be_inside |= set(parent_dict[to_check])
        checked.add(to_check)
    print(f"... and indirectly in {len(checked)} bag styles.")
    return len(checked)


# In[80]:


aoc_7_1(test_inp_1)


# In[81]:


aoc_7_1()


# ## 7.2

# In[82]:


test_inp_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


# In[83]:


def aoc_7_2(inp=inp, verbose=False):
    global COL
    colors, outside, inside = parse_all_lines(inp)
    out_in = dict(zip(outside, inside))
    
    def get_number(color, num, out_in=out_in, verbose=False):
        contents = out_in.get(color)
        if verbose: print(f"We have {num} {color} bags.")
        if contents:
            if verbose: print(f"{color:20} is in out_in, it's contents are:\n{contents}.")
            bags_inside = num + sum([num * get_number(inside_col, inside_num) 
                                     for inside_col, inside_num in contents.items()])
            if verbose: print(f"# bags inside {color}: {bags_inside}.")
            return bags_inside
        if verbose: print(f"Empty.")
        return num
    
    return get_number(COL, 1) - 1  # subtract shiny gold bag itself


# In[84]:


assert aoc_7_2(test_inp_1) == 32


# In[85]:


assert aoc_7_2(test_inp_2) == 126


# In[86]:


aoc_7_2()


# # 8

# In[87]:


day = 8
# put_away_input(inp, day)
inp = read_input(day)


# ## 8.1

# In[88]:


test_inp = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


# In[89]:


def split_instruction(inst):
    op = inst[:3]
    val = int(inst.split(" ")[-1])
    return op, val


# In[90]:


def read_code(inp):
    return tuple(split_instruction(inst)
                 for inst in inp.splitlines())


# In[91]:


def aoc_8_1(inp=inp, verbose=False):

    code = read_code(inp)
    visited = set()
    acc, idx = 0, 0

    while True:
        if idx in visited:
            return acc
        visited.add(idx)
        op, val = code[idx]
        acc += val if op == "acc" else 0
        idx += val if op == "jmp" else 1
        if verbose:
            print(f"[{op:} {val:2}] - accumulator now at {acc}, jumping to idx {idx}.")


# In[92]:


aoc_8_1(test_inp, verbose=True)


# In[93]:


assert aoc_8_1(test_inp) == 5


# In[94]:


aoc_8_1()


# ## 8.2

# In[95]:


def split_instruction(inst, immutable=True):
    op = inst[:3]
    val = int(inst.split(" ")[-1])
    iter_func = tuple if immutable else list
    return iter_func((op, val))


# In[96]:


def read_code(inp, immutable=True):
    iter_func = tuple if immutable else list
    return iter_func(split_instruction(inst, immutable)
                     for inst in inp.splitlines())


# In[97]:


def is_finite(code):

    visited = set()
    acc, idx = 0, 0

    while True:
        if idx in visited:
            return False, acc
        if idx >= len(code):
            return True, acc
        visited.add(idx)
        op, val = code[idx]
        acc += val if op == "acc" else 0
        idx += val if op == "jmp" else 1


# In[98]:


from copy import deepcopy


# In[99]:


def aoc_8_2(inp=inp):

    og_code = read_code(inp, immutable=False)
    for idx, (op, val) in enumerate(og_code):
        if op == "acc":
            continue
        new_code = deepcopy(og_code)
        new_code[idx][0] = "jmp" if op == "nop" else "nop"
        finite, acc = is_finite(new_code)
        if finite:
            return acc


# In[100]:


aoc_8_2(test_inp)


# In[101]:


aoc_8_2()


# # 9

# In[102]:


day = 9
# put_away_input(inp, day)
inp = read_input(day)


# ## 9.1

# In[103]:


test_inp = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


# In[104]:


import itertools as it


# In[105]:


def is_valid(n, previous_nums):
    for nums in it.permutations(previous_nums, 2):
        if sum(nums) == n:
            return True
    return False


# In[106]:


def aoc_9_1(inp=inp, preamble_len=25, verbose=False):
    nums = tuple(int(n) for n in inp.splitlines())
    if verbose:
        print(nums)
    for idx, n in enumerate(nums[preamble_len:]):
        previous_nums = nums[idx : idx + preamble_len]
        if verbose:
            print(f"n={n}. Checking from idx {idx} to idx {idx + preamble_len}: {previous_nums}.")
        if not is_valid(n, previous_nums):
            return n


# In[107]:


aoc_9_1(test_inp, 5, verbose=True)


# In[108]:


aoc_9_1()


# ## 9.2

# In[109]:


NUM = aoc_9_1()


# In[110]:


TEST_NUM = aoc_9_1(test_inp, 5)


# In[111]:


def find_contiguous_nums(nums, invalid_num, verbose=False):
    for start_idx, _ in enumerate(nums):
        iter_nums = iter(nums[start_idx:])
        cont_nums = []
        try:
            while sum(cont_nums) < invalid_num:
                cont_nums.append(next(iter_nums))
                if verbose:
                    print(cont_nums, sum(cont_nums))
                if sum(cont_nums) == invalid_num:
                    return cont_nums
        except StopIteration:
            continue
    return None


# In[112]:


def aoc_9_2(inp=inp, invalid_num=NUM, verbose=False):
    nums = tuple(int(n) for n in inp.splitlines())
    contiguous_nums = find_contiguous_nums(nums, invalid_num, verbose)
    return min(contiguous_nums) + max(contiguous_nums)


# In[113]:


aoc_9_2(test_inp, TEST_NUM, True)


# In[114]:


aoc_9_2()


# # 10

# In[10]:


day = 10
# put_away_input(inp, day)
inp = read_input(day)


# ## 10.1

# In[116]:


test_inp_1 = """16
10
15
5
1
11
7
19
6
12
4"""


# In[117]:


test_inp_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


# In[118]:


def get_adapters(inp):
    return sorted([int(a) for a in inp.splitlines()])


# In[119]:


def extend_adapters(adp):
    return [0] + adp + [adp[-1] + 3]


# In[120]:


def get_diffs(adp, diff=1):
    ext = extend_adapters(adp)
    return sum(1 for idx, a1 in enumerate(ext[:-1])
               if ext[idx+1] - a1 == diff)


# In[121]:


def aoc_10_1(inp=inp):
    adp = get_adapters(inp)
    return get_diffs(adp, 1) * get_diffs(adp, 3)


# In[122]:


aoc_10_1()


# ## 10.2

# In[123]:


TEST_SOL_1, TEST_SOL_2 = 8, 19_208


# In[124]:


from functools import lru_cache


# In[125]:


from typing import *


# In[126]:


@lru_cache(200)
def paths_to_n(n: int, chain: Tuple[int]) -> int:
    """Note: Chain must be immutable to be cached, so pass a tuple!
    Will return 0 for any n < 0 (even if it were in chain)."""
    if n not in chain:
        return 0
    if n == 0 or n == 1: # and n in chain (implicit)
        return 1
    if n == 2: # and n in chain
        return 2 if 1 in chain else 1
    return (  paths_to_n(n-3, chain)
            + paths_to_n(n-2, chain)
            + paths_to_n(n-1, chain))


# In[127]:


def aoc_10_2(inp=inp):
    chain = extend_adapters(get_adapters(inp))
    return paths_to_n(max(chain), tuple(chain))


# In[128]:


assert aoc_10_2(test_inp_1) == TEST_SOL_1


# In[129]:


assert aoc_10_2(test_inp_2) == TEST_SOL_2


# In[130]:


aoc_10_2()


# # 11

# In[8]:


day = 11
# put_away_input(inp, day)
inp = read_input(day)


# ## 11.1

# In[134]:


TEST_INP = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


# In[135]:


TEST_SOL = 37


# In[137]:


import numpy as np


# In[422]:


from typing import *


# In[439]:


def transform_and_pad(inp: str) -> np.array:
    mapping = {"L": -1, ".": 0, "#": 1}
    arr = [[mapping[k] for k in row]
           for row in inp.splitlines()]
    return np.pad(arr, 1)


# In[298]:


def check_one_element(pa: np.array, r: int, c: int) -> int:
    """Element-wise, quite inefficient. But not sure how to implement
    these rules vectorized.
    """
    el = pa[r, c].item()
    if el == 0:
        return 0
    slice_ = pa[r - 1 : r + 2, c - 1 : c + 2]
    if el == -1 and (slice_ < 1).all():
        return 1
    if el == 1 and (slice_ > 0).sum() > 4:  # > 4 b/c el is included in slice_
        return -1
    return el


# In[306]:


def loop_over_array_without_padding(nrows, ncols) -> Iterator:
    for r in range(1, nrows - 1):
        for c in range(1, ncols - 1):
            yield (r, c)


# In[307]:


def check_matrix(pa: np.array) -> np.array:
    pa_manipulated = pa.copy()
    for r, c in loop_over_array_without_padding(*pa.shape):
        pa_manipulated[r, c] = check_one_element(pa, r, c)
    return pa_manipulated


# In[302]:


def do_one_iteration(pa_og: np.array) -> Tuple[np.array, bool]:
    pa_manipulated = check_matrix(pa_og)
    return pa_manipulated, (pa_manipulated == pa_og).all()


# In[303]:


def aoc_11_1(inp=inp):
    padded_arr = transform_and_pad(inp)
    stable = False
    while not stable:
        padded_arr, stable = do_one_iteration(padded_arr)
    return (padded_arr > 0).sum()


# In[304]:


assert aoc_11_1(TEST_INP) == TEST_SOL


# In[441]:


get_ipython().run_line_magic('time', 'aoc_11_1()  # slow')


# ## 11.2

# - no need to pad (but can keep it padded b/c not looping over padding an 0s are neutral anyway)
# - replace `slice_` with `visible_` (can be a flat array/list), replace 4 by 5, done.
# - visible:
#     - 8 lines of vision
#     - first non-zero element counts --> lazy evaluation

# In[423]:


TEST_SOL_2 = 26


# In[424]:


def evaluate_line_of_vision(a, r, c, delta_r, delta_c) -> int:
    nrows, ncols = a.shape
    seat = 0
    while not seat:
        r += delta_r
        c += delta_c
        if not (0 < r < nrows - 1 and 0 < c < ncols - 1):
            return 0
        seat = a[r, c]
    return seat


# In[425]:


def seat_can_see(a, r, c):
    return np.array([evaluate_line_of_vision(a, r, c, delta_r, delta_c)
                     for delta_r, delta_c in range_over_lines_of_vision()])


# In[426]:


def range_over_lines_of_vision():
    directions = (-1, 0, 1)
    for delta_r in directions:
        for delta_c in directions:
            if not delta_r == delta_c == 0:
                yield delta_r, delta_c


# In[427]:


def check_one_element_2(pa: np.array, r: int, c: int) -> int:
    """Element-wise, quite inefficient. But not sure how to implement
    these rules vectorized.
    """
    el = pa[r, c].item()
    if el == 0:
        return 0
    seen_seats = seat_can_see(pa, r, c)
    if el == -1 and (seen_seats < 1).all():
        return 1
    if el == 1 and (seen_seats > 0).sum() > 4:  # > 4 b/c el is not included in seen_seats
        return -1
    return el


# In[428]:


def check_matrix_2(pa: np.array) -> np.array:
    pa_manipulated = pa.copy()
    for r, c in loop_over_array_without_padding(*pa.shape):
        pa_manipulated[r, c] = check_one_element_2(pa, r, c)
    return pa_manipulated


# In[429]:


def do_one_iteration_2(pa_og: np.array) -> Tuple[np.array, bool]:
    pa_manipulated = check_matrix_2(pa_og)
    return pa_manipulated, (pa_manipulated == pa_og).all()


# In[430]:


def aoc_11_2(inp=inp):
    padded_arr = transform_and_pad(inp)
    stable = False
    while not stable:
        padded_arr, stable = do_one_iteration_2(padded_arr)
    return (padded_arr > 0).sum()


# In[431]:


assert aoc_11_2(TEST_INP) == TEST_SOL_2


# In[440]:


get_ipython().run_line_magic('time', 'aoc_11_2()  # slow')


# ## simplify & unify 10.1 & 10.2

# - keep strings, don't convert to array
# - use a `Counter`
# - refactor functions to work for both parts

# In[442]:


from collections import Counter


# In[445]:


Grid = List[List[str]]


# In[504]:


def process_seat(grid: Grid, r: int, c: int, part: int) -> int:
    """Element-wise, quite inefficient. But not sure how to implement
    these rules vectorized.
    """
    assert part in (1, 2), f"Only parts 1 and 2 available, you passed part {part}."
    
    nrows, ncols = len(grid), len(grid[0])
    
    def direct_neighbor(grid, r, c, dr, dc):
        return grid[r + dr][c + dc]
    
    def next_in_lov(grid, r, c, dr, dc):
        s = "."
        while s not in ("#", "L"):
            r += dr
            c += dc
            if not (0 <= r < nrows and 0 <= c < ncols):
                return "."
            s = grid[r][c]
        return s
    
    neighbor_func = next_in_lov if part == 2 else direct_neighbor
    threshold = 5 if part == 2 else 4
    
    seat = grid[r][c]
    
    if seat == ".":
        return seat
    
    counts = Counter(neighbor_func(grid, r, c, dr, dc)
                     for dr, dc in range_over_lines_of_vision()
                     if 0 <= r + dr < nrows and 0 <= c + dc < ncols)
    
    if seat == "L" and counts["#"] == 0:
        return "#"
    if seat == "#" and counts["#"] >= threshold:
        return "L"
    return seat


# In[505]:


def do_one_iteration(grid: Grid, part: int) -> Tuple[Grid, bool]:
    manipulated_grid = [[process_seat(grid, ri, ci, part)
                         for ci, _ in enumerate(row)]
                         for ri, row in enumerate(grid)]
    return manipulated_grid, manipulated_grid == grid


# In[506]:


def aoc_11(inp=inp, part=1):
    grid = [[seat for seat in row] for row in inp.splitlines()]
    stable = False
    while not stable:
        grid, stable = do_one_iteration(grid, part)
    return sum(row.count("#") for row in grid)


# In[509]:


assert aoc_11(TEST_INP, part=1) == TEST_SOL


# In[511]:


assert aoc_11(TEST_INP, part=2) == TEST_SOL_2


# In[512]:


get_ipython().run_line_magic('time', 'aoc_11(part=1)  # still slow')


# In[513]:


get_ipython().run_line_magic('time', 'aoc_11(part=2)  # still slow')


# # 12

# In[120]:


day = 12
# put_away_input(inp, day)
inp = read_input(day)


# ## 12.1

# In[16]:


from typing import *


# In[35]:


import itertools as it


# In[13]:


DIRS = ("N", "E", "S", "W")


# In[32]:


DEGS = (90, 180, 270)


# In[33]:


SIDES = ("R", "L")


# In[97]:


DIR_MAPPING = dict(zip(DIRS,((-1, 0), (0, 1), (1, 0), (0, -1))))


# In[98]:


DIR_MAPPING


# In[81]:


START_POS = 0, 0, "E"


# In[19]:


# x: N is -, S is +
# y: W is -, E is +
# z: N is 0, E is 1, S is 2, W is 3


# In[14]:


TEST_INP = """F10
N3
F7
R90
F11
"""


# In[234]:


from typing import Tuple


# In[235]:


Position = Tuple[int, int, str]  # NS, WE, orientation


# In[236]:


# def move(act: str, num: int, curr_pos: Tuple[int, int, str]) -> Tuple[int, int, str]:
def move(act: str, num: int, curr_pos: Position) -> Position:
    assert act in DIRS
    x, y, z = curr_pos
    if act == "N":
        x -= num
    elif act == "S":
        x += num
    elif act == "W":
        y -= num
    elif act == "E":
        y += num
    return x, y, z


# In[162]:


def change_dir(act: str, num: int, curr_pos: Position) -> Position:
    assert act in SIDES
    assert num in DEGS
    dir_ = 1 if act == "R" else -1
    x, y, z = curr_pos
    z_idx = DIRS.index(z)
    z_idx += dir_ * (num // 90)
    z = DIRS[z_idx % 4]
    return x, y, z


# In[163]:


def forward(act: str, num: int, curr_pos: Position) -> Position:
    assert act == "F"
    x, y, z = curr_pos
    dx, dy = DIR_MAPPING[z]
    x += dx * num
    y += dy * num
    return x, y, z


# In[174]:


def next_position(instr: str, curr_pos: Position) -> Position:
    action, num = instr[:1], int(instr[1:])
    if action in DIRS:
        return move(action, num, curr_pos)
    elif action in SIDES:
        return change_dir(action, num, curr_pos)
    elif action == "F":
        return forward(action, num, curr_pos)


# In[165]:


def aoc_12_1(inp=inp):
    pos = START_POS
    for instr in inp.splitlines():
        pos = next_position(instr, pos)
    x, y, z = pos
    return abs(x) + abs(y)


# In[166]:


assert aoc_12_1(TEST_INP) == 25


# In[167]:


aoc_12_1()


# ## 12.2

# In[176]:


START_WAYPOINT = (-1, 10)


# In[170]:


Coords = Tuple[int, int]


# In[184]:


def move_wp(act: str, num: int, ship: Coords, wp: Coords) -> Coords:
    assert act in DIRS
    wp_ns, wp_we = wp
    if act == "N":
        wp_ns -= num
    elif act == "S":
        wp_ns += num
    elif act == "W":
        wp_we -= num
    elif act == "E":
        wp_we += num
    return ship, (wp_ns, wp_we)


# In[223]:


def rotate_wp(act: str, num: int, ship: Coords, wp: Coords) -> Coords:
    assert act in SIDES
    assert num in DEGS
    wp_ns, wp_we = wp
    dir_ = 1 if act == "R" else -1
    if num == 90:
        wp_ns, wp_we = dir_ * wp_we, dir_ * wp_ns * (-1)
    elif num == 180:
        wp_ns *= -1
        wp_we *= -1
    elif num == 270:
        wp_ns, wp_we = dir_ * wp_we * (-1), dir_ * wp_ns
    return ship, (wp_ns, wp_we)


# In[224]:


def towards_wp(act: str, num: int, ship: Coords, wp: Coords) -> Coords:
    assert act == "F"
    wp_ns, wp_we = wp
    sh_ns, sh_we = ship
    sh_ns += num * wp_ns
    sh_we += num * wp_we
    return (sh_ns, sh_we), (wp_ns, wp_we)


# In[225]:


def next_position_wp(instr: str, ship: Coords, wp: Coords) -> Coords:
    action, num = instr[:1], int(instr[1:])
    if action in DIRS:
        return move_wp(action, num, ship, wp)
    elif action in SIDES:
        return rotate_wp(action, num, ship, wp)
    elif action == "F":
        return towards_wp(action, num, ship, wp)
    raise


# In[229]:


def aoc_12_2(inp=inp):
    ship, wp = START_POS[:2], START_WAYPOINT
    for instr in inp.splitlines():
        ship, wp = next_position_wp(instr, ship, wp)
    x, y = ship
    return abs(x) + abs(y)


# In[230]:


assert aoc_12_2(TEST_INP) == 286


# In[231]:


aoc_12_2()


# # 13

# In[519]:


day = 13
#put_away_input(inp, day)
inp = read_input(day)


# ## 13.1

# In[520]:


from typing import *


# In[521]:


TEST_INP = """939
7,13,x,x,59,x,31,19"""


# In[522]:


def parse_input(inp: str) -> Tuple[int, Tuple[int]]:
    time, buses = inp.splitlines()
    time = int(time)
    buses = tuple(int(bus) for bus in buses.split(",") if bus != "x")
    return time, buses


# In[523]:


time, buses = parse_input(TEST_INP)


# In[524]:


time, buses


# In[525]:


def find_next_bus(time: int, buses: Tuple[int]) -> Tuple[int, int]:
    bustimes = {bus: (time // bus + 1) * bus for bus in buses}
    next_bus = min(bustimes, key=bustimes.get)
    return next_bus, bustimes[next_bus]


# In[526]:


def aoc_13_1(inp=inp):
    time, buses = parse_input(inp)
    next_bus, next_time = find_next_bus(time, buses)
    return next_bus * (next_time - time)


# In[527]:


aoc_13_1(TEST_INP)


# In[528]:


aoc_13_1()


# ## 13.2

# Works, but slow and inefficient:

# In[533]:


# Buses = Tuple[Tuple[int, int]]


# def parse_input_2(inp: str) -> Buses:
#     _, buses = inp.splitlines()
#     return tuple((timestamp, int(bus)) for timestamp, bus in enumerate(buses.split(",")) if bus != "x")


# def it_works(buses: Buses, t: int) -> bool:
#     return all((t + dt) % bus == 0 for dt, bus in buses)


# def yield_candidates(buses: Buses) -> Iterator[int]:
#     large_to_small = sorted(buses, key=lambda x: x[1])[::-1]
#     d_0, bus_0 = large_to_small[0]
#     i = 0
#     while True:
#         t = i * bus_0 - d_0
#         if it_works(buses=large_to_small[1:], t=t):
#             yield t
#         i += 1


# def aoc_13_2(inp=inp):
#     buses = parse_input_2(inp)
#     return next(yield_candidates(buses))


# In[724]:


from functools import reduce


# In[725]:


def parse_input_2(inp: str) -> Tuple[int, int]:
    _, buses = inp.splitlines()
    deltas, buses =  zip(*tuple((timestamp, int(bus)) for timestamp, bus in enumerate(buses.split(",")) if bus != "x"))
    modulos = tuple(b-d if d else 0 for d, b in zip(deltas, buses))
    return modulos, buses


# Next two cells from [rosettacode](https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6):

# In[726]:


def chinese_remainder(modulos, buses):
    sum = 0
    bus_product = reduce(lambda a, b: a * b, buses)
    for m_i, b_i in zip(modulos, buses):
        p = bus_product // b_i
        sum += m_i * mul_inv(p, b_i) * p
    return sum % bus_product


# In[727]:


def mul_inv(p, b):
    if b == 1:
        return 1
    b0 = b
    x0, x1 = 0, 1
    while p > 1:
        q = p // b
        p, b = b, p % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# In[728]:


def aoc_13_2(inp=inp):
    modulos, buses = parse_input_2(inp)
    return chinese_remainder(modulos, buses)


# In[730]:


get_ipython().run_line_magic('timeit', 'aoc_13_2(TEST_INP)')


# In[732]:


assert aoc_13_2(TEST_INP) == 1068781


# In[733]:


aoc_13_2()


# # 14

# In[740]:


day = 14
# put_away_input(inp, day)
inp = read_input(day)


# In[741]:


TEST_INP = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


# ## 14.1

# In[742]:


import re


# In[874]:


Mask = Tuple[int, int]


# In[895]:


def parse_mask(m: str) -> Mask:
    """Find the ints that we can use to manipulate bits
    using bitwise 'and' to set bit to zero: n & zi
    or bitwies 'or' to set a bit to one: n | oi.
    """
    zm = m.replace("X", "1")
    om = m.replace("X", "0")
    zi, oi = int(zm, 2), int(om, 2)
    return zi, oi


# In[896]:


def parse_inp(inp: str) -> Iterator[Tuple[Mask, int, int]]:
    """Two modes: mask mode yields (mask, None, None),
    memory mode yields (None, pos, num).
    """
    for line in inp.splitlines():
        inst, val = line.split(" = ")
        is_mask = line.startswith("mask")
        mask = parse_mask(val) if is_mask else None
        pos = None if is_mask else int(re.findall(r"\[(\d+)\]", inst)[0])
        num = None if is_mask else int(val)
        yield (mask, pos, num)


# In[897]:


def apply_bitmask(mask: Mask, n: int) -> int:
    """Change the zero-bits, then change the one-bits."""
    zi, oi = mask
    return n & zi | oi


# In[891]:


def aoc_14_1(inp: str = inp) -> int:
    mem = {}
    current_mask = None
    for mask, pos, num in parse_inp(inp):
        if mask is not None:
            current_mask = mask
            continue
        mem[pos] = apply_bitmask(current_mask, num)
    return sum(mem.values())


# In[893]:


assert aoc_14_1(TEST_INP) == 165


# In[894]:


aoc_14_1()


# ## 14.2

# In[1001]:


TEST_INP2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


# In[935]:


import itertools as it


# In[974]:


Mask2 = Tuple[Tuple[int], int]


# In[1185]:


def parse_mask2(m: str) -> Mask2:
    om = m.replace("X", "0")
    oi = int(om, 2)
    xs = tuple(len(m) - idx - 1 for idx, val in enumerate(m) if val == "X")
    return xs, oi


# In[1186]:


def parse_inp2(inp: str) -> Iterator[Mask2, int, int]:
    """Two modes: mask mode yields (mask, None, None),
    memory mode yields (None, pos, num).
    """
    for line in inp.splitlines():
        inst, val = line.split(" = ")
        is_mask = line.startswith("mask")
        mask = parse_mask2(val) if is_mask else None
        pos = None if is_mask else int(re.findall(r"\[(\d+)\]", inst)[0])
        num = None if is_mask else int(val)
        yield (mask, pos, num)


# In[1114]:


def set_bit(value: int, bit: int) -> int:
    return value | (1 << bit)


# In[1115]:


def clear_bit(value: int, bit: int) -> int:
    return value & ~(1 << bit)


# In[1179]:


def apply_floats(xs: Tuple[int], n: int) -> Iterator[int]:
    floats_can_be = tuple((0, 1) for _ in xs)
    for combination in it.product(*floats_can_be):
        for bit, value in zip(xs, combination):
            n = set_bit(n, bit) if value == 1 else clear_bit(n, bit)
        yield n


# In[1180]:


def apply_bitmask2(mask: Mask2, n: int) -> Iterator[int]:
    """Change the one-bits, then all combinations of floating bits."""
    xs, oi = mask
    return apply_floats(xs, n | oi)


# In[1181]:


def aoc_14_2(inp: str = inp) -> int:
    mem = {}
    current_mask = None
    for mask, pos, num in parse_inp2(inp):
        if mask is not None:
            current_mask = mask
            continue
        positions = apply_bitmask2(current_mask, pos)
        for p in positions:
            mem[p] = num
    return sum(mem.values())


# In[1182]:


assert aoc_14_2(TEST_INP2) == 208


# In[1184]:


aoc_14_2()


# # 15

# In[1206]:


inp = """0,3,1,6,7,5"""


# In[1207]:


day = 15
# put_away_input(inp, day)
inp = read_input(day)


# In[1192]:


EXAMPLES = """
    Given the starting numbers 1,3,2, the 2020th number spoken is 1.
    Given the starting numbers 2,1,3, the 2020th number spoken is 10.
    Given the starting numbers 1,2,3, the 2020th number spoken is 27.
    Given the starting numbers 2,3,1, the 2020th number spoken is 78.
    Given the starting numbers 3,2,1, the 2020th number spoken is 438.
    Given the starting numbers 3,1,2, the 2020th number spoken is 1836.
"""


# ## 15.1

# In[1193]:


import re


# In[1226]:


from collections import defaultdict


# In[1214]:


def parse_input(inp):
    return tuple(int(x) for x in inp.split(","))


# In[1263]:


def spoken(starting_nums):
    
    def register(num, last_spoken, turn):
        last_spoken[num].append(turn)
        turn += 1
        return num, last_spoken, turn
    
    last_spoken = defaultdict(list)
    turn = 1
    
    for num in starting_nums:
        last_num, last_spoken, turn = register(num, last_spoken, turn)
        yield num
        
    while True:
        occurences = last_spoken[last_num]
        if not occurences:
            num = last_num
            last_num, last_spoken, turn = register(num, last_spoken, turn)
            yield num
        else:
            num = occurences[-1] - occurences[-2] if len(occurences) > 1 else 0
            last_num, last_spoken, turn = register(num, last_spoken, turn)
            yield num


# In[1221]:


def yield_examples():
    starting_nums = tuple(parse_input(x) for x in re.findall(r"starting numbers (.+), the 2020th", EXAMPLES))
    solutions = tuple(int(z) for z in re.findall(r"spoken is (\d+).", EXAMPLES))
    yield from zip(starting_nums, solutions)


# In[1285]:


for starting_nums, solution in yield_examples():
    speak_numbers = spoken(starting_nums)
    [next(speak_numbers) for _ in range(2019)]
    assert next(speak_numbers) == solution


# In[1283]:


def aoc_15_1(inp=inp):
    pi = parse_input(inp)
    speak_numbers = spoken(pi)
    [next(speak_numbers) for _ in range(2019)]
    return next(speak_numbers)


# In[1284]:


aoc_15_1()


# ## 15.2

# In[1290]:


from functools import partial


# In[1286]:


def aoc_15(part, inp=inp):
    n = 2020 if part == 1 else 30_000_000
    pi = parse_input(inp)
    speak_numbers = spoken(pi)
    [next(speak_numbers) for _ in range(n-1)]
    return next(speak_numbers)


# In[1288]:


aoc_15_2 = partial(aoc_15, part=2)


# In[1289]:


aoc_15_2()


# # 16

# In[3]:


day = 16
# put_away_input(inp, day)
inp = read_input(day)


# In[4]:


TEST_INP = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


# ## 16.1

# In[5]:


get_ipython().system(' pip install dataclasses')


# In[6]:


import itertools as it
import re
from dataclasses import dataclass
from typing import *


# In[7]:


@dataclass
class Rule:
    name: str
    bounds: Tuple[int]
        
    def __repr__(self):
        lolo, lohi, hilo, hihi = self.bounds
        return f"{self.name:30}: {lolo:>3} <= n <= {lohi:<3} or {hilo:>3} <= n <= {hihi:<3}"
    
    def check(self, n):
        lolo, lohi, hilo, hihi = self.bounds
        return lolo <= n <= lohi or hilo <= n <= hihi


# In[8]:


def parse_input(inp):
    rules, my_ticket, other_tickets = inp.split("\n\n")
    
    def extract_rule(line):
        name = line.split(": ")[0] 
        bounds = tuple(int(n) for n in re.findall(r"\d+", line))    
        return Rule(name, bounds)
    
    rules = tuple(extract_rule(l) for l in rules.splitlines())  # name: rule_func
    my_ticket = tuple(int(x) for x in my_ticket.splitlines()[-1].split(","))
    other_tickets = tuple(tuple(int(x) for x in ticket.split(","))
                          for ticket in other_tickets.splitlines()[1:])
    return rules, my_ticket, other_tickets


# In[9]:


def aoc_16_1(inp=inp):
    rules, _, other_tickets = parse_input(inp)
    fail_all_rules = tuple(n for n in it.chain(*other_tickets)
                           if not any(rule.check(n) for rule in rules))
    return sum(fail_all_rules)


# In[10]:


assert aoc_16_1(TEST_INP) == 71


# In[11]:


aoc_16_1()


# ## 16.2

# In[31]:


TEST_INP2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


# In[122]:


from functools import reduce


# In[36]:


def check_ticket(ticket, rules):
    return all(any(rule.check(n) for rule in rules) for n in ticket)


# In[79]:


def sort_rules(rules: Tuple[Rule], valid_tickets: Tuple[Tuple[int]], verbose: bool = False) -> Tuple[Rule]:
    rule_dict = {rule.name: rule for rule in rules}
    sorted_rules = {idx: None for idx, _ in enumerate(rules)}
    while rule_dict:
        for idx, nums in enumerate(zip(*valid_tickets)):
            if sorted_rules[idx] is not None:
                continue
            matches = [rule for rule in rule_dict.values() if all(rule.check(n) for n in nums)]
            if len(matches) == 1:
                sorted_rules[idx] = rule_dict.pop(matches[0].name)
                if verbose:
                    print(f"Found rule {sorted_rules[idx].name} for idx {idx}.")
    return sorted_rules


# In[126]:


def product(iterable):
    return reduce(lambda a, b: a * b, iterable, 1)


# In[131]:


def aoc_16_2(inp=inp):
    rules, my_ticket, other_tickets = parse_input(inp)
    assert check_ticket(my_ticket, rules), "My ticket is not valid!"
    valid_other_tickets = tuple(ticket for ticket in other_tickets
                                if check_ticket(ticket, rules))
    sorted_rules = sort_rules(rules, valid_other_tickets, verbose=True)
    dep_values = (my_ticket[idx]
                  for idx, rule in sorted_rules.items()
                  if rule.name.startswith("departure"))
    return product(dep_values)


# In[132]:


aoc_16_2()


# # 17

# In[7]:


inp = """...#...#
..##.#.#
###..#..
........
...##.#.
.#.####.
...####.
..##...#
"""


# In[10]:


day = 17
# put_away_input(inp, day)
inp = read_input(day)


# In[11]:


TEST_INP = """.#.
..#
###"""


# ## 17.1

# In[12]:


import itertools as it


# In[13]:


from typing import *


# In[19]:


from collections import defaultdict


# In[20]:


Point = Tuple[int]


# In[21]:


Grid = DefaultDict[Point, bool]


# In[49]:


def parse_input(inp: str) -> Grid:
    # col_num, row_num = x, y
    # upper left = (0, 0, 0)  (arbitrary)
    input_points = defaultdict(bool)
    z = 0
    for y, line in enumerate(inp.splitlines()):
        for x, symbol in enumerate(line):
            input_points[(x, y, z)] = symbol == "#"
    return input_points


# In[55]:


def get_neighbors(point: Point) -> Tuple[Point]:
    dimensions = len(point)
    diffs = (-1, 0, 1)
    coord_options = tuple(tuple(c + d for d in diffs)
                          for c in point)
    neighbors = tuple(p for p in it.product(*coord_options)
                      if tuple(p) != point)
    expected = pow(3, dimensions) - 1
    assert len(neighbors) == expected, f"Found {len(neighbors)} neighbors, expected {expected}."
    return neighbors


# In[28]:


def count_active_neighbors(point: Point, grid: Grid) -> int:
    return sum(1 for neighbor in get_neighbors(point)
               if grid.get(neighbor))


# In[53]:


pow(3, 4)


# In[37]:


def extend_grid(grid: Grid) -> Tuple[Point]:
    """Returns a tuple of all Points within a grid plus 1 dimension in each direction."""
    min_dims, max_dims = tuple(map(min, zip(*grid))), tuple(map(max, zip(*grid)))
    return tuple(p for p in it.product(*tuple(tuple(range(mi - 1, ma + 2))
                                              for mi, ma in zip(min_dims, max_dims))))


# In[46]:


def step(grid: Grid) -> Grid:
    """
    If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    """
    new_grid = grid.copy()
    potential_cubes = extend_grid(grid)
    for cube in potential_cubes:
        status = grid[cube]
        n_active_neighbors = count_active_neighbors(cube, grid)
        if not (status is True and n_active_neighbors in (2, 3)):
            new_grid[cube] = False
        if status is False and n_active_neighbors == 3:
            new_grid[cube] = True
    return new_grid


# In[41]:


def aoc_17_1(inp: str = inp, verbose: bool = False) -> int:
    grid = parse_input(inp)
    for r in range(6):
        if verbose:
            print(f"Before round {r + 1}: {grid}.")
        grid = step(grid)
    return sum(1 for cube in grid if grid.get(cube))


# In[44]:


assert aoc_17_1(TEST_INP) == 112


# In[45]:


aoc_17_1()


# ## 17.2

# __Basically the same solution as 17.1:__
# - `Point` and `Grid` still work in 4D
# - so do `get_neighbors` (just make the assert depend on the dimensions), `count_active_neighbors` and `extend_grid`
# - only adjustment: during parsing, add dimension w with value 0

# In[48]:


def parse_input_2(inp: str) -> Grid:
    # col_num, row_num = x, y
    # upper left = (0, 0, 0, 0)  (arbitrary)
    input_points = defaultdict(bool)
    z = w = 0
    for y, line in enumerate(inp.splitlines()):
        for x, symbol in enumerate(line):
            input_points[(x, y, z, w)] = symbol == "#"
    return input_points


# In[56]:


def aoc_17_2(inp: str = inp, verbose: bool = False) -> int:
    grid = parse_input_2(inp)
    for r in range(6):
        if verbose:
            print(f"Before round {r + 1}: {grid}.")
        grid = step(grid)
    return sum(1 for cube in grid if grid.get(cube))


# In[57]:


assert aoc_17_2(TEST_INP) == 848


# In[58]:


aoc_17_2()


# # 18

# In[5]:


TEST_INP = """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""


# In[6]:


TEST_SOL = (71, 51, 26, 437, 12240, 13632)


# In[7]:


day = 18
# put_away_input(inp, day)
inp = read_input(day)


# In[8]:


from typing import *


# ## 18.1

# In[9]:


class Operator:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name
    
    def __call__(self, a, b):
        if self.name == "+":
            return a + b
        elif self.name == "*":
            return a * b
        else:
            raise


# In[10]:


def parse_line_without_par(line: str) -> Tuple[Iterator]:
    parts = line.split(" ")
    nums = (int(n) for n in parts[::2])
    ops = (Operator(o) for o in parts[1::2])
    return nums, ops


# In[11]:


def calculate_line(line: str, verbose: bool = False) -> int:
    while "(" in line or ")" in line:
        if verbose: print(line)
        line = solve_inside_parenthesis(line)
    if verbose: print(line)
    nums, ops = parse_line_without_par(line)
    result = next(ops)(next(nums), next(nums))
    for op in ops:
        result = op(result, next(nums))
    return result


# In[12]:


def solve_inside_parenthesis(line: str) -> str:
    for idx, v in enumerate(line):
        if v == "(":
            ls = idx
        elif v == ")":
            rs = idx
            inside = line[ls + 1 : rs]
            evaluated = calculate_line(inside)
            return line[:ls] + str(evaluated) + line[rs+1:]


# In[13]:


for line, sol in zip(TEST_INP.splitlines(), TEST_SOL):
    assert calculate_line(line) == sol


# In[14]:


def aoc_18_1(inp: str = inp, verbose: bool = False) -> int:
    return sum(calculate_line(line) for line in inp.splitlines())


# In[15]:


aoc_18_1()


# ## 18.2

# In[16]:


TEST_SOL_2 = (231, 51, 46, 1445, 669060, 23340)


# In[65]:


from functools import reduce


# In[66]:


def solve_inside_parenthesis_2(line: str) -> str:
    for idx, v in enumerate(line):
        if v == "(":
            ls = idx
        elif v == ")":
            rs = idx
            inside = line[ls + 1 : rs]
            evaluated = calculate_line_2(inside)
            return line[:ls] + str(evaluated) + line[rs+1:]


# In[67]:


def solve_addition(line: str) -> str:
    for idx, v in enumerate(line):
        if v == "+":
            try:
                elements = [el.replace("(", "").replace(")", "") for el in line.split(" ")]
                if "+" in elements:
                    plus_idx = elements.index("+")
                    left, right = (int(elements[plus_idx + offset]) for offset in (-1, 1))
                    return " ".join(elements[: plus_idx - 1] + [str(left + right)] + elements[plus_idx + 2:])
                else:
                    return str(left + right)
            except:
                import pdb; pdb.set_trace()
    return line


# In[68]:


def calculate_line_2(line: str, verbose: bool = False) -> int:
    while "(" in line or ")" in line:
        if verbose: print(line)
        line = solve_inside_parenthesis_2(line)
    while "+" in line:
        line = solve_addition(line)
    nums, _ = tuple(tuple(x) for x in parse_line_without_par(line))
    return reduce(lambda a, b: a * b, nums, 1)


# In[70]:


for line, sol in zip(TEST_INP.splitlines(), TEST_SOL_2):
    assert calculate_line_2(line) == sol


# In[71]:


def aoc_18_2(inp: str = inp, verbose: bool = False) -> int:
    return sum(calculate_line_2(line) for line in inp.splitlines())


# In[72]:


aoc_18_2()


# Ugly. :/

# In[ ]:





# In[ ]:




