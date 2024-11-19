##Created by SAL on 11/18/2024

for i in range(99, 0, -1):
    if i > 1:
        print(f'{i} bottle{"" if i==1 else "s"} of beer on the wall, {i} bottle{"" if i==1 else "s"} of beer\nTake one down and pass it around, {i-1 or "no more"} bottle{"" if i-1==1 else "s"} of beer on the wall.\n')
else:
    print('One last bottle of beer on the wall, One last bottle of beer.\nTake one down and pass it around, No more bottles of beer on the wall.\n')
    print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')
