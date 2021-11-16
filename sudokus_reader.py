import json
import numpy as np

from typing import List, NewType

Grid = NewType("GRID",List[np.array])

class SudokusReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_sudokus(self) -> List[Grid]:
        res = []

        with open(self.file_path) as sudokus_file:
            problems = json.load(sudokus_file)["problems"]
        
        for problem in problems:
            # Convert '.' to 0 and cast everything to int
            problem = np.array([int(x) if x != "." else 0 for row in problem for x in row])
            problem = problem.reshape((9,9))
            res.append(problem)
    
        return res

if __name__ == "__main__":
    reader = SudokusReader("sudokus.json")
    sudokus = reader.read_sudokus()
    print(sudokus)