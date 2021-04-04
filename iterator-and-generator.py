import random

'''
1) Write a generator which computes the running average.

'''


def compute_running_average():
    average = 0.0
    total = 0.0
    counter = 0

    while True:
        term = yield average
        total += term
        counter += 1
        average = total / counter


average_generator = compute_running_average()
average_generator.send(None)

# for term in range(1, 11):
#     print(average_generator.send(term))

'''
2) Write a generator frange, which behaves like range but accepts float values.

'''


def frange(start, end, step):
    while start < end:
        yield start
        start += step


# for i in frange(0.0, 1.0, 0.1):
#     print(i)

'''
3) Write a generator trange, which generates a sequence of time tuples from start to stop incremented 
by step. A time tuple is a 3-tuple of integers: (hours, minutes, seconds) So a call to trange might 
look like this: trange( (10, 10, 10), (13, 50, 15), (0, 15, 12) )

'''


def trange(start, end, step):
    start, end, step = list(start), list(end), list(step)

    while start < end:
        yield tuple(start)
        start[0] += step[0]
        start[1] += step[1]
        start[2] += step[2]

        start[1] = start[1] + 1 if start[2] // 60 == 1 else start[1]
        start[2] %= 60
        start[0] = start[0] + 1 if start[1] // 60 == 1 else start[0]
        start[1] %= 60
        start[0] %= 24


# for i in trange((10, 10, 10), (13, 50, 15), (0, 15, 12)):
#     print(i)

'''
4) Write a version "rtrange" of the previous generator, which can receive messages to reset the start value.

'''


def rtrange(start, end, step):
    current, end, step = list(start), list(end), list(step)

    while current < end:
        start = yield tuple(current)

        if start is not None:
            current = list(start)
            continue

        current[0] += step[0]
        current[1] += step[1]
        current[2] += step[2]

        current[1] = current[1] + 1 if current[2] // 60 == 1 else current[1]
        current[2] %= 60
        current[0] = current[0] + 1 if current[1] // 60 == 1 else current[0]
        current[1] %= 60
        current[0] %= 24


# ts = rtrange((10, 10, 10), (17, 50, 15), (1, 15, 12))
# for _ in range(3):
#     print(next(ts))

# print(ts.send((8, 5, 50)))
# for _ in range(3):
#     print(next(ts))

'''
5) Write a program, using the newly written generator "trange", to create a file "times_and_temperatures.txt". 
The lines of this file contain a time in the format hh::mm::ss and random temperatures between 10.0 
and 25.0 degrees. The times should be ascending in steps of 90 seconds starting with 6:00:00. For example:

06:00:00 20.1
06:01:30 16.1
06:03:00 16.9
06:04:30 13.4
06:06:00 23.7
06:07:30 23.6
06:09:00 17.5
06:10:30 11.0

'''


# with open("times_and_temperatures.txt", "w") as f:
#     for t in trange((6, 0, 0), (6, 11, 0), (0, 1, 30)):
#         time = "{:02d}:{:02d}:{:02d}".format(*t)
#         temperature = round(random.uniform(10.0, 25.0), 1)
#         f.write(f"{time} {temperature}")
#         f.write("\n")

'''
6) Write a generator with the name "random_ones_and_zeroes", which returns a bitstream, i.e. a zero or a 
one in every iteration. The probability p for returning a 1 is defined in a variable p. The generator will 
initialize this value to 0.5. In other words, zeroes and ones will be returned with the same probability.

'''


def random_ones_and_zeroes(p=0.5):
    while True:
        c = random.uniform(0, 1)

        if c < p:
            yield 0
        else:
            yield 1


# roz = random_ones_and_zeroes()
# for _ in range(8):
#     print(next(roz), end='')
# print()

'''
7) We wrote a class Cycle in the beginning of this chapter of our Python tutorial. Write a generator 
"cycle" performing the same task.

'''


def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


# c = cycle("abc")
# for _ in range(8):
#     print(next(c))
