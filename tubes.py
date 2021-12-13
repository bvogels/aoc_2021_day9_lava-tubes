size = 0


class Tubes:

    def __init__(self):
        self.risk = 0
        self.basins = []
        with open("testdata", "r") as data:
            self.tubes = [line.rstrip().split() for line in data]
        for n, tube in enumerate(self.tubes):
            l = list(tube[0])
            self.tubes[n] = l

    def lowpoint(self):
        for r, row in enumerate(self.tubes):
            for c, col in enumerate(row):
                if r == 0 or c == 0 or c == len(row) - 1 or r == len(self.tubes) - 1:
                    if r == 0 and c == 0:  # top left corner
                        if self.tubes[r][c] < self.tubes[r][c + 1] and self.tubes[r][c] < self.tubes[r + 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                    if r == 0 and c > 0 and c < len(row) - 1:  # top row
                        if self.tubes[r][c] < self.tubes[r][c - 1] and self.tubes[r][c] < self.tubes[r][c + 1] and \
                                self.tubes[r][
                                    c] < self.tubes[r + 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                    if r == 0 and c == len(row) - 1:  # top right corner
                        if self.tubes[r][c] < self.tubes[r][c - 1] and self.tubes[r][c] < self.tubes[r + 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                    if r == len(self.tubes) - 1 and c == 0:  # bottom left corner
                        if self.tubes[r][c] < self.tubes[r][c + 1] and self.tubes[r][c] < self.tubes[r - 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                    if r == len(self.tubes) - 1 and c < len(row) - 1:  # bottom row
                        if self.tubes[r][c] < self.tubes[r][c - 1] and self.tubes[r][c] < self.tubes[r][c + 1] and \
                                self.tubes[r][
                                    c] < self.tubes[r - 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                    if r == len(self.tubes) - 1 and c == len(row) - 1:  # bottom right corner
                        if self.tubes[r][c] < self.tubes[r][c - 1] and self.tubes[r][c] < self.tubes[r - 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                    if r > 0 and r < len(self.tubes) - 1 and c == 0:  # left column
                        if self.tubes[r][c] < self.tubes[r][c + 1] and self.tubes[r][c] < self.tubes[r - 1][c] and \
                                self.tubes[r][c] < self.tubes[r + 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                    if r > 0 and r < len(self.tubes) - 1 and c == len(row) - 1:  # right column
                        if self.tubes[r][c] < self.tubes[r][c - 1] and self.tubes[r][c] < self.tubes[r - 1][c] and \
                                self.tubes[r][c] < self.tubes[r + 1][c]:
                            self.risk += int(self.tubes[r][c]) + 1
                            print("Row: ", r, ", Col: ", c)
                            continue
                        else:
                            continue
                else:
                    if self.tubes[r][c] < self.tubes[r][c - 1] and self.tubes[r][c] < self.tubes[r][c + 1] and \
                            self.tubes[r][c] < self.tubes[r + 1][c] and self.tubes[r][c] < self.tubes[r - 1][c]:
                        self.risk += int(self.tubes[r][c]) + 1

    def basin(self):
        for r, row in enumerate(self.tubes):
            for c, col in enumerate(row):
                if col != 9:
                    Tubes.size = 0
                    self.gauge(r, c, Tubes.size)
                else:
                    continue

    def gauge(self, r, c, size):
        if int(self.tubes[r][c]) == 9 or c == len(self.tubes[r]) - 1:
            c = 0
            if int(self.tubes[r + 1][c]) != 9:
                self.gauge(r + 1, c, size)
            if int(self.tubes[r + 1][c + 1]) != 9:
            else:
                return
        else:
            self.gauge(r, c + 1, (size + 1))


if __name__ == "__main__":
    t = Tubes()
    #t.lowpoint()
    t.basin()
    print("Risk Level: ", t.risk)
