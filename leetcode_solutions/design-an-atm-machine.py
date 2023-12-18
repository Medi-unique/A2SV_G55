from typing import List

class ATM:
    def __init__(self):
        self.banknotes = [20, 50, 100, 200, 500]
        self.amount = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.amount[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrawal = [0, 0, 0, 0, 0]

        for i in range(len(self.banknotes) - 1, -1, -1):
            if amount >= self.banknotes[i] and self.amount[i] > 0:
                num_banknotes_to_withdraw = min(amount // self.banknotes[i], self.amount[i])
                withdrawal[i] += num_banknotes_to_withdraw
                self.amount[i] -= num_banknotes_to_withdraw
                amount -= num_banknotes_to_withdraw * self.banknotes[i]

        if amount == 0:
            return withdrawal
        else:
            # Roll back the changes made to the banknotes count
            for i in range(len(self.banknotes)):
                self.amount[i] += withdrawal[i]
            return [-1]

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)