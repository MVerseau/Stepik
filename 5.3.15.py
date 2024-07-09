class Vector:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (self.x, self.y) == (other.x, other.y)
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        else:
            return NotImplemented



# TEST_4:
vectors = [Vector(196, 21), Vector(102, 82), Vector(91, 28), Vector(137, 128), Vector(97, 69), Vector(79, 29), Vector(93, 62), Vector(85, 58), Vector(46, 176), Vector(84, 197)]
pairs = [(26, 86), (177, 150), (144, 175), (137, 128), (110, 196), (79, 29), (93, 62), (36, 158), (180, 24), (84, 167)]

for vector, pair in zip(vectors, pairs):
    print(vector == pair, vector != pair)

# TEST_5:
vectors1 = [Vector(114, 220), Vector(180, 148), Vector(85, 58), Vector(49, 246), Vector(110, 250), Vector(50, 91), Vector(60, 55), Vector(75, 238), Vector(189, 88), Vector(33, 190)]
vectors2 = [Vector(148, 144), Vector(169, 296), Vector(85, 58), Vector(172, 94), Vector(191, 55), Vector(50, 91), Vector(181, 150), Vector(43, 167), Vector(98, 238), Vector(33, 190)]

for v1, v2 in zip(vectors1, vectors2):
    print(v1 == v2, v1 != v2)

# TEST_6:
a = Vector(0, 1)
not_supported = [[1, 2], True, (1, 2, 3, 4), 'beegeek', {'name': 'Grace Hopper'}, {18, 22}]

for item in not_supported:
    print(a == item)

# TEST_7:
a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)

# TEST_8:
vector = Vector(0, 1)

print(vector.__eq__(1))
print(vector.__ne__(1.1))
print(vector.__gt__(range(5)))
print(vector.__lt__([1, 2, 3]))
print(vector.__ge__({4, 5, 6}))
print(vector.__le__({1: 'one'}))