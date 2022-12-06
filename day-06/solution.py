from pathlib import Path


script_dir = Path(__file__).parent


def find_lock_signal_idx(data: list[str], win_length):
    i = 0
    found = False
    window: list[str] = []
    while not found:
        if len(window) == win_length:
            window.pop(0)
            window.append(data[i])
        else:
            window.append(data[i])
        num_unique_items = len(set(window))
        if num_unique_items == win_length:
            found = True
        i += 1
    return i

if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read()
    data = list(input_raw)

    lock_signal_idx = find_lock_signal_idx(data, 4)

    part_1 = lock_signal_idx
    print(f"Part 1: {part_1}")

    message_signal_idx = find_lock_signal_idx(data, 14)

    part_2 = message_signal_idx
    print(f"Part 2: {part_2}")
