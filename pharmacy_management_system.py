
d1 = {'dolo': [50, 5],
    'aspirin': [90, 15],
    'amoxicillin': [200, 20]}
choice='y'
while choice=='y' :
    print("\n====== APOLLO PHARMACY ======")
    print("1. Add Medicine")
    print("2. Billing")
    print("3. View Stock")
    print("4. Exit")

    ch = input("Enter your choice (1-4): ")

    # ---------------- ADD MEDICINE ----------------
    if ch == "1":
        medicine = input("Enter medicine name: ").lower()
        qnt = int(input("Enter number of sheets: "))

        if medicine in d1:
            d1[medicine][1] += qnt
            print("Medicine quantity updated successfully")
        else:
            price = int(input("Enter price per sheet: "))
            d1[medicine] = [price, qnt]
            print("New medicine added successfully")

        print("Updated Stock:", d1)

    # ---------------- BILLING ----------------
    elif ch == "2":
        medicine = input("Enter medicine name: ").lower()

        if medicine in d1:
            price = d1[medicine][0]
            stock = d1[medicine][1]

            print("Cost per sheet:", price)
            qnt = int(input("Enter number of sheets: "))

            if qnt <= stock:
                d1[medicine][1] -= qnt
                bill = price * qnt

                print("\n------ APOLLO PHARMACY BILL ------")
                print("Medicine:", medicine)
                print("Quantity:", qnt)
                print("Price per sheet:", price)
                print("Total Bill:", bill)
                print("----------------------------------")

                # Low stock alert
                if d1[medicine][1] < 5:
                    print(" Low Stock Alert! Remaining:", d1[medicine][1])

            else:
                print("Sorry! Only", stock, "sheets available")

        else:
            print("Medicine not available")

    # ---------------- VIEW STOCK ----------------
    elif ch == "3":
        print("\n------ CURRENT STOCK ------")
        for name, details in d1.items():
            print("Medicine:", name)
            print("Price:", details[0])
            print("Stock:", details[1])
            print("----------------------------")

    # ---------------- EXIT ----------------
    elif ch == "4":
        print("Thank you for visiting Apollo Pharmacy")
        break

    else:
        print("Please enter correct choice")
    choice=input("do you want to continue say [y/n] :")
print("thank you")




