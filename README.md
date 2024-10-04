# Vehicle Rental Pricing Script

This script calculates the total rental price of a vehicle based on the selected vehicle type, rental duration, and additional features. It also applies discounts depending on the rental duration.

## Features

- Allows users to select from four types of vehicles with different daily rates.
- Calculates a discount based on the rental duration:
  - No discount for a 1-day rental.
  - 4% discount for a 2-3 day rental.
  - 10% discount for a 4-7 day rental.
  - 20% discount for a rental of 8 days or more.
- Additional services (GPS, Mobile Wi-Fi, Child Seat, etc.) can be selected to add to the total cost.
- Final price is displayed with discounts and additional services applied.

## Vehicle Rates per Day

- **Compact**: $25/day
- **Sedan**: $35/day
- **SUV**: $50/day
- **Luxury**: $60/day

## Discounts by Rental Duration

| Duration       | Discount   |
|----------------|------------|
| 1 day          | No discount|
| 2-3 days       | 4%         |
| 4-7 days       | 10%        |
| 8+ days        | 20%        |

## Additional Features & Services

| Feature                      | Rate (per day) |
|------------------------------|----------------|
| GPS Navigation                | $5             |
| Mobile Wi-Fi                  | $8             |
| Child Seat                    | $2             |
| Toll Pass                     | $4.50          |
| Roadside Assistance Plus       | $5             |

## How to Use the Script

1. **Run the script**.
2. **Choose a vehicle type**:
   - Select from Compact, Sedan, SUV, or Luxury.
3. **Select a rental duration**:
   - Specify how long the rental will last in days.
   - The system applies discounts automatically based on duration.
4. **Select additional features** (optional):
   - Add extra services like GPS, Wi-Fi, Child Seat, etc.
5. **Final Output**:
   - The script will display the final price after applying the duration discount and additional features.

## Example

```bash
Choose your vehicle type ('1' / '2' / '3' / '4'): 1
Choose your rental duration ('1' / '2' / '3' / '4'): 2
How long is your rental (answer in days): 3
Choose additional features ('1' / '2' / '3' / '4' / '5'): 1

Your rental Type is compact, Your rental duration is 3 days, and your final price is 72.0 dollars
