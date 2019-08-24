"""
    If you have an iterable that is too large to fit in memory in full
    (e.g., when dealing with large files), being able to take and use
    chunks of it at a time can be very valuable.

    Implement a generator function, chunker, that takes in an iterable
    and yields a chunk of a specified size at a time.

    Calling the function like this:

    for chunk in chunker(range(25), 4):
    print(list(chunk)

"""

def chunker(iterable, size):
    # Implement function here
    i = 0
    while size <= len(iterable):
        yield list(range(i, size))
        i += 4
        size += 4
    yield [i]

for chunk in chunker(range(25), 4):
    print(chunk)


# Udacity Solution

def chunker(iterable, size):
    "Yield successive chunks from iterable of length size"
    for i in range(0, len(iterable), size):
        yield iterable[i: i + size]
for chunk in chunker(range(25), 4):
    print(list(chunk))


chunk_1 = lambda x,y: [ x[i:i+y] for i in range(0,len(x),y)]
for chunk_2 in chunk_1(range(25), 4):
    print(list(chunk_2))
