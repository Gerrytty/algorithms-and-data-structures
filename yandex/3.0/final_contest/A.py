class Target:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __repr__(self):
        return f"{self.name} {self.num}"

if __name__ == "__main__":
    n = int(input())

    arr = []

    for i in range(n):
        command = input().split()

        if command[0] == "add":
            arr.append(Target(command[2], int(command[1])))

        elif command[0] == "delete":
            need_to_del = int(command[1])

            while need_to_del > 0:
                if len(arr) > 0:
                    target = arr[-1]
                    if target.num <= need_to_del:
                        need_to_del -= target.num
                        arr.pop()
                    else:
                        target.num -= need_to_del
                        need_to_del = 0
                        break
                else:
                    break

        elif command[0] == "get":
            count = 0
            for j in range(len(arr)):
                if arr[j].name == command[1]:
                    count += arr[j].num
            print(count)