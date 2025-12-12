import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_tictactoe(board, title="Tic-Tac-Toe"):
    fig, ax = plt.subplots(figsize=(5,5))
    for i in range(4):
        ax.plot([i/3, i/3], [0,1], color='black', linewidth=2)
        ax.plot([0,1], [i/3, i/3], color='black', linewidth=2)
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            cx = (j + 0.5)/3
            cy = 1 - (i + 0.5)/3
            half = 0.12
            if val.lower() == 'o':
                circle = patches.Circle((cx, cy), half, fill=False, linewidth=2)
                ax.add_patch(circle)
            elif val.lower() == 'x':
                ax.plot([cx-half, cx+half], [cy-half, cy+half], color='black', linewidth=2)
                ax.plot([cx-half, cx+half], [cy+half, cy-half], color='black', linewidth=2)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

sample = [
    ['x', 'o', 'x'],
    ['', 'o', ''],
    ['x', '', 'o']
]
plot_tictactoe(sample)