import customtkinter as ctk

class TicTacToeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("400x700")
        self.resizable(True, True)
        
        # Set dark theme as default
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#1a1a1a")
        
        # Initialize variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.theme_mode = "dark"
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Tic Tac Toe",
            font=("Arial", 32, "bold"),
            text_color="#FFFFFF"
        )
        self.title_label.grid(row=0, column=0, pady=(30, 10))
        
        # Theme toggle button
        self.theme_button = ctk.CTkButton(
            self,
            text="☀️",
            width=50,
            height=35,
            font=("Arial", 18),
            command=self.toggle_theme
        )
        self.theme_button.place(relx=0.95, rely=0.05, anchor="ne")
        
        # Player turn indicator
        self.turn_label = ctk.CTkLabel(
            self,
            text=f"Player {self.current_player}'s Turn",
            font=("Arial", 18, "bold"),
            text_color="#00FF00"
        )
        self.turn_label.grid(row=1, column=0, pady=10)
        
        # Game board frame
        board_frame = ctk.CTkFrame(self, fg_color="transparent")
        board_frame.grid(row=2, column=0, pady=20, sticky="nsew", padx=20)
        
        # Configure board grid
        for i in range(3):
            board_frame.grid_columnconfigure(i, weight=1)
            board_frame.grid_rowconfigure(i, weight=1)
        
        # Create game buttons
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = ctk.CTkButton(
                    board_frame,
                    text="",
                    font=("Arial", 48, "bold"),
                    width=120,
                    height=120,
                    command=lambda row=i, col=j: self.button_click(row, col),
                    fg_color="#2d2d2d",
                    hover_color="#3d3d3d",
                    corner_radius=10
                )
                button.grid(row=i, column=j, padx=8, pady=8, sticky="nsew")
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        
        # Status label
        self.status_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 16),
            text_color="#FFFFFF"
        )
        self.status_label.grid(row=3, column=0, pady=10)
        
        # Reset button
        self.reset_button = ctk.CTkButton(
            self,
            text="New Game",
            font=("Arial", 16, "bold"),
            width=150,
            height=40,
            command=self.reset_game,
            fg_color="#dc3545",
            hover_color="#c82333"
        )
        self.reset_button.grid(row=4, column=0, pady=20)
        
    def button_click(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            # Place the symbol
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(
                text=self.current_player,
                text_color="#FF6B6B" if self.current_player == "X" else "#4ECDC4"
            )
            
            # Check for win
            if self.check_winner(row, col):
                self.game_over = True
                self.status_label.configure(
                    text=f"Player {self.current_player} wins!",
                    text_color="#00FF00"
                )
                self.turn_label.configure(text="")
                return
            
            # Check for draw
            if self.check_draw():
                self.game_over = True
                self.status_label.configure(
                    text="It's a draw!",
                    text_color="#FFA500"
                )
                self.turn_label.configure(text="")
                return
            
            # Switch player
            self.current_player = "O" if self.current_player == "X" else "X"
            self.turn_label.configure(text=f"Player {self.current_player}'s Turn")
            
    def check_winner(self, row, col):
        symbol = self.board[row][col]
        
        # Check row
        if all(self.board[row][i] == symbol for i in range(3)):
            self.highlight_winning_cells([(row, i) for i in range(3)])
            return True
        
        # Check column
        if all(self.board[i][col] == symbol for i in range(3)):
            self.highlight_winning_cells([(i, col) for i in range(3)])
            return True
        
        # Check diagonal (top-left to bottom-right)
        if row == col and all(self.board[i][i] == symbol for i in range(3)):
            self.highlight_winning_cells([(i, i) for i in range(3)])
            return True
        
        # Check diagonal (top-right to bottom-left)
        if row + col == 2 and all(self.board[i][2-i] == symbol for i in range(3)):
            self.highlight_winning_cells([(i, 2-i) for i in range(3)])
            return True
        
        return False
        
    def highlight_winning_cells(self, winning_cells):
        for row, col in winning_cells:
            self.buttons[row][col].configure(
                fg_color="#FFD700",  # Gold color for winning cells
                text_color="#000000"
            )
            
    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))
        
    def reset_game(self):
        # Reset board
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        
        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(
                    text="",
                    fg_color="#2d2d2d",
                    text_color="#FFFFFF"
                )
        
        # Reset labels
        self.turn_label.configure(text=f"Player {self.current_player}'s Turn")
        self.status_label.configure(text="")
        
    def toggle_theme(self):
        if self.theme_mode == "dark":
            self.theme_mode = "light"
            self.theme_button.configure(text="🌙")
            ctk.set_appearance_mode("light")
            self.configure(fg_color="#f8f9fa")
            self.title_label.configure(text_color="#000000")
            self.turn_label.configure(text_color="#000000")
            self.status_label.configure(text_color="#000000")
            
            # Update button colors for light theme
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j].cget("text") == "":
                        self.buttons[i][j].configure(
                            fg_color="#e9ecef",
                            hover_color="#dee2e6"
                        )
        else:
            self.theme_mode = "dark"
            self.theme_button.configure(text="☀️")
            ctk.set_appearance_mode("dark")
            self.configure(fg_color="#1a1a1a")
            self.title_label.configure(text_color="#FFFFFF")
            self.turn_label.configure(text_color="#00FF00")
            self.status_label.configure(text_color="#FFFFFF")
            
            # Update button colors for dark theme
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j].cget("text") == "":
                        self.buttons[i][j].configure(
                            fg_color="#2d2d2d",
                            hover_color="#3d3d3d"
                        )

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = TicTacToeApp()
    app.protocol("WM_DELETE_WINDOW", app.quit)
    app.mainloop() 
