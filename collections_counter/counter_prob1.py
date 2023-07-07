from collections import Counter


num_shoes = int(input())
shoes_sizes = list(map(int, input().split()))
number_of_customers = int(input())

shoes_sizes_dict = Counter(shoes_sizes)
# for size in shoes_sizes:
#     if size in shoes_sizes_dict:
#         shoes_sizes_dict[size] +=1
#     else:
#         shoes_sizes_dict[size] = 1

Total_price = 0
for _ in range(number_of_customers):
    siz, price = map(int, input().split())
    if siz in shoes_sizes_dict and shoes_sizes_dict[siz] > 0:
        Total_price += price
        shoes_sizes_dict[siz] -= 1

print(Total_price)
