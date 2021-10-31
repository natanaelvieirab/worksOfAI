from data import data

def main():
    for test in data:
        if(test.isSolvable == test.board.isSolvable()):
            print("Ok")
        else:
            print("Not Ok")

main()