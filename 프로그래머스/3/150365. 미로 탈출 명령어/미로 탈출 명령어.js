function solution(n, m, x, y, r, c, k) {
    let matrix = [];

    for (let i = 0; i < n; i++) {
        let array = ''
        for (let j = 0; j < m; j++) {
            array += '.';
        }
        matrix.push(array);
    }
    
    let paths = [];
    let fast_path = '';

    const dx = [1, 0, 0, -1];
    const dy = [0, -1, 1, 0];
    const direction = ['d', 'l', 'r', 'u'];
    
    let Q = [[x-1,y-1,0,'']];
    
    while (Q.length !== 0) {
        let [x_,y_,moved,path] = Q.shift();
        if (moved === k) {
            if (x_ === r - 1 && y_ === c - 1) paths.push(path);
            continue;
        }
        moved_ = moved + 1;
        for (let i = 0; i < 4; i++) {
            nx = x_ + dx[i];
            ny = y_ + dy[i];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            if (k - moved_ < Math.abs(r-1-nx) + Math.abs(c-1-ny)) continue;
            Q.push([nx, ny, moved_, path + direction[i]]);
        }
    }
    paths.sort();
    
    if (paths.length === 0) return 'impossible';
    return paths[0];
}