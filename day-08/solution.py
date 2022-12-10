from pathlib import Path
import numpy as np

script_dir = Path(__file__).parent


def compute_visible_trees(grid: np.ndarray) -> np.ndarray:
    visible_trees = np.zeros_like(grid)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            height = grid[i, j]
            row_left = grid[i, :j]
            row_right = grid[i, j + 1 :]
            col_up = grid[:i, j]
            col_down = grid[i + 1 :, j]
            can_see_left = np.all(row_left < height)
            can_see_right = np.all(row_right < height)
            can_see_up = np.all(col_up < height)
            can_see_down = np.all(col_down < height)
            visible = can_see_left or can_see_right or can_see_up or can_see_down
            visible_trees[i, j] = visible

    return visible_trees

def compute_senic_score(grid: np.ndarray, i: int, j: int) -> int:
    height = grid[i, j]

    row_left = grid[i, :j]
    row_right = grid[i, j + 1 :]
    col_up = grid[:i, j]
    col_down = grid[i + 1 :, j]

    blocking_row_left = row_left >= height
    blocking_row_right = row_right >= height
    blocking_col_up = col_up >= height
    blocking_col_down = col_down >= height

    dist_left = int(np.argmax(blocking_row_left[::-1]))+1 if np.any(blocking_row_left) else len(row_left)
    dist_right = int(np.argmax(blocking_row_right))+1 if np.any(blocking_row_right) else len(row_right)
    dist_up = int(np.argmax(blocking_col_up[::-1]))+1 if np.any(blocking_col_up) else len(col_up)
    dist_down = int(np.argmax(blocking_col_down))+1 if np.any(blocking_col_down) else len(col_down)

    senic_score = dist_left * dist_right * dist_up * dist_down
    return senic_score

def compute_senic_scores(grid: np.ndarray) -> np.ndarray:
    senic_scores = np.zeros_like(grid)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            senic_scores[i, j] = compute_senic_score(grid, i, j)

    return senic_scores

if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read()

    grid_list = [list(line) for line in input_raw.splitlines()]
    grid_list_int = [[int(char) for char in line] for line in grid_list]
    grid = np.asarray(grid_list_int)

    visible_trees = compute_visible_trees(grid)    
    num_visible_trees = np.sum(visible_trees)

    part_1 = num_visible_trees
    print(f"Part 1: {part_1}")

    senic_scores = compute_senic_scores(grid)
    max_senic_score = np.max(senic_scores)

    part_2 = max_senic_score
    print(f"Part 2: {part_2}")
