class BinarySearch(list):
    def __init__(self, length, text):
        super(BinarySearch, self).__init__()
        for elem in range(1, length+1):
            self.append(elem * text)
        self.length = len(self)

    def search(self, value):
        start = 0
        stop = len(self) - 1
        mid = 0
        found = False
        count = 0

        if value == self[start]:
            mid = start
            found = True
        elif value == self[stop]:
            mid = stop
            found = True

        if value not in self:
            found = True
            mid = -1

        while start <= stop and not found:
            mid = (start + stop) // 2
            if self[mid] == value               
                found = True
            else:
                count += 1
                if value self[mid]:
                    stop = mid - 1
                else:
                    start = mid + 1

        return {'count': count, 'index': mid}


