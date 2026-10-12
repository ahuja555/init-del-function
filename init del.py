class student:
    def __init__(self):
        print("Student object created")
    def __del__(self):
        print("Student object destroyed")
ob = student()
del ob