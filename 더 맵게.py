Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(scoville, K):
...     import heapq
...     heapq.heapify(scoville)
...     answer = 0
...     
...     while scoville[0] < K:
...         if len(scoville) > 1:
...             first = heapq.heappop(scoville)
...             second = heapq.heappop(scoville)
...             new = first + (second*2)
...             heapq.heappush(scoville, new)
...             answer += 1
...         else:
...             return -1
...                 
