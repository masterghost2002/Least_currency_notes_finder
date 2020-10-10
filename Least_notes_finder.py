##     Build Date 09/10/2020 by Rakesh Dhariwal
## Least number of notes to be given on form in 1,2,5,10,100,200,500,2000 currency amount
def least_notes():
    try:
        amount = int(input("Enter Amount Of Which U Want Least N Currency Notes\n"))
    except Exception as e:
        print("Please Correctly Enter The Amount In Numeric Form")
        least_notes()
    if amount == 0:
        print("Please Enter Amount\n")
        least_notes()
    elif amount % 2000 == 0:
        notes_2000 = amount / 2000
        print(f"Number Of 2000rs Notes: {notes_2000}")
        print(f"\nTotal Notes         : {notes_2000}")
    elif amount % 2000 != 0:
        reminder_d_2000 = amount % 2000
        amount_left_2000 = amount - reminder_d_2000
        new_2000_notes = amount_left_2000 / 2000
        if reminder_d_2000 % 500 == 0:
            notes_500 = reminder_d_2000 / 500
            print(f"Number of 2000rs Notes: {new_2000_notes}")
            print(f"Number of 500rs  Notes: {notes_500}\n")
            print(f"Total Notes           : {new_2000_notes + notes_500}")
        elif reminder_d_2000 % 500 != 0:
            reminder_d_500 = reminder_d_2000 % 500
            amount_left_500 = reminder_d_2000 - reminder_d_500
            new_500_notes = amount_left_500 / 500
            if reminder_d_500 % 200 == 0:
                notes_200 = reminder_d_500 / 200
                print(f"Number of 2000rs Notes: {new_2000_notes}")
                print(f"Number of 500rs  Notes: {new_500_notes}")
                print(f"Number of 200rs  Notes: {notes_200}\n")
                print(f"Total Notes           : {new_2000_notes + new_500_notes + notes_200}")
            elif reminder_d_500 % 200 != 0:
                reminder_d_200 = reminder_d_500 % 200
                amount_left = reminder_d_500 - reminder_d_200
                new_notes_200 = amount_left / 200
                if reminder_d_200 % 100 == 0:
                    notes = reminder_d_200 / 100
                    print(f"Number of 2000rs Notes: {new_2000_notes}")
                    print(f"Number of 500rs  Notes: {new_500_notes}")
                    print(f"Number of 200rs  Notes: {new_notes_200}")
                    print(f"Number of 100rs  Notes: {notes}\n")
                    print(f"Total Notes           : {new_2000_notes + new_500_notes + new_notes_200 + notes}")
                elif reminder_d_200 % 100 != 0:
                    reminder_d_100 = reminder_d_500 % 100
                    amount_left = reminder_d_200 - reminder_d_100
                    notes_100 = amount_left / 100
                    if reminder_d_100 % 50 == 0:
                        notes_50 = reminder_d_100 / 50
                        print(f"Number of 2000rs Notes: {new_2000_notes}")
                        print(f"Number of 500rs  Notes: {new_500_notes}")
                        print(f"Number of 200rs  Notes: {new_notes_200}")
                        print(f"Number of 100rs  Notes: {notes_100}")
                        print(f"number of 50rs   Notes: {notes_50}\n")
                        print(f"Total Number          : {new_2000_notes + new_500_notes + new_notes_200 + notes_100 + notes_50}")
                    elif reminder_d_100 % 50 != 0:
                        reminder_d_50 = reminder_d_100 %50
                        amount_left_d_50 = reminder_d_100 - reminder_d_50
                        new_50_notes = amount_left_d_50 / 50
                        if reminder_d_50 % 10 == 0:
                            notes_10 = reminder_d_50 / 10
                            print(f"Number of 2000rs Notes: {new_2000_notes}")
                            print(f"Number of 500rs  Notes: {new_500_notes}")
                            print(f"Number of 200rs  Notes: {new_notes_200}")
                            print(f"Number of 100rs  Notes: {notes_100}")
                            print(f"Number of 50rs   Notes: {new_50_notes}")
                            print(f"Number of 10rs   Notes: {notes_10}\n")
                            print(f"Total Notes           : {new_2000_notes + new_500_notes + new_notes_200 + notes_100 + new_50_notes + notes_10}")
                        elif reminder_d_50 % 10 != 0:
                            reminder_d_10 = reminder_d_50 % 10
                            amount_left_d_50 = reminder_d_50 - reminder_d_10
                            new_10_notes = amount_left_d_50 / 10
                            if reminder_d_10 % 5 == 0:
                                notes_5 = reminder_d_10 / 5
                                print(f"Number of 2000rs Notes: {new_2000_notes}")
                                print(f"Number of 500rs  Notes: {new_500_notes}")
                                print(f"Number of 200rs  Notes: {new_notes_200}")
                                print(f"Number of 100rs  Notes: {notes_100}")
                                print(f"Number of 50rs   Notes  {new_50_notes}")
                                print(f"Number of 10rs   Notes: {new_10_notes}")
                                print(f"Number of 5rs    Notes: {notes_5}\n")
                                print(f"Total Notes           : {new_2000_notes + new_500_notes + new_notes_200 + notes_100 + new_50_notes + new_10_notes + notes_5}")
                            elif reminder_d_10 % 5 != 0:
                                reminder_d_5 = reminder_d_10 % 5
                                amount_left_d_5 = reminder_d_10 - reminder_d_5
                                new_5_notes = amount_left_d_5 / 5
                                if reminder_d_5 % 2 == 0:
                                    notes_2 = reminder_d_5 / 2
                                    print(f"Number of 2000rs Notes: {new_2000_notes}")
                                    print(f"Number of 500rs  Notes: {new_500_notes}")
                                    print(f"Number of 200rs  Notes: {new_notes_200}")
                                    print(f"Number of 100rs  Notes: {notes_100}")
                                    print(f"Number of 50rs   Notes: {new_50_notes}")
                                    print(f"Number of 10rs   Notes: {new_10_notes}")
                                    print(f"Number of 5rs    Notes: {new_5_notes}")
                                    print(f"Number of 2rs    Notes: {notes_2}\n")
                                    print(f"Total Notes           : {new_2000_notes + new_500_notes + new_notes_200 + notes_100 + new_50_notes + new_10_notes + new_5_notes + notes_2}")
                                elif reminder_d_5 % 2 != 0:
                                    reminder_d_2 = reminder_d_5 % 2
                                    amount_left_d_2 = reminder_d_5 - reminder_d_2
                                    new_2_notes = amount_left_d_2 / 2
                                    notes_1 = reminder_d_2
                                    print(f"Number of 2000rs Notes: {new_2000_notes}")
                                    print(f"Number of 500rs  Notes: {new_500_notes}")
                                    print(f"Number of 200rs  Notes: {new_notes_200}")
                                    print(f"Number of 100rs  Notes: {notes_100}")
                                    print(f"Number of 50rs   Notes: {new_50_notes}")
                                    print(f"Number of 10rs   Notes: {new_10_notes}")
                                    print(f"Number of 5rs    Notes: {new_5_notes}")
                                    print(f"Number of 2rs    Notes: {new_2_notes}")
                                    print(f"Number of 1rs    Notes: {notes_1}\n")
                                    print(f"Total Notes           : {new_2000_notes + new_500_notes + new_notes_200 + notes_100 + new_50_notes + new_10_notes + new_5_notes + new_2_notes + notes_1}")
if __name__ == '__main__':
    print("Welcome!\nThis Program Gives U Least Number of Indian Currency Notes To Give\nIn form of 1rs, 2rs, 5rs, 10rs,200rs, 100rs, 500rs, 2000rs\n")
    least_notes()
