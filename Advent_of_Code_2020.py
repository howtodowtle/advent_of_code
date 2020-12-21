#!/usr/bin/env python
# coding: utf-8

# # Setup

# In[1]:


get_ipython().system(' jupyter nbconvert --to python Advent_of_Code_2020.ipynb')


# In[2]:


get_ipython().system(' mkdir -p inputs')


# In[3]:


def put_away_input(inp, day):
    with open(f"inputs/inp_day_{day}.txt", "w") as f:
        f.write(inp)


# In[4]:


def read_input(day):
    with open(f"inputs/inp_day_{day}.txt", "r") as f:
        inp = f.read()
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


# # 5.1

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
#put_away_input(inp, day)
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


# In[81]:


aoc_7_1(test_inp_1)


# In[82]:


aoc_7_1()


# ## 7.2

# In[83]:


test_inp_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


# In[84]:


def aoc_7_2(inp=inp):
    global COL
    colors, outside, inside = parse_all_lines(inp)
    out_in = dict(zip(outside, inside))
    
    def get_number(color, num, verbose=False):
        contents = out_in.get(color)
        if verbose: print(f"We have {num} {color} bags.")
        if contents:
            if verbose: print(f"{color:20} is in out_in, it's contents are:\n{contents}.")
            bags_inside = num + sum([num * get_number(inside_col, inside_num) for inside_col, inside_num in contents.items()])
            if verbose: print(f"# bags inside {color}: {bags_inside}.")
            return bags_inside
        if verbose: print(f"Empty.")
        return num
    
    return get_number(COL, 1) - 1


# In[85]:


assert aoc_7_2(test_inp_1) == 32


# In[86]:


assert aoc_7_2(test_inp_2) == 126


# In[87]:


aoc_7_2(inp)


# In[ ]:




