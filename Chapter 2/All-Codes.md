# 2.1 Numbers

```
-29
```

```
0
```

```
1415926535897932384626433832795028841971693993
```

```
20.22
```

```
-11.291117
```

```
3.1415926535897932384626433832795028841971693993
```

```
100000000000000000000000000000.11
```

```
1000_000_000
```

# 2.2 Strings

```
"This is a string in Python"
```

```
"Everything is '42'."
```

```
"it's always tea time"
```

# 2.3 Lists

```
["Pawn", "Knight", "Bishop", "Rook", "Queen"]
```

```
[1, 3, 3, 5, 9]
```

```
["Pawn",1, "Knight",3, "Bishop",3, "Rook",5, "Queen",9]
```

# 2.4 True and False

```
True
```

```
False
```

```
not True
```

```
not False
```

```
2 > 5
```

```
0 == 0
```

```
10 == "10"
```

```
2.5 != 2.55
```

```
-1 < 0
```

```
1.9 <= 2
```

```
100 > 99
```

```
5 >= 6
```

# 2.5 Variables

```
Cup = None
```

```
Cup = "coffee"
```

```
Cup = Cup + " milk "
Cup
```

# 2.7 Multiple assignments

```
a, b = 2
a
```

```
b
```

```
m, d = 12, 5
```

# 2.8 Arithmetic Operators

```
a, b = 12, 26
```

```
a + b
```

```
a - b
```

```
a * b
```

```
12.6 / 3.0
```

```
12.6 / 3
```

```
43 / 11
```

```
43 // 11
```

```
43 % 11
```

```
2**4
```

# 2.9 Built-In Functions

```
abs(9.33)
```

```
abs(0)
```

```
abs(-7)
```

```
round(12.2)
```

```
round(-13.51)
```

```
round(1.618033988749894, 5)
```

```
round(123113122022, -8)
```

```
min(12, 41, 13, 12, 20, 22)
```

```
max(12, 41, 13, 12, 20, 22)
```

```
a = [9, 18, 19, 1, 19, 8, 1, 16, 15, 21, 18, 9]
max(a)
```

```
int("24")
```

```
int(2.50)
```

```
float("2.53")
```

```
float(254)
```

```
str(256)
```

```
str(2.56)
```

```
int("Feb")
```

# 2.10 String Operations

```
str1 = "Beautiful is"
str2 = "better than ugly."
string = str1 + " " + str2
string
```

```
result = len(string)
result
```

```
str1[0]
```

```
str1[len(str1) - 1]
```

```
string = "Explicit is better than implicit."
result = string[12:18]
result
```

```
string = "Simple is better than complex."
result = string[22:]
result * 5
```

# 2.11 List Operations

```
list1 = ["1", "3", "5", "7", "11"]
list2 = ["13", "17", "19", "23"]
list3 = list1 + list2
list3
```

```
result = len(list3)
result
```

```
list3[0]
```

```
list3[len(list3) - 1]
```

```
list3[:4]
```

```
list3[0] = 2
list3
```

```
string = "251"
string[0] = "3"
```

```
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
list1
```

```
list1.append(7)
list1
```

```
list1 = [1, 3]
list1.insert(1, 2)
list1
```

```
list1 = [3, 4, 6]
list1.pop()
```

```
list1
```

```
list1 = [3, 4, 9]
list1.pop(1)
```

```
list1 = [1, 2, 3, 4, 2]
list1.remove(2)
list1
```

```
list1 = [2, 1, 6, 4, 3, 7]
list1.sort()
list1
```

```
list1.reverse()
list1
```

# 2.12 Input And Output


```
print("Hello World")
```

```
name = "Irsa"
print("Hello, " + name)
```

```
name = input("What is your name? ")
print("Hello, " + name)
```

# 2.13 if, elif and else

```
height = int(input("How tall are you (cm)?"))
if height >= 150:
    print("You are tall enough to ride the roller coaster!")
```

```
height = int(input("Enter your height (cm): "))
age = int(input("Enter your age: "))

if height >= 150 and age >= 12:
    print("You can ride!")

else:
    print("You can't ride.")
```

```
number = int(input("Pick a number between 1 and 100: "))
if number >= 1 and number <= 33:
    print("In the lower third?")
elif number > 33 and number <= 66:
    print("In the middle third?")
else:
    print("In the upper third?")
```

# 2.14 Loops

```
count = 1
while count <= 100:
    print(count)
    count += 1
```

```
while True:
    print("This is an infinite loop")
```

```
count = 0
while True:
    count += 1
    if count == 5:
        break
    print(count)
```

```
count = 1
while count <= 10:
    print(count)
    count += 1
```

```
count = 1
while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(count)
    count += 1
```

```
fruits = ["apple", "banana", "cherry"]
```

```
for fruit in fruits:
    print(fruit)
```

```
for character in "abc":
    print(character)
```

```
for i in range(1, 6):
    print(i)
```

# 2.15 Functions


```
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)

print(result)
```

```
def reverse_string(s):
    return s[::-1]

result = reverse_string("spider")

print(result)
```

```
def word_counter(s):
    return len(s.split())

result = word_counter("Complex is better than complicated.")

print(result)
```

# 2.16 Data Structures

```
movie = ("The Matrix", 1999, "Sci-Fi")
```

```
print(movie[0])
print(movie[1])
print(movie[2])
```

