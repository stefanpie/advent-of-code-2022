from pathlib import Path


script_dir = Path(__file__).parent

map_abc = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

map_xyz = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

score_shape = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

score_loss = 0
score_draw = 3
score_win = 6

def who_wins(move_a, move_b):
    if move_a == move_b:
        return "draw"
    elif move_a == "rock" and move_b == "scissors":
        return "a"
    elif move_a == "scissors" and move_b == "paper":
        return "a"
    elif move_a == "paper" and move_b == "rock":
        return "a"
    elif move_b == "rock" and move_a == "scissors":
        return "b"
    elif move_b == "scissors" and move_a == "paper":
        return "b"
    elif move_b == "paper" and move_a == "rock":
        return "b"

def eval_strategy_guide_v0(guide):
    score_self = 0
    score_opponent = 0
    for round in guide:
        move_other_symbol = round[0]
        move_self_symbol = round[1]

        move_other = map_abc[move_other_symbol]
        move_self = map_xyz[move_self_symbol]


        winner = who_wins(move_self, move_other)
        if winner == "a":    
            score_self += score_win
            score_opponent += score_loss
        elif winner == "b":
            score_self += score_loss
            score_opponent += score_win
        elif winner == "draw":
            score_self += score_draw
            score_opponent += score_draw

        score_self += score_shape[move_self]

    return score_self, score_opponent

map_xyz_v1 = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

def chose_my_move(move_other, end_condition):
    if end_condition == "win":
        if move_other == "rock":
            return "paper"
        elif move_other == "paper":
            return "scissors"
        elif move_other == "scissors":
            return "rock"
    elif end_condition == "draw":
        return move_other
    elif end_condition == "lose":
        if move_other == "rock":
            return "scissors"
        elif move_other == "paper":
            return "rock"
        elif move_other == "scissors":
            return "paper"

def eval_strategy_guide_v1(guide):
    # The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
    score_self = 0
    score_opponent = 0
    for round in guide:
        move_other_symbol = round[0]
        end_self_symbol = round[1]

        move_other = map_abc[move_other_symbol]
        end_self = map_xyz_v1[end_self_symbol]

        move_self = chose_my_move(move_other, end_self)

        winner = who_wins(move_self, move_other)
        if winner == "a":
            score_self += score_win
            score_opponent += score_loss
        elif winner == "b":
            score_self += score_loss
            score_opponent += score_win
        elif winner == "draw":
            score_self += score_draw
            score_opponent += score_draw
        
        score_self += score_shape[move_self]

    return score_self, score_opponent
        

if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.readlines()
    
    guide = [x.strip().split(" ") for x in input_raw]

    score_self_0, score_opponent_0 = eval_strategy_guide_v0(guide)

    part_1 = score_self_0
    print(f"Part 1: {part_1}")


    score_self_1, score_opponent_1 = eval_strategy_guide_v1(guide)

    part_2 = score_self_1
    print(f"Part 2: {part_2}")
