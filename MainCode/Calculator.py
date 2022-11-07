class Calculator:

    def __init__(self):
        self.first_no = None
        self.second_no = None
        self.operator_code = None

    def __show_input_request(self):

        for i in range(0, 2):
            if i == 0:
                try:
                    userinput = float(input("Enter the first number: "))
                    a = userinput
                except ValueError:
                    print("Input not supported, Please enter a number to continue")
                    self.__show_input_request()
                    return
            else:
                try:
                    userinput = float(input("Enter the second number: "))
                    b = userinput
                except ValueError:
                    print("Input not supported, Please enter a number to continue")
                    self.__show_input_request()
                    return

        self.__get_inputs(a, b)

    def __show_operator_code_request(self):
        print("\nChoose One of the Operator Codes below!!\n")
        print("\tFor Addition, Enter '1'\n\tFor Subtraction, Enter '2'\n"
              "\tFor Division, Enter '3'\n\tFor Multiplication, Enter '4'")
        try:
            operator = int(input("\nEnter here: "))
            self.operator_code = operator
            self.__calculate()
        except ValueError:
            print("!!You Entered the wrong operator code, please check and try again!!")
            self.__show_operator_code_request()

    def __get_inputs(self, first_number, second_number):
        self.first_no = first_number
        self.second_no = second_number

    def __get_operator(self, operator_code):
        self.operator_code = operator_code

    def __calculate(self):
        # should have used match statement but only supported in python 3.10 and above
        if self.operator_code == 1:
            result = self.first_no + self.second_no
        elif self.operator_code == 2:
            result = self.first_no - self.second_no
        elif self.operator_code == 3:
            result = self.first_no / self.second_no
        elif self.operator_code == 4:
            result = self.first_no * self.second_no
        else:
            print("Invalid operator code, Please Enter a result from from the one listed above")
            self.__show_operator_code_request()
            return

        print(f"The result of your calculation is: {result}")

    def run(self):
        print("Welcome to Neo's Calculator App\n------------------------------")
        self.__show_input_request()
        self.__show_operator_code_request()
