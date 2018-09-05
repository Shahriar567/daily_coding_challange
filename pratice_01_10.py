import itertools as it

class Repeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


# repeater = Repeater('Hello', 3)
# iterator = iter(repeater)
# while True:
#     try:
#         item = next(iterator)
#     except StopIteration:
#         break
#     print(item)


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


# val = countdown(5)
# val
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))

data = [1, 2, 3, 4, 5]
data1 = [10, 20, 30, 40, 50]
data2 = []

for x , y in zip(data,data1):
    data2.append(x)
    data2.append(y)
    # print(f"it is the best {data2} and they corrosponf to {x}, {y}")

#*x, y = data
# print(x)


def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]


def better_grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(list(better_grouper(nums, 3)))


# Problem 5:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    return f(lambda a, b: a)

def cdr(f):
    return f(lambda x, y: y)


# print(cdr(cons(1,2)))


# Problem 4:



#Problem 6:

# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
# it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.


class node():
    def __init__(self, both = None, data=None):
        self.both = both
        self.data = data


# Problem 7



def problem7(msg):
    symbols = map(str, range(1,27))
    if not msg:
        return 1
    matches = filter(lambda symbol: msg.startswith(symbol), symbols)
    enc = [problem7(msg[len(m):]) for m in matches]
    return sum(enc)



# print(problem7("26261"))


# Problem 8

def problem8(btree):
    data, ln, rn = btree

    if ln is None and rn is None:
        return 1, True, data

    lcount, is_L, lval = problem8(ln)
    rcount, is_R, rval = problem8(rn)

    is_uval = is_L and is_R and data == lval and data == rval
    count = lcount + rcount + is_uval
    return count, is_uval, data

btree = (0, (0, (0, None, None), (0, (0, None, None), (0, None, None))), (1, None, None))

# print(problem8(btree)[0])


# Problem 9

def problem9(L):

    if not L:
        return 0

    if len(L) <= 2:
        return max(L)

    with_last = problem9(L[:-2]) + L[-1]
    without_last = problem9(L[:-1])
    return max(with_last, without_last)



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(problem9(([-8, 4, -3, 2, 3, 4])))
