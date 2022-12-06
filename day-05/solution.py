import copy
from pathlib import Path
from collections import deque

script_dir = Path(__file__).parent

class CargoStack:
    def __init__(self, id: int, init_items: list[str]):
        self.id = id
        self.items = deque(init_items)

class Instruction:
    def __init__(self, from_id: int, to_id: int, count: int):
        self.from_id = from_id
        self.to_id = to_id
        self.count = count
    
    def __repr__(self) -> str:
        return f"Instruction(from_id={self.from_id}, to_id={self.to_id}, count={self.count})"

class CargoArea:
    def __init__(self, stacks: list[CargoStack]):
        self.stacks = stacks
    
    def get_stack_idx_by_id(self, id: int):
        for i, stack in enumerate(self.stacks):
            if stack.id == id:
                return i
        raise ValueError(f"Stack with id {id} not found")

    def execute_instruction(self, instruction: Instruction, mode="single"):
        from_stack_idx = self.get_stack_idx_by_id(instruction.from_id)
        to_stack_idx = self.get_stack_idx_by_id(instruction.to_id)
        if mode == "single":
            for i in range(instruction.count):
                current_item = self.stacks[from_stack_idx].items.pop()
                self.stacks[to_stack_idx].items.append(current_item)
        elif mode == "bulk":
            items_to_move = []
            for i in range(instruction.count):
                current_item = self.stacks[from_stack_idx].items.pop()
                items_to_move.append(current_item)
            items_to_move.reverse()
            self.stacks[to_stack_idx].items.extend(items_to_move)
        else:
            raise ValueError(f"Invalid mode {mode}")
        
    def execute_all_instructions(self, instructions: list[Instruction], mode="single"):
        for instruction in instructions:
            self.execute_instruction(instruction, mode=mode)

    def get_top_all_stacks(self):
        top_items = []
        for stack in self.stacks:
            top_items.append(stack.items[-1])
        return top_items



def parse_stacks(raw_input_stacks: str):
    raw_input_stacks_lines = raw_input_stacks.splitlines()

    stack_ids = raw_input_stacks_lines[-1].split()
    stack_ids_int = [int(stack_id) for stack_id in stack_ids]
    print(stack_ids_int)
    num_stacks = len(stack_ids)

    raw_input_stacks_lines = raw_input_stacks_lines[:-1]

    table: list[list[str]] = []
    for line in raw_input_stacks_lines:
        row = []
        for i in range(num_stacks):
            row.append(line[i*4:(i+1)*4])
        row = [item.strip().replace("[", "").replace("]", "") for item in row]
        table.append(row)

    table_t = list(map(list, zip(*table)))
    table_t_gathered = [list(filter(None, row)) for row in table_t]
    table_t_gathered_str = [[str(item) for item in row] for row in table_t_gathered]
    table_t_gathered_str_reverse = [row[::-1] for row in table_t_gathered_str]

    stacks = []
    for stack_id, stack_items in zip(stack_ids_int, table_t_gathered_str_reverse):
        stacks.append(CargoStack(stack_id, stack_items))
        
    cargo_area = CargoArea(stacks)

    return cargo_area


def parse_instructions(raw_instructions: str):
    instructions = []
    for raw_instruction in raw_instructions.splitlines():
        raw_instruction_numbers = raw_instruction.split()
        instruction_numbers = [int(raw_number) for raw_number in raw_instruction_numbers if raw_number.isdigit()]
        count, from_id, to_id = instruction_numbers
        instruction = Instruction(from_id, to_id, count)
        instructions.append(instruction)
        
    return instructions
        
    

def parse_raw_input(raw_input: str):
    raw_input_stacks, raw_instructions = raw_input.split("\n\n")
    cargo_area = parse_stacks(raw_input_stacks)
    instructions = parse_instructions(raw_instructions)

    return cargo_area, instructions

if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read()

    cargo_area, instructions = parse_raw_input(input_raw)

    cargo_area_0 = copy.deepcopy(cargo_area)
    cargo_area_0.execute_all_instructions(instructions, mode="single")
    top_items_0 = cargo_area_0.get_top_all_stacks()
    top_item_str_0 = "".join(top_items_0)

    part_1 = top_item_str_0
    print(f"Part 1: {part_1}")

    cargo_area_1 = copy.deepcopy(cargo_area)
    cargo_area_1.execute_all_instructions(instructions, mode="bulk")
    top_items_1 = cargo_area_1.get_top_all_stacks()
    top_item_str_1 = "".join(top_items_1)

    part_2 = top_item_str_1
    print(f"Part 2: {part_2}")
