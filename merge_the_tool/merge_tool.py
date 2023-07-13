def merge_the_tools(string, k):
    pair_number = len(string)//k
    y = 0
    for x in range(k,len(string)+1,k):
        main_value = []

        splitted_string = string[y:x]
        y = x
        for st in splitted_string:
            if st not in main_value:
                main_value.append(st)
        print("".join(main_value))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)