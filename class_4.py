"""

СПИСКИ

people = ['anna','bob','kate']


nums = [1, 10, 0.58, "abc", [1,2,3], [1. ['a']]]

"anna" in people
True


name = 'kate'
 if name in people:
	print('yea!!')
 else:
       print('no')

>>> nums = [0,1,2]+[6,7,10]
>>> nums
[0, 1, 2, 6, 7, 10]
>>> nums.apend(11)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    nums.apend(11)
AttributeError: 'list' object has no attribute 'apend'
>>> nums.append(11)
>>> nums
[0, 1, 2, 6, 7, 10, 11]
>>> nums.append ([100,200,300])
>>> nums
[0, 1, 2, 6, 7, 10, 11, [100, 200, 300]]
>>> nums[3]
6
>>> nums[-1]
[100, 200, 300]
>>> nums[-1][0]
100
>>> nums[-1][-1]
300

nums = [1,2,3]
for n in nums:
    print(n)
    


nums = []
for n in range(5):
    print(n)
    nums.append(n)
print(nums)


nums = []
for n in range(5):
    print(n)
    nums.append(n)
    print(nums)
print('length:', len(nums))


#СЛАЙСЫ

text = "i want to die"
words = text.split()
print(words)
print(words[0:2])
print(words[2:])
for w in words[::2]:
    print(w)
    


nums = [[1,2,3]]*3
print(nums)
for row in nums:
    #print(row)
    #print('inner')
    for n in row:
        print(n, end=' ')
    print()
  
#символы word => ['w', 'o', 'r', 'd']

w = "word"
letters = []
for j in w:
    letters.append(j)
print(letters)

>>> w = 'hello'
>>> l = list(w)
>>> l
['h', 'e', 'l', 'l', 'o']
>>> str(l)
"['h', 'e', 'l', 'l', 'o']"




nums = [1, 2, 3]
nums_str = ""
for d in nums:
    nums_str = nums_str + str(d) + " "
print(nums_str)
nums_str = nums_str[:-1]
print(nums_str)

.join => разделитель, только с str
>>> letters=list('hello')
>>> letters
['h', 'e', 'l', 'l', 'o']
>>> ' '.join(letters)
'h e l l o'
>>> '!'.join(letters)
'h!e!l!l!o'





>>> letters = list('hello')
>>> letters
['h', 'e', 'l', 'l', 'o']
>>> new = letters.pop()
>>> new
'o'
>>> letters
['h', 'e', 'l', 'l']



letters = list('hello')
letters.pop(-2)
print(letters)


letters = list('hello world')
print(letters.index('e'))
print(letters.count('o'))
print(sorted(letters))



letters = list('hello world')
print(letters)
print(sorted(letters, reverse = True))
nums = [2,3,14,1,1,0]
print(sorted(nums, reverse = True))



>>> nums = [1,2,3,4,14,1,0,2]
>>> nums = sorted(nums)
>>> nums
[0, 1, 1, 2, 2, 3, 4, 14]
>>> nums = [1,2,3,4,14,1,0,2]
>>> nums
[1, 2, 3, 4, 14, 1, 0, 2]
>>> nums[::-1]
[2, 0, 1, 14, 4, 3, 2, 1]
>>> nums = [1,2,3,4,14,1,0,2]
>>> nums.reverse()
>>> nums
[2, 0, 1, 14, 4, 3, 2, 1]

"""

nums =[[1,2,3,4]]*5
#print(nums)
for row in nums:
    print(row)
    row.reverse()
    
        











