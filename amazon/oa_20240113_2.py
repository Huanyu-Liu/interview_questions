from collections import defaultdict
test_case = [3, 1, 3, 5]

def solution(test_stock):

    visited1 = {}
    visited2 = {}

    dp_list1 = [1]
    n = len(test_stock)
    previous_max = True
    current_max = test_stock[0]
    current_sum 
    for i in range(1, n):
        if test_stock[i] > current_max:
            if previous_max:
                dp_list1.append(dp_list1[i - 1] + 1)
            current_max = test_stock
            previous_max = True
        else:
            previous_max = False
            dp_list1.append(1)

    dp_list2 = [0] * n 
    current_max = test_stock[-1]
    previous_max = True
    # dp_list2[-1] = 1
    for i in range(n - 2, -1, -1):
        if test_stock[i] >= current_max:
            dp_list2[i] = dp_list2[i + 1] + 1

    def dp1(stocks, index):
        if index in visited1:
            return visited1[index]
        if index == 0:
            visited1[0] = 1
            return 1
        if stocks[index] > stocks[index - 1]:
            visited1[index] = dp1(stocks, index - 1) + 1
        else:
            visited1[index] = 0

        return visited1[index]
    

    def dp2(stocks, index):
        if index in visited2:
            return visited2[index]
        n = len(stocks) - 1
        if index == n:
            visited2[n] = 1
            return 1
        if stocks[index] >= stocks[index + 1]:
            visited2[index] = dp2(stocks, index + 1) + 1
        else:
            visited2[index] = 0

        return visited2[index]

    print(dp1(test_stock, 3))
    print(dp2(test_stock, 0))
    print(visited1)
    print(visited2)
    print(dp_list1)
    print(dp_list2)

if __name__ == "__main__":
    solution(test_case)
