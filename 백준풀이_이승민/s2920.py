#리스트 받기
music_list = list(map(int, input().split()))
#원본 함수 복사
origin=music_list.copy()

# 오름차순 정렬 후 정렬 리스트  복사
music_list.sort()
asc=music_list.copy()

# 내림차순 정렬 후 정렬 리스트 복사
music_list.sort(reverse=True)
des=music_list.copy()

if origin == asc:
    print('ascending')
elif origin == des:
    print('descending')
else:
    print('mixed')


# origin=[1,2,3,5,4,6]
# asc= sorted(origin)
# des=sorted(origin, reverse=True)



# music_list=[1,3,4,5,6,7,8,2]
# origin=music_list.copy()
# music_list.sort()
# asc=music_list.copy()
# music_list.sort(reverse=True)
# des=music_list



# music_list.sort()
# asc=music_list
# # music_list.sort(reverse=False)
# # des=music_list
# print(origin)
# print(asc)
# print(des)
# # if music_list == 



