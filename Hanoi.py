def hanoi(n, source, temp, target):
    """
    Solution to the Tower of Hanoi Problem.
    Moves n discs from the first tower to the target tower.
    :param n: number of discs to be moved
    :param source: Array containing discs in starting position.
    :param temp: An empty array
    :param target: An empty array.
    :return: None
    """
    if n == 1:
        target.append(source.pop())
    else:
        # move n-1 disks from source to temp:
        hanoi(n - 1, source, target, temp)
        # move disk from source peg to target peg
        target.append(source.pop())
        # move n-1 disks from temp to target
        hanoi(n - 1, temp, source, target)


if __name__ == "__main__":
    source = [5, 4, 3, 2, 1]
    target = []
    temp = []
    hanoi(len(source), source, temp, target)

    print(source, temp, target)
