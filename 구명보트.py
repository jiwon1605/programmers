Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(people, limit):
...     answer = 0
...     people.sort()
...     front = 0
...     back = len(people) - 1
...     
...     while front < back:
...         if people[front] + people[back] <= limit:
...             front += 1
...             answer += 1
...         back -= 1
...             
