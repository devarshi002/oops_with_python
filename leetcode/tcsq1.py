class ATMMachine:
    def __init__(self):
        self.results = []

    def process_test_case(self, N, K, A):
        result = []
        for amount in A:
            if K >= amount:
                result.append('1')  # Withdrawal successful
                K -= amount  # Deduct the withdrawn amount
            else:
                result.append('0')  # Withdrawal failed
        self.results.append(''.join(result))

    def run(self):
        # Read the number of test cases
        T = int(input("Enter the number of test cases: "))
        for _ in range(T):
            # Read N (number of people) and K (initial ATM balance)
            N, K = map(int, input("Enter N (number of people) and K (ATM balance): ").split())
            # Read the array A (withdrawal requests)
            A = list(map(int, input(f"Enter the withdrawal requests for {N} people: ").split()))
            self.process_test_case(N, K, A)

        # Print all results, each on a new line
        print("\n".join(self.results))


# Instantiate and run the ATM machine
atm = ATMMachine()
atm.run()
