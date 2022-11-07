class StudentDisplay:

    def __init__(self):
        self.name = None
        self.age = None
        self.department = None

    def __get_user_input(self):
        username = input("\nEnter your name: ")
        self.__save_name(username)

        user_age = input("\nEnter your age: ")
        self.__save_age(user_age)

        user_dept = input("\nWhat is your department: ")
        self.__save_department(user_dept)

    def __save_name(self, user_name):
        self.name = user_name

    def __save_age(self, user_age):
        self.age = user_age

    def __save_department(self, dept):
        self.department = dept

    def __display_student_info(self):
        print("\nBased on the details supplied by this user, this is the student's details\n"
              "----------------------------------------------------------------------------\n"
              f"\tStudent's name: {self.name}\n"
              f"\tStudent's age: {self.age}\n"
              f"\tStudent's department: {self.department}")

    def run(self):
        print("Hello there, Welcome to my simple student display program.\n"
              "Please provide the needed details below")
        self.__get_user_input()
        self.__display_student_info()
