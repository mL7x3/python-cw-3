# write your code here
favorite_animals = ["cat", "dog", "bird", "monkey"]

print(favorite_animals[1])

favorite_animals.remove("monkey")

print(favorite_animals)

favorite_animals.append("gorilla")

print(favorite_animals)

for f_a in favorite_animals:
    print(f"i love {f_a}")

number = [1, 2, 3, 4, 5]

number_sum = 0

for num in number:
    number_sum += num
print(number_sum)
