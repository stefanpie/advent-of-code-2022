from pathlib import Path


script_dir = Path(__file__).parent

def item_priority(item: str):
        if item.islower():
            return ord(item) - 96
        else:
            return ord(item) - 38

class Rucksack:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input

        input_length = len(raw_input)
        self.compartment_0 = set(list(raw_input[:input_length // 2]))
        self.compartment_1 = set(list(raw_input[input_length // 2:]))
        self.compartment_all = set(list(raw_input))

    @property
    def common_item(self):
        intersection = self.compartment_0.intersection(self.compartment_1)
        assert len(intersection) == 1
        return list(intersection)[0]    

    @property
    def common_item_priority(self):
        return item_priority(self.common_item)

# As you finish identifying the misplaced items, the Elves come to you with another issue.
# For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.
# The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.
# Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.


class ElfGroup:
    def __init__(self, rucksacks: list):
        assert len(rucksacks) == 3
        self.rucksacks = rucksacks
    
    def group_common_item(self):
        # item type that is common between all three Elves
        intersection = self.rucksacks[0].compartment_all & self.rucksacks[1].compartment_all & self.rucksacks[2].compartment_all
        assert len(intersection) == 1
        return list(intersection)[0]

    def group_common_item_priority(self):
        return item_priority(self.group_common_item())
        
    
if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read().splitlines()
    

    rucksacks = [Rucksack(raw_input) for raw_input in input_raw]

    sum_priority = sum([rucksack.common_item_priority for rucksack in rucksacks])

    part_1 = sum_priority
    print(f"Part 1: {part_1}")

    groups = [ElfGroup(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)]
    sum_goruup_priority = sum([group.group_common_item_priority() for group in groups])

    part_2 = sum_goruup_priority
    print(f"Part 2: {part_2}")
