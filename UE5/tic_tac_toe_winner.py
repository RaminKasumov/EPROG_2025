def check_winner(pos):
    lines = []

    lines.extend(pos)
    lines.extend([[pos[r][c] for r in range(3)] for c in range(3)])

    lines.append([pos[i][i] for i in range(3)])
    lines.append([pos[i][2 - i] for i in range(3)])

    for line in lines:
        if line == ["X"] * 3:
            return "X wins"
        elif line == ["O"] * 3:
            return "O wins"
    return "No winner"

position = [["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "X"]]
print(check_winner(position))
