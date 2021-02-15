import re

def get_containers(bag):
    containers = [data.strip() for data in all_bags if bag in data]
    unique_bags = []
    for container in containers:
        unique_bags.append(' '.join(container.split()[:2]))
    return unique_bags


with open('Day 7\\input.txt') as f:
    all_bags = f.readlines()

containers = set()
contains_shiny_gold_bag = get_containers('shiny gold bags')
containers.update(contains_shiny_gold_bag)

while contains_shiny_gold_bag:
    for bag in contains_shiny_gold_bag:
        contains_shiny_gold_bag.extend(get_containers(bag))
        containers.update(get_containers(bag))
        while bag in contains_shiny_gold_bag: contains_shiny_gold_bag.remove(bag)
        
containers.remove('shiny gold')
print(containers)
print(len(containers))