```
movies = [
    ("The Matrix", 1999, "Sci-Fi"),
    ("Inception", 2010, "Action"),
    ("Interstellar", 2014, "Sci-Fi"),
    ("The Dark Knight", 2008, "Action"),
    ("The Shawshank Redemption", 1994, "Drama"),
]
```

```
print(movies[0])
print(movies[1])
```

```
print(movies[0][0])
print(movies[0][1])
print(movies[0][2])
```

```
numbers = [1, 2, 3, 4, 5, 2, 4, 5, 6, 7, 7, 8, 9, 9, 10]
unique_numbers = list(set(numbers))
print(unique_numbers)
```

```
friend_A = {'🍕', '🍔', '🌭'}
friend_B = {'🍕', '🥗', '🍟'}
```

```
print(friend_A | friend_B) 
#print(friend_A.union(friend_B))
```

```
print(friend_A & friend_B) 
#print(friend_A.intersection(friend_B))
```

```
print(friend_A - friend_B)
#print(friend_A.difference(friend_B))
print(friend_B - friend_A)
#print(friend_B.difference(friend_A))
```

```
student_grades = {"Alice": 96, "Bob": 80, "Charlie": 92}
```

```
print(student_grades["Alice"])
```

```
student_grades["David"] = 85
print(student_grades)
```

```
student_grades["Bob"] = 95
print(student_grades)
```

```
del student_grades["Charlie"]
print(student_grades)
```

```
planets = {
 "Mercury": {"Distance from Sun (AU)": 0.39, "Moons": 0},
 "Venus": {"Distance from Sun (AU)": 0.72, "Moons": 0},
 "Earth": {"Distance from Sun (AU)": 1.00, "Moons": 1},
 "Mars": {"Distance from Sun (AU)": 1.52, "Moons": 2},
 "Jupiter": {"Distance from Sun (AU)": 5.20, "Moons": 79}
}
```

```
print(planets["Earth"]["Distance from Sun (AU)"])
print(planets["Mars"]["Moons"])
```

# 2.17 Working With Files

```
import os
```

```
path = "/Users/irsa/Desktop/Python-Book/Chapter2/Codes/C2.md"
print(os.path.basename(path))
```

```
print(os.path.splitext(path))
```

```
print("Does the file exist?", os.path.exists(path))
```

```
print("Is the path a file?", os.path.isfile(path))
```

```
print("Is the path a directory?", os.path.isdir(path))
```

```
path = "/Users/irsa/Desktop/Python-Book"
path = os.path.join(path, "Chapter2", "Codes")
print(path)
```

```
import os
print("The current working directory is:", os.getcwd())
```

```
os.chdir("/Users/irsa/Desktop/Python-Book/Chapter2/Codes")
print(os.getcwd())
```

```
path = "/Users/irsa/Desktop/Python-Book/Chapter2/Codes/new_dir"

if not os.path.exists(path):
    os.mkdir(path)
    print("Directory created successfully.")
else:
    print("Directory already exists.")
```

```
if os.path.exists(path):
    os.rmdir(path)
    print("Directory removed successfully.")
else:
    print("Directory does not exist.")
```

```
old_path = "/Users/irsa/Desktop/Python-Book/Chapter2/Codes/C2.md"
new_path = "/Users/irsa/Desktop/Python-Book/Chapter2/Codes/Chapter2.md"

if os.path.exists(old_path):
    os.rename(old_path, new_path)
    print("File renamed successfully.")
else:
    print("File does not exist.")
```

```
path = "/Users/irsa/Desktop/Python-Book/Chapter2/Codes/test.py"

if os.path.exists(path):
    os.remove(path)
    print("File removed successfully.")
else:
    print("File does not exist.")
```

```
import shutil
```

```
src_path = 'Chapter2/Codes/C2.md'
dst_path = 'Chapter1/Codes/C2-cp.md'
shutil.copy(src_path, dst_path)
```

```
src_path = 'Chapterw/Codes/C2-cp.md'
dst_path = 'Backup/C2.md'
shutil.move(src_path, dst_path)
```

```
dir_path = 'Backup'
shutil.rmtree(dir_path)
```

```
dir_path = 'Chapter2'
archive_path = 'Chapter2/Codes'
shutil.make_archive(archive_path, 'zip', dir_path)
```

```
file = open('text-file.txt', 'r')
```

```
file = open('Chapter III/images/Figure_1.png', 'rb')
```

```
file = open('new-text-file.txt', 'w')
```

```
file = open('Chapter III/images/New_Figure.png', 'wb')
```

```
file = open('new-text-file.txt', 'r+')
```

```
file = open('new-text-file.txt', 'a')
```

```
file = open('new-text-file.txt', 'a+')
```

```
file = open('Chapter2/Codes/spider_story.txt', 'r')
content = file.read()
file.close()
print(content)
```

```
file = open('file.txt', 'w')
file.write('Flat is better than nested.')
file.close()
```

```
with open('Chapter2/Codes/spider_story.txt', 'r') as file:
    content = file.read()
    count = 0
    for letter in content:
        if letter == 'a':
            count += 1
    print(count)
```

# 2.18 Exception Handling

```
try:
    x = 10 / 0
except:
    print("Division by zero is not allowed.")
```

```
try:
    file = open("example.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access the file.")
except:
    print("An unknown error occurred.")
```
