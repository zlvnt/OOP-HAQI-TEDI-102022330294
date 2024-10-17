age = 20
if age >= 18:
    message = "Adult"
else:
    message = "Not Adult"
print(message)


x = "10"
y = 5
z = x * y
print(z)


def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text if char in vowels)

print(count_vowels("hello"))


def check_even(number):
    return number % 2 == 0

result = check_even(7)
print(result)


total = 0
for i in range(1, 5):
    total += i
print(total)


x = (1,2,3)
x[0] = 4
print(x)


my_list = [1, 2, 3, 4, 5]
print(my_list[3])


from array import array

def find_max_difference(arr):
    if len(arr) < 2:
        return "Array requires at least two elements"
    
    max_diff = arr[1] - arr[0]
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]
    
    return max_diff

test_array = array('i', [2, 3, 10, 6, 4, 8, 1])
output = find_max_difference(test_array)
print(output)