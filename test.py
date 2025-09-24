
s = 'abccdef'
left = 0
right = 0
cnt = [False for _ in range(26)]
print(cnt)
ans = 0
while right < len(s):
	while cnt[ord(s[right]) - ord('a')]:
		cnt[ord(s[left]) - ord('a')] = False
		left = left + 1
	cnt[ord(s[right]) - ord('a')] = True 

	if right - left + 1 > ans:
		ans = right - left + 1
	print(f'right:{right} left:{left} ans:{ans}')
	right = right + 1

print(ans)
print(len(s))
'''
right=0,s[right]='a'
[1,0,0,0,0,0]
ans=1
right=1,s[right]='b'
[1,1,0,0,0,0]
ans=2
right=2,s[right]='c'
[1,1,1,0,0,0]
ans=3
right=3,s[right]='c',s[left]='a'
[0,1,1,0,0,0]
right=3,s[right]='c',s[left]='b'
[0,0,1,0,0,0]
right=3,s[right]='c',s[left]='c'
[0,0,0,0,0,0]
right=4,s[right]='d',
[0,0,0,1,0,0]
left=3,ans=3
right=5,s[right]='e',
[0,0,0,1,1,0]
left=3,ans=3
right=6,s[right]='f',
[0,0,0,1,1,1]
left=3,ans=3
'''



