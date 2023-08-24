arr = input()
# print(arr)

if arr in ('fdsajkl;', 'jkl;fdsa'):
    print('in-out')
elif arr in ('asdf;lkj', ';lkjasdf'):
    print('out-in')
elif arr == 'asdfjkl;':
    print('stairs')
elif arr == ';lkjfdsa':
    print('reverse')
else:
    print('molu')