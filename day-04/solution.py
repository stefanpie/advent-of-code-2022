from pathlib import Path


script_dir = Path(__file__).parent

class SectionAssignments:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end
    def enumerate(self):
        return range(self.start, self.end + 1)

def check_full_containment(section_assignment_0: SectionAssignments, section_assignment_1: SectionAssignments):
    full_range_0 = set(section_assignment_0.enumerate())
    full_range_1 = set(section_assignment_1.enumerate())
    if full_range_0.issubset(full_range_1):
        return True
    elif full_range_1.issubset(full_range_0):
        return True
    else:
        return False

def check_any_overlap(section_assignment_0: SectionAssignments, section_assignment_1: SectionAssignments):
    full_range_0 = set(section_assignment_0.enumerate())
    full_range_1 = set(section_assignment_1.enumerate())
    if full_range_0.isdisjoint(full_range_1):
        return False
    else:
        return True

def process_input(input_raw: list[str]):
    assignment_pairs: list[tuple] = []
    for line in input_raw:
        person_0, person_1 = line.split(",")
        person_0_start, person_0_end = person_0.split("-")
        person_1_start, person_1_end = person_1.split("-")
        person_0_start_int = int(person_0_start)
        person_0_end_int = int(person_0_end)
        person_1_start_int = int(person_1_start)
        person_1_end_int = int(person_1_end)
        assignment_pairs.append((
            SectionAssignments(person_0_start_int, person_0_end_int),
            SectionAssignments(person_1_start_int, person_1_end_int)
        ))
    return assignment_pairs

if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read().splitlines()

    assignment_pairs = process_input(input_raw)

    containment_checks = [check_full_containment(*assignment_pair) for assignment_pair in assignment_pairs]
    containment_checks_true_sum = sum(containment_checks)

    part_1 = containment_checks_true_sum
    print(f"Part 1: {part_1}")

    
    overlap_checks = [check_any_overlap(*assignment_pair) for assignment_pair in assignment_pairs]
    overlap_checks_true_sum = sum(overlap_checks)

    part_2 = overlap_checks_true_sum
    print(f"Part 2: {part_2}")
