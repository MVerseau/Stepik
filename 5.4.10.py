class ReversibleString:
    def __init__(self, string):
        self.string=string

    def __str__(self):
        return f'{self.string}'

    def __neg__(self):

        return ReversibleString(self.string[-1::-1])

# TEST_1:
string = ReversibleString('python')

print(string)
print(-string)

# TEST_2:
string = ReversibleString('p')

print(string)
print(-string)

# TEST_3:
string = ReversibleString('')

print(string)
print(-string)

# TEST_4:
string = ReversibleString("Namespaces are one honking great idea -- let's do more of those!")

print(string)
print(-string)

# TEST_5:
string = ReversibleString('beegeek')

print(-string)
print(type(-string))

# TEST_6:
strings = [ReversibleString('social'), ReversibleString('history'), ReversibleString('certain'),
           ReversibleString('end'), ReversibleString('wear'), ReversibleString('into'), ReversibleString('PM'),
           ReversibleString('factor'), ReversibleString('budget'), ReversibleString('I'), ReversibleString('know'),
           ReversibleString('statement'), ReversibleString('similar'), ReversibleString('do'), ReversibleString('with'),
           ReversibleString('voice'), ReversibleString('fact'), ReversibleString('already'),
           ReversibleString('quality'), ReversibleString('growth'), ReversibleString('television'),
           ReversibleString('during'), ReversibleString('direction'), ReversibleString('fact'),
           ReversibleString('system'), ReversibleString('floor'), ReversibleString('production'),
           ReversibleString('dog'), ReversibleString('image'), ReversibleString('price'), ReversibleString('while'),
           ReversibleString('conference'), ReversibleString('though'), ReversibleString('white'),
           ReversibleString('statement'), ReversibleString('view'), ReversibleString('fight'), ReversibleString('plan'),
           ReversibleString('third'), ReversibleString('minute'), ReversibleString('rate'), ReversibleString('with'),
           ReversibleString('soldier'), ReversibleString('book'), ReversibleString('whose'), ReversibleString('decade'),
           ReversibleString('only'), ReversibleString('ago'), ReversibleString('study'), ReversibleString('at'),
           ReversibleString('message'), ReversibleString('first'), ReversibleString('challenge'),
           ReversibleString('more'), ReversibleString('paper'), ReversibleString('senior'),
           ReversibleString('practice'), ReversibleString('wrong'), ReversibleString('edge'),
           ReversibleString('knowledge'), ReversibleString('person'), ReversibleString('much'),
           ReversibleString('race'), ReversibleString('piece'), ReversibleString('management'),
           ReversibleString('pass'), ReversibleString('vote'), ReversibleString('performance'),
           ReversibleString('brother'), ReversibleString('sister'), ReversibleString('apple'),
           ReversibleString('early'), ReversibleString('while'), ReversibleString('director'),
           ReversibleString('consumer'), ReversibleString('city'), ReversibleString('reason'), ReversibleString('boy'),
           ReversibleString('off'), ReversibleString('trip'), ReversibleString('action'), ReversibleString('physical'),
           ReversibleString('always'), ReversibleString('myself'), ReversibleString('despite'),
           ReversibleString('early'), ReversibleString('a'), ReversibleString('bill'), ReversibleString('part'),
           ReversibleString('even'), ReversibleString('summer'), ReversibleString('behavior'),
           ReversibleString('attorney'), ReversibleString('artist'), ReversibleString('project'),
           ReversibleString('test'), ReversibleString('win'), ReversibleString('and'), ReversibleString('character'),
           ReversibleString('particularly')]

for string in strings:
    print(-string)