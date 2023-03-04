from pathlib import Path
import numpy as np



script_dir = Path(__file__).parent



def run_program(instructions: list[str]):
    current_cycle = 1
    x_reg = 1

    history_cycle = []
    history_x_reg = []

    for i, op in enumerate(instructions):
        if op.startswith("noop"):
            current_cycle += 1
            history_cycle.append(current_cycle)
            history_x_reg.append(x_reg)
        elif op.startswith("addx"):
            val = int(op.split(" ")[1])

            current_cycle += 1
            history_cycle.append(current_cycle)
            history_x_reg.append(x_reg)
            
            current_cycle += 1
            x_reg += val
            history_cycle.append(current_cycle)
            history_x_reg.append(x_reg)
    
    return history_cycle, history_x_reg


def run_program

if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read()

    input_raw_lines = input_raw.splitlines()

    history_cycle, history_x_reg = run_program(input_raw_lines)
    print(history_cycle)
    print(history_x_reg)


    cycle_locs = [20, 60, 100, 140, 180, 220]
    cycle_locs_idx = [history_cycle.index(i) for i in cycle_locs]
    signal_strengths = [history_cycle[i] * history_x_reg[i] for i in cycle_locs_idx]
    print(signal_strengths)
    sum_signal_strengths = sum(signal_strengths)
    print(sum_signal_strengths)

    part_1 = None
    print(f"Part 1: {part_1}")

    part_2 = None
    print(f"Part 2: {part_2}")
