# 🎮 Tic Tac Toe - CustomTkinter Edition

A modern **Tic Tac Toe** game with a beautiful dark/light theme toggle, built using **Python** and **CustomTkinter**.

---

## 📁 Repository

Clone this repository using:

```bash
git clone https://github.com/GITWithAkshay/tic-tac-toe-customtkinter.git
cd tic-tac-toe-customtkinter
```

---

## 🧰 Requirements

* Python 3.8 or higher
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* [Pillow](https://pypi.org/project/Pillow/) (if you add images/icons)

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
python tic_tac_toe.py
```

---

## 🕹 Features

✅ **Classic 2-player mode** (local)
✅ **Modern UI with dark and light theme toggle**
✅ **Responsive button grid layout**
✅ **Turn indicator and winner/draw announcements**
✅ **"New Game" reset functionality**
✅ **Highlighting of winning cells**
✅ **Auto-switch between X and O**

---

## 🌗 Theme Support

* ☀️ Light mode and 🌙 Dark mode toggle
* Theme toggle button available on the top-right corner
* Auto-updates text and button colors accordingly

---

## 🧠 Game Logic

* 3x3 grid managed as a 2D list (`self.board`)
* Checks for:

  * Row-wise, column-wise, and diagonal wins
  * Draw when all cells are filled
* Highlights winning cells in gold (`#FFD700`)
* Turn alternates between Player X and O

---

## 🔄 Resetting the Game

Click the **“New Game”** button to:

* Clear the board
* Reset all button colors and text
* Re-enable interaction
* Reset the game state and turn tracker

---

## 🧪 Example Output

```text
Player X's Turn
[ X ][   ][   ]
[   ][ X ][   ]
[   ][   ][ X ]

=> Player X wins!
```

---

## 📸 Screenshots

![image alt](https://github.com/GITWithAkshay/PRODIGY_AD_04/blob/51c157dd59a79eb5f505be11252e4114b0aa7f5e/Screenshot%20(190).png)
![image alt](https://github.com/GITWithAkshay/PRODIGY_AD_04/blob/51c157dd59a79eb5f505be11252e4114b0aa7f5e/Screenshot%20(191).png)
![image alt](https://github.com/GITWithAkshay/PRODIGY_AD_04/blob/51c157dd59a79eb5f505be11252e4114b0aa7f5e/Screenshot%20(193).png)
![image alt](https://github.com/GITWithAkshay/PRODIGY_AD_04/blob/51c157dd59a79eb5f505be11252e4114b0aa7f5e/Screenshot%20(195).png)

---

## 📂 File Structure

```
tic-tac-toe-customtkinter/
│
├── tic_tac_toe.py           # Main application file
├── README.md                # Project documentation
└── requirements.txt         # (Optional) Python dependencies list
```

---

## 🙏 Acknowledgement

* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky — for making modern tkinter UIs possible.
* The Python community — for continuous support and open-source contributions.

---

## 📜 License

Feel free to use, modify, and distribute.

---
