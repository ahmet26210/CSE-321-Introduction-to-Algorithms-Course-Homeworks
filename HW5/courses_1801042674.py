class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos
        
def maxMeeting(l, n,ans,time_limit):
    for i in range(1, n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end

    for i in ans:
        print(i + 1, end = " ")

if __name__ == '__main__':
    start_time = [1,3,0,5,8,5]
    finish_time = [2,4,6,7,9,9]
    length = len(start_time)
    arr = []
    ans = []
    for i in range(length):
        arr.append(meeting(start_time[i], finish_time[i], i))
    arr.sort(key = lambda x: x.end)
    ans.append(arr[0].pos)
    time_limit = arr[0].end
    maxMeeting(arr, length,ans,time_limit)