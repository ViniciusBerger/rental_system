rate = 0
duration_discount = 0
features_value = 0

# Show Rental Rates per day
print("--"*30)
print("Vehicle type // price")
print("--"*30)

print("[1] Compact       $25")
print("[2] Sedan         $35")
print("[3] SUV           $50")
print("[4] Luxury        $60")



# adding value to rate
while True:
    vehicle_type = input("Choose your option ('1' / '2' / '3' / '4'): ")
    # Handling error might the user enter a different imput
    while not vehicle_type.isnumeric():
        vehicle_type = input("Choose your option ('1' / '2' / '3' / '4'): ") 
    match int(vehicle_type):
        case 1: 
            rate = 25; rental_type = "compact" 
            break
        case 2: 
            rate = 35; rental_type = "Sedan"
            break 
        case 3: 
            rate = 50; rental_type = "Suv"
            break
        case 4: 
            rate = 60; rental_type = "luxury"
            break
        case _:
            print("Invalid type, please report a valid one")
            continue
    


# -----------------------------------------------------------------------------
# Choose the duration of the desired rental
print("--"*30)
print("Choose your rental duration: ")
print("--"*30)

print("Rental Duration  //  Discount (Apply to base rate only)")
print()
print("[1] 1 day                                          none")
print("[2] 2-3 days                                         4%")
print("[3] 4-7 days                                        10%")
print("[4] 8 or more days                                  20%")




# Getting the discount per day based on the rental duration
while True:
    rental_duration = input("Choose your option ('1' / '2' / '3' / '4'): ")
    # Handling error might the user enter a different imput
    while not rental_duration.isnumeric():
        rental_duration = input("Choose your option ('1' / '2' / '3' / '4'): ")


    days = int(input("How long is your rental (answer in days): "))
    match int(rental_duration):
        
        case 1: 
            duration_discount = 0
            break
        case 2: 
            duration_discount = (rate*days)*(4/100)
            break
        case 3: 
            duration_discount = (rate*days)*(10/100) 
            break
        case 4: 
            duration_discount = (rate*days)*(20/100)
            break
        case _:
            print("Invalid type, please select a valid one.")
            continue

print(duration_discount)
    
# -----------------------------------------------------------------------------
# Add adicional services and features
print("--"*30)
print("Adicional services and features // Rate per day")
print("--"*30)
print("[1] GPS navigation                           $5")
print("[2] Mobile Wi-fi                             $8")
print("[3] Child seat                               $2")
print("[4] Toll Pass                             $4.50")
print("[5] Roadside Assistance Plus                 $5")


# Getting rate for features and services per rental
while True:
    features = input("Choose your option ('1' / '2' / '3' / '4' / '5' ): ")
    # Handling error
    while not features.isnumeric():
        features = input("Choose your option ('1' / '2' / '3' / '4' / '5' ): ")
    match int(features):
        case 1: 
            features_value = 5*days
            break
        case 2: 
            features_value = 8*days
            break
        case 3: 
            features_value = 2*days
            break
        case 4: 
            features_value = 4.50*days
            break
        case 5: 
            features_value = 5*days
            break
        case _:
            print("Invalid type, please select a valid one.")
            continue
# -----------------------------------------------------------------------------

# Getting a price after discounts applied by rental duration
price = rate*days
price_after_discount = price - duration_discount


print(" Your rental Type is ", rental_type," Your rental duration is ", days, " and your final price is ", price_after_discount," dolares" )