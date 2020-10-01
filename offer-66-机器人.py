import collections
class Solution:
    def sum_rc(self,row,col):
        tmp = 0
        while row > 0:
            tmp += row % 10
            row //= 10
        while col > 0:
            tmp += col % 10
            col //= 10
        return tmp

    def movingCount(self, threshold, rows, cols):
        end=set()
        que=collections.deque()
        que.append((0,0))
        while que:
            dx,dy=que.popleft()
            if (dx,dy) not in end and self.sum_rc(dx,dy)<=threshold:
                end.add((dx,dy))
                for x, y in [(0, 1), (1, 0)]:
                    if 0 <= dx + x < rows and 0 <= dy + y < cols:
                        que.append((dx + x, dy + y))
        return len(end)

