import { sudoku } from './sudoku.js';
import * as fs from 'fs';

let data = [];

for (var _ = 0; _ < 10000; _++) {
    var problem = sudoku().generate("medium");
    var problemGrid = sudoku().board_string_to_grid(problem);

    data.push(problemGrid)

}

let json = JSON.stringify({
    "problems": data
});

fs.writeFileSync('sudokus.json', json);



