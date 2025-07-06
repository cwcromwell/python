
# Compare two sets of triplets and decide whether a or b won the most rounds

a = [1, 2, 3]
b = [3, 2, 1]
score = [0, 0]

for i in range (0, len(a)):
    print("i =")
    print(i)
    if a[i] > b[i]:
        print("a wins")
        score[0] = score[0] + 1
    elif a[i] < b[i]:
        print("b wins")
        score[1] = score[1] + 1

    elif a[i] == b[i]: 
        print("It's a tie.")
        pass

return score