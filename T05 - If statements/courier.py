print("Hi! Welcome to Pass The Parcel cost calculator. Here we'll calculate the full price of purchasing and sending your parcel of choice.")
package_price = float(input("How much does your parcel cost, in rand?"))
package_distance = float(input("How far does the parcel need to travel, in km?"))

while True:

    package_transport = input("Do you want to transport the parcel via: \n A) Air. B) Freight. [A/B]? : ")

    if package_transport == "A":
        package_cost_per_km = 0.36
        break
    elif package_transport == "B":
        package_cost_per_km = 0.25
        break
    else:
        print('Type a letter A-B')
        continue

print("Please type 'True' or 'False' in response to the following queries.")
package_fullInsurance = input("Limited insurance is included on all deliveries. Would you like to pay an extra R25 for full insurance?")
package_gift = input("Is this parcel a gift?")
package_priority = input("Would you like to pay an additional R80 for priority delivery?")

package_total_cost = package_price + (package_cost_per_km*package_distance)

if package_fullInsurance:
    package_total_cost = package_total_cost + 50
else:
    package_total_cost = package_total_cost + 25

if package_gift:
    package_total_cost = package_total_cost + 15
else:
    package_total_cost = package_total_cost + 0

if package_priority:
    package_total_cost = package_total_cost + 100
else:
    package_total_cost = package_total_cost + 20

print("The total cost of your parcel, including postage and packing, is R" + str(package_total_cost))