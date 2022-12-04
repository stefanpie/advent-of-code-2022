from pathlib import Path

script_dir = Path(__file__).parent


if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read()

    groups_raw = input_raw.split("\n\n")
    groups = {idx: list(map(int, group.split("\n"))) for idx, group in enumerate(groups_raw)}

    groups_sum = {idx: sum(group) for idx, group in groups.items()}
    group_largest_sum_idx, group_largest_sum  = max(groups_sum.items(), key=lambda x: x[1])

    part_1 = group_largest_sum
    print(f"Part 1: {part_1}")

    
    top_3 = sorted(groups_sum.items(), key=lambda x: x[1], reverse=True)[:3]
    top_3_sum = sum([x[1] for x in top_3])
    
    part_2 = top_3_sum
    print(f"Part 2: {part_2}")
