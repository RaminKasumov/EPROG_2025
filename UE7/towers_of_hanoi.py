def move_tower(n, source, target, auxiliary, rods):
    if n == 0:
        return

    move_tower(n-1, source, auxiliary, target, rods)

    disk = rods[source].pop()
    rods[target].append(disk)
    print(f"Move disk {disk} from rod {source+1} to rod {target+1}")

    move_tower(n-1, auxiliary, target, source, rods)

rods = [[3,2,1], [], []]
move_tower(3, 0, 2, 1, rods)