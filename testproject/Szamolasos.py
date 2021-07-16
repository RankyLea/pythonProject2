# while True:
#     x = input("Adj meg egy szamot: ")
#     y = input("Adj meg meg egy szamot: ")
#     print(int(x) - int(y))
#
# my_list = [56, 42, 78, 12, 33]
# for i in my_list:

# salary = 8000
#
#
# def printSalary():
#     salary = 12000
#     print("Salary: ", salary)
#
#
# printSalary()
# print("Salary: ", salary)

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 ==0:
            continue
            var += 1
    var += 1
else:
    var += 1
print(var)
