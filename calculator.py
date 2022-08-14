def rem_zero(x):
    x = round(x,3)
    return float(str(x).rstrip('0').rstrip('.'))

def calculator(
    num_of_benifitiaries, 
    total_comodity_amount, 
    comodity_amount, 
    num_of_days, 
    comodity, 
    unit
            ):
    
    initial_comodity_amount = total_comodity_amount
    daily_comodity_amount = comodity_amount * num_of_benifitiaries

    print("\nDaily %s consumption: %s %s"%(comodity,str(rem_zero(daily_comodity_amount)),unit[1]))

    for i in range(num_of_days):
        print("Day %d:-"%(i+1))
        print("Total amount = %s %s"%(total_comodity_amount,unit[0]))
        print("Consumed = %s %s"%(str(daily_comodity_amount),unit[1]))
        total_comodity_amount -= daily_comodity_amount/1000
        print("Remaining = %s %s"%(str(rem_zero(total_comodity_amount)),unit[0]))
        print("--------------------------------------------------------------------------------")
        if total_comodity_amount <= 0:
            print("You have consumed all the %s"%(comodity))
            break
    consumed_comodity_amount = rem_zero(initial_comodity_amount - total_comodity_amount)
    remaining_comodity_amount = rem_zero(total_comodity_amount)
    print("\nYou have consumed %s %s"%(str(consumed_comodity_amount if consumed_comodity_amount>1 else consumed_comodity_amount*1000), unit[0] if consumed_comodity_amount>1 else unit[1]))
    print("Remaining %s: %s"%(unit[0] if remaining_comodity_amount>1 else unit[1], str(remaining_comodity_amount if remaining_comodity_amount>1 else remaining_comodity_amount*1000)))

def main():
    num_of_benifitiaries = 0
    total_comodity_amount = 0 #in kgs
    comodity_amount = 0 #in grams
    num_of_days = 0
    comodity = ""
    unit = {}

    print("Choose the comodity to measure:-\n1. Salt\n2. Oil\n3. Daal\n4. Rice")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        comodity = "salt"
        unit = ["Kgs","Gms"]
    elif choice == 2:
        comodity = "oil"
        unit = ["Ltrs","Gms"]
    elif choice == 3:
        comodity = "daal"
        unit = ["Kgs","Gms"]
    elif choice == 4:
        comodity = "rice"
        unit = ["Kgs","Gms"]
    else:
        print("Invalid choice")
        exit()

    num_of_benifitiaries = int(input("Enter number of benifitiary students: "))
    total_comodity_amount = rem_zero(float(input("Enter amount of %s in reserve(%s): "%(comodity,unit[0]))))
    comodity_amount = rem_zero(float(input("Enter amount of %s used per head(%s): "%(comodity,unit[1]))))
    num_of_days = int(input("Enter number of days: "))

    calculator(num_of_benifitiaries,
                total_comodity_amount,
                comodity_amount, 
                num_of_days, 
                comodity,
                unit)



if __name__ == "__main__":
    main()
