word = input()
bomb = input()
Stack = []
for letter in word:
    Stack.append(letter)
    if len(Stack) >= len(bomb) and ''.join(Stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            Stack.pop()
if not Stack: print("FRULA")
else: print(''.join(Stack))