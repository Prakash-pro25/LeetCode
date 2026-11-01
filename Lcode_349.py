n1=int(input())
nums1=[int(input(f"num{i}")) for i in range(n1)]

n2=int(input())
nums2=[int(input(f"num{i}")) for i in range(n2)]


print(list(set(nums1)&set(nums2)))