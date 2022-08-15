# age = 12
# if 0 <= age < 21:
#     print("am not legal")
# else:
#     print("am legal")
#
# message = "eligible" if age <= 23 else "not eligible"
# print(message)
#
# for x in range(4):
#     for y in range(4):
#         print(f"{x} and {y}")
# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count = count + 1
#         print(number)
# print(f"we have {count} even numbers")
#
# square = []
# for value in range(1, 11):
#     squares = value ** 2
#     square.append(squares)
# print(square)
# print("\n")
#
# summ = sum(range(1, 1_0001))
# print(summ)
#
# for let in range(1, 21, 2):
#     print(let)
#
# multiples = [3, 9, 12, 15, 18, 21]
# for multiple in multiples:
#     print(multiple)
# cubes = []
# for value in range(1, 11):
#     cube = value ** 3
#     cubes.append(cube)
# print(cubes)
#
# lists = []
# for i in range(1, 11):
#     lists.insert((i - 1), i ** 3)
#
# print(lists)
#
# may = [val ** 3 for val in range(1, 10)]
# print(may)

person = {"name": "mariama", "last_name": "cham", "age": 22, "city": "paris"}
print(person["name"] + "\n" + person["last_name"] + "\n" + str(person["age"]) + "\n" + person["city"])

favorite_numbers = {"mariama": 8, "fatima": 67, "john": 9}
favorite_numbers0 = {"mariama": 8, "fatima": 67, "john": 9, "betty": 45}

rivers = {"nile": "egypt", "river gambia": "gambia", "limpopo": "south africa"}
for river, place in rivers.items():
    print(f"\n{river.title()} runs through {place.title()}")
for river, place in rivers.items():
    print(river, place)
