import random

# Function to simulate dice rolls and calculate probabilities
def roll_dice_simulator(rolls):
    # Initialize a dictionary to store the frequency of each possible sum (2 to 12)
    frequency = {i: 0 for i in range(2, 13)}

    # Simulate rolling two dice the specified number of times
    for _ in range(rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        frequency[total] += 1

    # Print the results
    print("Sum\tFrequency\tProbability")
    for sum_value, count in frequency.items():
        probability = count / rolls
        print(f"{sum_value}\t{count}\t\t{probability:.2f}")

# Main function to ask for user input and run the simulation
def main():
    rolls = int(input("Enter the number of dice rolls: "))
    roll_dice_simulator(rolls)

if __name__ == "__main__":
    main()