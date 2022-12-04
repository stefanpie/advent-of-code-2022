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
