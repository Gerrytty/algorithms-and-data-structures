"""
We can go one, two or three steps by one
How many variants exits to go on step n?
"""
def get_num_vars(n):
    arr = []

    for i in range(n):
        # on 0 step we can go to one way (1)
        if i == 0:
            arr.append(1)
        # on 1 step we can go to two-ways (11, 2)
        elif i == 1:
            arr.append(2)
        # on 2 step we can go to three-ways (111, 12, 21)
        elif i == 2:
            arr.append(4)
        else:
            arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])

    return arr[-1]


def min_cost(costs):
    min_costs = [0, 0]
    prevs = []

    for i in range(2, len(costs)):
        if min_costs[i - 2] >= min_costs[i - 1]:
            prevs.append(i - 3)
            min_costs.append(min_costs[i - 2] + costs[i])
        else:
            prevs.append(i - 2)
            min_costs.append(min_costs[i - 1] + costs[i])

    steps = [len(costs) - 2]

    curr_step = steps[0]
    while curr_step != 1:
        steps.append(prevs[curr_step - 1])
        curr_step = prevs[curr_step - 1]

    return min_costs, prevs[1:], steps[::-1]

if __name__ == "__main__":
    print(min_cost([0, 0, 10, -5, -20, -10, 20, 30, -10, 10]))