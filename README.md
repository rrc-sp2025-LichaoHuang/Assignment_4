## [Assignment_4]

[Describe the tools and techniques you'll use to improve the quality of the PiXELL Transaction Report.]


## Code Modification 1

- Added error handling when the the import data can not be stored as a float.

## Code Modification 2

- Identify those invalid data and collect them in a list.

## Code Modification 3

- In the test, average_transaction_amount = total_transaction_amount / transaction_counter does not work because the divisor is 0，And the dividend is also 0.

- The cause of this bug is in line 75. In this if loop, the new customer ID will only be created, and no deposit or withdrawal will be executed. Therefore, add the execution of deposit or withdraw to the script for creating a new account.

- After the repair is completed, you need to assign a value to transaction_counter, so assign a value to transaction_counter in line 121.

## Code Modification 4

- After adding the second set of data, the average output is found to be 3750, instead of the expected 7500.

- Lines 121 and 122 had indentation errors, which were corrected to get the correct output(7500).

## Code Modification 5

- During the test, I found that the balance of some accounts was incorrect.

- After testing, it was found that the spelling of withdraw was wrong. After correction, the correct balance was obtained.