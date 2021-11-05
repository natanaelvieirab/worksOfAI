# Python3 program to check if a given
# instance of 8 puzzle is solvable or not

# este script verifica se um puzzle de tamanho oito é solucionavel !
# codigo retirado do site:
# https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/


# A utility function to count
# inversions in given array 'arr[]'
def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:

                print(f" v: {arr[i]} > v: {arr[j]}")
                inv_count += 1

    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle):

    # Print verision array of the list of list!
    print([j for sub in puzzle for j in sub])

    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])

    print(f"valor retornado foi: {inv_count}")
    # return true if inversion count is even.
    return (inv_count % 2 == 0)


# Driver code
puzzle = [[-1, 1, 2], [8, 4, 3], [7, 5, 6]]

for i in range(0, 3):
    print(puzzle[i])

if(isSolvable(puzzle)):
    print("Solvable")
else:
    print("Not Solvable")

    # This code is contributed by vitorhugooli
    # Fala meu povo desse Brasil varonil
