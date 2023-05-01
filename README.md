# EscapeRoom
A simple graphical game built only with python. 

- Used package: graphics.py

## Running the game

In order to run the project, first clone the repo:
```
git clone https://github.com/KTsula/EscapeRoom-in-Python.git
```
Open the folder in any code editor. I would suggest pycharm or VScode.

The code has been tested and definitely works for Python 3.9 version.

To play the game run the file
```
main.py
```

## The game UI:
<img width="448" alt="Screenshot 2023-05-01 154841" src="https://user-images.githubusercontent.com/64359365/235461716-1578db78-7ccf-4c7a-af27-6cb71b60c3e3.png">
<img width="448" alt="Screenshot 2023-05-01 154912" src="https://user-images.githubusercontent.com/64359365/235461706-20a12156-dbfa-4f75-9076-8f5ff52f86fe.png">
<img width="449" alt="Screenshot 2023-05-01 155008" src="https://user-images.githubusercontent.com/64359365/235461703-8750036a-145c-4856-afb5-0bb5cae06825.png">
<img width="449" alt="Screenshot 2023-05-01 155043" src="https://user-images.githubusercontent.com/64359365/235461698-0bd04391-11b2-42ff-864a-5813b9df12ac.png">
<img width="448" alt="Screenshot 2023-05-01 155147" src="https://user-images.githubusercontent.com/64359365/235461697-a09d45e0-a34d-4765-a901-0b45fce1fbb7.png">
<img width="449" alt="Screenshot 2023-05-01 155241" src="https://user-images.githubusercontent.com/64359365/235461694-fc95ee52-93f0-4d84-8689-535cb0ae0d2e.png">
<img width="451" alt="Screenshot 2023-05-01 155326" src="https://user-images.githubusercontent.com/64359365/235461688-54e94795-59bd-4613-841b-1f829972737c.png">

## Logic behind
In order to activate a game execute main.py - > main.py activates play.py - > play.py is a function that organizes switch from one room to another and checks if the conditions for continuing a game are satisfied.

room*.py -s are functions for different rooms.

Inventory is constant in all rooms and is sent to one another as a list.
