function solution(s) {
    dic = {};
    answer = [];
    for (let i = 0; i < s.length; i++) {
        const a = dic[s[i]];
        const b = i - a;
        answer.push(b ? b : -1);
        dic[s[i]] = i;
    }
    
    return answer;
}