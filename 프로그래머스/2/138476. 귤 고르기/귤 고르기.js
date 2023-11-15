function solution(k, tangerine) {
    data = {};
    for (t of tangerine) {
        if (t in data) {
            data[t] += 1;
        } else {
            data[t] = 1;
        }
    }
    let sorted = Object.entries(data).sort((a, b) => b[1] - a[1]);
    let count = 0;
    let answer = 0;
    for (s of sorted) {
        count += s[1];
        answer += 1;
        if (count >= k) return answer
    }
}