def calculate(no_of_people,total_amount,currency):
    if no_of_people<=1:
        raise ValueError("Number of people must be greater than one")

    share=total_amount/no_of_people



    print(f"Total Expense:{currency}{total_amount}")
    print(f"No.of people:{no_of_people}")
    print(f"Each member need to pay:{currency}{share}")

def main():
    try:
        no_of_people=int(input("Enter the no of people:"))
        total_amount=float(input("Enter the amount spent:"))
        calculate(no_of_people,total_amount,currency="₹")

    except ValueError as e:
        print(f"Error:{e}")
main()