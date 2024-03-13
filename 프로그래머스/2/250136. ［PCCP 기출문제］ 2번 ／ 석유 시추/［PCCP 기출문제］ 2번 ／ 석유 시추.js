function countOil(land, x, y, save) {
    const [dx, dy] = [[-1, 1, 0, 0], [0, 0, -1, 1]];
    let count = 1;
    land[x][y] = 0;
    const Stack = [[x, y]];
    const array = [y];
    while (Stack.length) {
        const cur = Stack.pop();
        for (let i = 0; i < 4; i++) {
            const [x_, y_] = [cur[0] + dx[i], cur[1] + dy[i]];
            if (x_ >= 0 && x_ < land.length && y_ >= 0 && y_ < land[0].length && land[x_][y_]) {
                land[x_][y_] = 0;
                count++;
                Stack.push([x_, y_]);
                array.push(y_);
            }
        }
    }
    const newArray = [...new Set(array)];
    for (let i = 0; i < newArray.length ; i++) {
        save[newArray[i]].push(count);
    }
}

function solution(land) {
    const save = Array.from({ length: land[0].length }, () => []);
    for (let i = 0; i < land.length; i++) {
        for (let j = 0; j < land[0].length; j++) {
            if (land[i][j]) countOil(land, i, j, save);
        }
    }
    
    let answer= 0;
    for (let i = 0; i < save.length; i++) {
        let tmp = 0;
        for (let j = 0; j < save[i].length; j++) {
            tmp += save[i][j];
        }
        answer = Math.max(answer, tmp);
    }
    
    return answer;
}