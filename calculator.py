def calculator(num_of_benifitiaries, food_amount, comodity_amount, num_of_days, comodity):
    total_food_amount = food_amount * num_of_days
    total_comodity_amount = comodity_amount * num_of_days
    total_comodity_amount = total_comodity_amount / 1000
    total_comodity_amount = total_comodity_amount / num_of_benifitiaries
    print("Total amount of %s is %s"%(comodity, total_comodity_amount))

def main():
    num_of_benifitiaries = 0
    food_amount = 0 #in kgs
    comodity_amount = 0 #in grams
    num_of_days = 0
    comodity = ""

    choice = int(input("Choose the comodity to measure:-\n1. Salt\n2. Oil\n3.Daal"))
    
    if choice == 1:
        comodity = "salt"
    
    if choice == 2:
        comodity = "oil"
        unit = 
    
    if choice == 3:
        pass
        
    num_of_benifitiaries = input("Enter number of benifitiary students: ")
    num_of_benifitiaries = 0
    food_amount = 0
    grams_of_comodity = 0
    num_of_days = 0

    num_of_benifitiaries = int(input("Enter number of benifitiary students: "))
    food_amount = int(input("Enter amount of %s in reserve(KG): "%(comodity))
    comodity_amount = int(input("Enter amount of %s(Grams): "%(comodity)))
    num_of_days = int(input("Enter number of days: "))

    calculator(num_of_benifitiaries, food_amount, comodity_amount, num_of_days, comodity)


