with open('Day 7\\input.txt') as f:
    all_bags = f.readlines()
data = [data.strip() for data in all_bags]


bags = {}
count = 0
def get_contents(bag, mult):
    global count
    if bags[bag] is None:
        return
    for b, v in bags[bag].items():
        count += mult * v
        get_contents(b, v*mult)

for bag in data:
    b, c = bag.split('contain')
    if c == " no other bags.":
        bags.update({b.replace('bags', '').strip(): None})
        continue
    contents = {}
    for bg in c.split(','):
        v = int(bg[1])
        t = bg[2:]
        contents.update({t.replace('bags', '').replace(
            'bag.', '').replace('bag','').replace(' .', '').strip(): v})
    bags.update({b.replace('bags', '').strip(): contents})

get_contents('shiny gold', 1)
print(count)