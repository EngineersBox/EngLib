class mathlib:

    def __init__(self):
        self.cfg_path = ""

    def getdsign(pos1, pos2):
        value = pos2 - pos1
        if value < 0:
            return -1
        elif value == 0:
            return 0
        else:
            return 1

    def retVector(x1, y1, x2, y2, limChange=True, changeMult=1):
        dx = x2 - x1
        dy = y2 - y1
        if limChange == False:
            changeMult = 9
        if dx < 0 and dy < 0:
            return [-1 * changeMult, -1 * changeMult]
        elif dx == 0 and dy < 0:
            return [0, -1 * changeMult]
        elif dx < 0 and dy == 0:
            return [-1 * changeMult, 0]
        elif dx > 0 and dy > 0:
            return [1 * changeMult, 1 * changeMult]
        elif dx == 0 and dy > 0:
            return [0, 1 * changeMult]
        elif dx > 0 and dy == 0:
            return [1 * changeMult, 0]
        elif dx < 0 and dy > 0:
            return [-1 * changeMult, 1 * changeMult]
        elif dx > 0 and dy < 0:
            return [1 * changeMult, -1 * changeMult]
        else:
            pass
