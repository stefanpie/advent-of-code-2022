from pathlib import Path
import numpy as np

from matplotlib import pyplot as plt


script_dir = Path(__file__).parent


def manhatten_distance(x_0: tuple[int, int], x_1: tuple[int, int]):
    return abs(x_0[0] - x_1[0]) + abs(x_0[1] - x_1[1])
        

class Rope:
    def __init__(self, rope_len: int) -> None:
        self.rope_len = rope_len

    @property
    def rope_knots(self):
        rope = ["H"]
        for i in range(1, self.rope_len+1):
            rope.append(f"{i}")
        return rope
    
    def sim_rope(self, moves: list[tuple[str, int]]):
        pos = {knot: (0,0) for knot in self.rope_knots}

        moves_elaborated: list[str] = []
        for move in moves:
            d,s = move
            moves_elaborated.extend([d] * s)

        pos_history = {knot: [pos[knot]] for knot in self.rope_knots}

        for move_simple in moves_elaborated:
            d = move_simple
            for knot in self.rope_knots:
                if knot == "H":
                    if d == "U":
                        pos[knot] = (pos[knot][0], pos[knot][1] + 1)
                    elif d == "D":
                        pos[knot] = (pos[knot][0], pos[knot][1] - 1)
                    elif d == "L":
                        pos[knot] = (pos[knot][0] - 1, pos[knot][1])
                    elif d == "R":
                        pos[knot] = (pos[knot][0] + 1, pos[knot][1])
                else:
                    previous_knot = self.rope_knots[self.rope_knots.index(knot) - 1]
                    distance_to_previous_knot = manhatten_distance(pos[knot], pos[previous_knot])

                    if distance_to_previous_knot > 1:
                        # same row
                        if pos[knot][0] == pos[previous_knot][0]:
                            if pos[previous_knot][1] > pos[knot][1]:
                                pos[knot] = (pos[knot][0], pos[knot][1] + 1)
                            else:
                                pos[knot] = (pos[knot][0], pos[knot][1] - 1)
                        # same column
                        elif pos[knot][1] == pos[previous_knot][1]:
                            if pos[previous_knot][0] > pos[knot][0]:
                                pos[knot] = (pos[knot][0] + 1, pos[knot][1])
                            else:
                                pos[knot] = (pos[knot][0] - 1, pos[knot][1])
                        # diagonal
                        else:
                            if distance_to_previous_knot > 2:
                                if pos[previous_knot][0] > pos[knot][0] and pos[previous_knot][1] > pos[knot][1]:
                                    pos[knot] = (pos[knot][0] + 1, pos[knot][1] + 1)
                                elif pos[previous_knot][0] > pos[knot][0] and pos[previous_knot][1] < pos[knot][1]:
                                    pos[knot] = (pos[knot][0] + 1, pos[knot][1] - 1)
                                elif pos[previous_knot][0] < pos[knot][0] and pos[previous_knot][1] > pos[knot][1]:
                                    pos[knot] = (pos[knot][0] - 1, pos[knot][1] + 1)
                                elif pos[previous_knot][0] < pos[knot][0] and pos[previous_knot][1] < pos[knot][1]:
                                    pos[knot] = (pos[knot][0] - 1, pos[knot][1] - 1)
                
            for knot in self.rope_knots:
                pos_history[knot].append(pos[knot])

        return pos_history


if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read()

    input_raw_lines = input_raw.splitlines()
    moves = []
    for line in input_raw_lines:
        d, s = line.split(" ")
        moves.append((d, int(s)))

    rope = Rope(1)
    pos_history = rope.sim_rope(moves)
    num_unique_pos_t = len(set(pos_history["1"]))

    part_1 = num_unique_pos_t
    print(f"Part 1: {part_1}")


    rope_9 = Rope(9)
    pos_history_9 = rope_9.sim_rope(moves)
    num_unique_pos_t_9 = len(set(pos_history_9["9"]))

    part_2 = num_unique_pos_t_9
    print(f"Part 2: {part_2}")
