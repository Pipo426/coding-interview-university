def array_left_rotation(a, n, k):
    rotation_index = (k%n)
    return a[rotation_index:] + a[:rotation_index]

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
