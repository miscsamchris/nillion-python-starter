# Rock, Paper, Scissors Game with Nillion

This project is a simple command-line Rock, Paper, Scissors game written in Python. The player can choose rock, paper, or scissors by entering a number (1, 2, or 3). The computer randomly selects its choice, and the winner is determined based on the rules of the game. This version leverages Nillion, a decentralized computing network, for secure and efficient data management.

## Features

- Player 1 & 2 can choose rock, paper, or scissors using numeric input.
- The game determines the winner and displays the result.
- Includes ASCII art for the title and choices.
- Utilizes Nillion for secure and decentralized data management.

## Prerequisites

- Python 3.x
- Nillion SDK 

## How to Run

1. Clone the repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the scripts.
```bash
cd ./nillion-python-starter/blob/main/examples_and_tutorials/my_first_program/
 ```

### Step 1

- Alice creates and stores program in the network and starts the game.
- Alice shares the user id and the resulting program id with Bob.

Run the command to perform step 1.

```bash
python3 step_1.py
```

### Step 2

- Bob stores the choice in the network as secrets. Each secret is stored with
  - **bindings** to the Rock Paper Scissors (my_first_program)  program id
  - **permissions** so Alice can compute using the secret
- Bob shares thei party_id and secret store_id with Alice.

The script will provide the command to perform step 2.

```bash
python3 step_2.py --user_id_1 {user_id} --program_id {program_id}
```

### Step 3

- Alice runs Rock Paper Scissor (my_first_program) program computation using Bob's choice and provide a choice as a secret at computation time.
- Alice receives the output result of the program.

The script will provide the command to perform step 3.

```bash
python3 step_3.py --program_id {program_id} --party_ids_to_store_ids {party_ids_to_store_ids}
```


## Game Rules

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.

## Sample Output

```        

1 = Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

2 = Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

3 = Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

```

## Nillion Integration
Nillion is a decentralized computing network that secures high-value data without relying on blockchain technology. Instead, it uses innovative cryptographic methods, particularly a process called "Nil Message Compute," developed by cryptography professor Miguel de Vega. This network allows data to be stored and computed on securely without the need for decryption, enhancing both security and efficiency.

For more information on Nillion, you can visit the [Nillion website](https://nillion.com) or refer to the [Developer Docs](https://docs.nillion.com/quickstart).

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the game.

## License
This project is licensed under the MIT License.
