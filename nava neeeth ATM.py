class ATM:
    def __init__(self, pin, balance=0): 
        self.correct_pin = pin
        self.balance = balance
        self.transactions = []
        self.language = "English"

    def select_language(self):
        print("भाषा चुनें / Select Language:")
        print("1. English")
        print("2. हिन्दी")
        lang = input("Enter your choice (1 or 2): ")
        if lang == "1":
            self.language = "English"
            print("Language set to English.\n")
        elif lang == "2":
            self.language = "Hindi"
            print("भाषा हिन्दी में सेट की गई है।\n")
        else:
            print("Invalid choice. Defaulting to English.\n")

    def get_input(self, prompt_en, prompt_hi=""):
        return input(prompt_hi if self.language == "Hindi" else prompt_en)

    def authenticate(self):
        pin_input = self.get_input("Enter your PIN: ", "अपना पिन दर्ज करें: ")
        if pin_input == self.correct_pin:
            return True
        else:
            print("गलत पिन।" if self.language == "Hindi" else "Invalid PIN.")
            return False

    def balance_check(self):
        if self.language == "Hindi":
            print(f"आपका बैलेंस है: ₹{self.balance}")
        else:
            print(f"Your balance is: ₹{self.balance}")

    def deposit(self):
        amount = float(self.get_input("Enter amount to deposit: ", "जमा करने की राशि दर्ज करें: "))
        if amount <= 0:
            print("अमान्य राशि।" if self.language == "Hindi" else "Invalid deposit amount.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print("जमा सफल।" if self.language == "Hindi" else "Deposit successful.")

    def withdraw(self):
        if self.language == "Hindi":
            print("खाता प्रकार चुनें:")
            print("1. करंट खाता")
            print("2. बचत खाता")
        else:
            print("Select Account Type:")
            print("1. Current Account")
            print("2. Savings Account")

        acc_type = self.get_input("Enter choice (1 or 2): ", "चयन दर्ज करें (1 या 2): ")

        if acc_type not in ['1', '2']:
            print("अमान्य खाता प्रकार।" if self.language == "Hindi" else "Invalid account type.")
            return

        amount = float(self.get_input("Enter amount to withdraw: ", "निकासी राशि दर्ज करें: "))
        if amount <= 0:
            print("अमान्य राशि।" if self.language == "Hindi" else "Invalid withdrawal amount.")
        elif amount > self.balance:
            print("पर्याप्त शेष राशि नहीं है।" if self.language == "Hindi" else "Insufficient funds.")
        else:
            self.balance -= amount
            if self.language == "Hindi":
                acc_name = "करंट खाता" if acc_type == '1' else "बचत खाता"
                print(f"{acc_name} से ₹{amount} की निकासी सफल रही।")
            else:
                acc_name = "Current Account" if acc_type == '1' else "Savings Account"
                print(f"₹{amount} withdrawn from {acc_name} successfully.")
            self.transactions.append(f"Withdrew ₹{amount} from {acc_name}")

    def change_pin(self):
        old_pin = self.get_input("Enter current PIN: ", "वर्तमान पिन दर्ज करें: ")
        if old_pin != self.correct_pin:
            print("गलत पिन।" if self.language == "Hindi" else "Incorrect PIN.")
            return
        new_pin = self.get_input("Enter new PIN: ", "नया पिन दर्ज करें: ")
        confirm_pin = self.get_input("Confirm new PIN: ", "नया पिन फिर से दर्ज करें: ")
        if new_pin == confirm_pin:
            self.correct_pin = new_pin
            print("पिन सफलतापूर्वक बदला गया।" if self.language == "Hindi" else "PIN changed successfully.")
        else:
            print("पिन मेल नहीं खा रहे।" if self.language == "Hindi" else "PINs do not match. Try again.")

    def show_transactions(self):
        if not self.transactions:
            print("कोई लेनदेन नहीं।" if self.language == "Hindi" else "No transactions yet.")
        else:
            print("लेन-देन विवरण:" if self.language == "Hindi" else "Transaction History:")
            for t in self.transactions:
                print(" -", t)

    def run(self):
        self.select_language()

        if not self.authenticate():
            return

        while True:
            if self.language == "Hindi":
                print("\n--- एटीएम मेनू ---")
                print("1. बैलेंस जांचें")
                print("2. जमा करें")
                print("3. निकासी करें")
                print("4. पिन बदलें")
                print("5. लेन-देन इतिहास")
                print("6. बाहर निकलें")
            else:
                print("\n--- ATM Menu ---")
                print("1. Balance Check")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Change PIN")
                print("5. Transaction History")
                print("6. Exit")

            choice = self.get_input("Enter your choice: ", "अपना विकल्प दर्ज करें: ")

            if choice == '1':
                self.balance_check()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.show_transactions()
            elif choice == '6':
                print("धन्यवाद!" if self.language == "Hindi" else "Thank you for using the ATM.")
                break
            else:
                print("अमान्य विकल्प।" if self.language == "Hindi" else "Invalid option. Try again.")
atm = ATM(pin="1234", balance=10000)
atm.run()
