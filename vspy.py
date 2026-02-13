# print("hello")
# class student:
#     def __init__(self,A,B):
#         self.a=A
#         self.b=B
#     def sum(self,s):
#         s=self.a + self.b
#         print(s)
# s1=student(2,5)
# s1.sum()



class Student:
    def __init__(self, A, B):
        self.a = A
        self.b = B

    def sum(self):
        s = self.a + self.b
        print(s)  # ✅ print the calculated sum

s1 = Student(2, 5)
s1.sum()  # Output: 7
