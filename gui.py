import tkinter as tk
from tkinter import ttk
from password_analyzer import PasswordAnalyzer
import re

class ModernTheme:
    # Color scheme
    BG_COLOR = "#f0f2f5"
    CARD_BG = "#ffffff"
    TEXT_COLOR = "#1a1a1a"
    ACCENT_COLOR = "#2196f3"
    SUCCESS_COLOR = "#4caf50"
    WARNING_COLOR = "#ff9800"
    ERROR_COLOR = "#f44336"
    
    # Fonts
    TITLE_FONT = ("Helvetica", 24, "bold")
    HEADER_FONT = ("Helvetica", 14, "bold")
    NORMAL_FONT = ("Helvetica", 12)
    
    # Padding and spacing
    PADDING = 20
    SPACING = 10

class ModernCard(tk.Frame):
    def __init__(self, parent, title, **kwargs):
        super().__init__(parent, bg=ModernTheme.CARD_BG, **kwargs)
        
        # Title
        title_label = tk.Label(
            self,
            text=title,
            font=ModernTheme.HEADER_FONT,
            bg=ModernTheme.CARD_BG,
            fg=ModernTheme.TEXT_COLOR
        )
        title_label.pack(anchor='w', padx=ModernTheme.PADDING, pady=(ModernTheme.PADDING, ModernTheme.SPACING))
        
        # Content frame
        self.content = tk.Frame(self, bg=ModernTheme.CARD_BG)
        self.content.pack(fill='x', padx=ModernTheme.PADDING, pady=(0, ModernTheme.PADDING))

class PasswordStrengthGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Analyzer")
        self.root.geometry("800x600")
        self.root.configure(bg=ModernTheme.BG_COLOR)
        
        # Initialize password analyzer
        self.analyzer = PasswordAnalyzer()
        
        # Create main container with scrollbar
        self.main_container = tk.Frame(root, bg=ModernTheme.BG_COLOR)
        self.main_container.pack(fill='both', expand=True)
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self.main_container, bg=ModernTheme.BG_COLOR, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=ModernTheme.BG_COLOR)
        
        # Configure scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=760)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack scrollbar and canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Create main frame inside scrollable frame
        self.main_frame = tk.Frame(self.scrollable_frame, bg=ModernTheme.BG_COLOR)
        self.main_frame.pack(fill='both', expand=True, padx=ModernTheme.PADDING, pady=ModernTheme.PADDING)
        
        # Title
        title_label = tk.Label(
            self.main_frame,
            text="Password Strength Analyzer",
            font=ModernTheme.TITLE_FONT,
            bg=ModernTheme.BG_COLOR,
            fg=ModernTheme.TEXT_COLOR
        )
        title_label.pack(pady=(0, ModernTheme.PADDING))
        
        # Password input card
        input_card = ModernCard(self.main_frame, "Enter Password")
        input_card.pack(fill='x', pady=(0, ModernTheme.PADDING))
        
        # Password entry with modern styling
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            input_card.content,
            textvariable=self.password_var,
            show="•",
            font=ModernTheme.NORMAL_FONT,
            width=40,
            bg=ModernTheme.CARD_BG,
            fg=ModernTheme.TEXT_COLOR
        )
        self.password_entry.pack(fill='x', pady=ModernTheme.SPACING)
        
        # Bind password changes
        self.password_var.trace('w', self.on_password_change)
        
        # Strength indicator card
        self.strength_card = ModernCard(self.main_frame, "Strength Analysis")
        self.strength_card.pack(fill='x', pady=(0, ModernTheme.PADDING))
        
        # Strength category with larger font
        self.category_label = tk.Label(
            self.strength_card.content,
            text="",
            font=("Helvetica", 20, "bold"),
            bg=ModernTheme.CARD_BG,
            fg=ModernTheme.TEXT_COLOR
        )
        self.category_label.pack(pady=ModernTheme.SPACING)
        
        # Modern progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.strength_card.content,
            variable=self.progress_var,
            maximum=100,
            mode='determinate',
            style='Modern.Horizontal.TProgressbar'
        )
        self.progress_bar.pack(fill='x', pady=ModernTheme.SPACING)
        
        # Score label
        self.score_label = tk.Label(
            self.strength_card.content,
            text="",
            font=ModernTheme.NORMAL_FONT,
            bg=ModernTheme.CARD_BG,
            fg=ModernTheme.TEXT_COLOR
        )
        self.score_label.pack(pady=ModernTheme.SPACING)
        
        # Details card
        details_card = ModernCard(self.main_frame, "Password Details")
        details_card.pack(fill='x', pady=(0, ModernTheme.PADDING))
        
        # Create grid for details
        details_grid = tk.Frame(details_card.content, bg=ModernTheme.CARD_BG)
        details_grid.pack(fill='x')
        
        # Entropy
        tk.Label(details_grid, text="Entropy:", font=ModernTheme.NORMAL_FONT, bg=ModernTheme.CARD_BG, fg=ModernTheme.TEXT_COLOR).grid(row=0, column=0, sticky='w', pady=ModernTheme.SPACING)
        self.entropy_label = tk.Label(details_grid, text="", font=ModernTheme.NORMAL_FONT, bg=ModernTheme.CARD_BG, fg=ModernTheme.TEXT_COLOR)
        self.entropy_label.grid(row=0, column=1, sticky='w', pady=ModernTheme.SPACING)
        
        # Length
        tk.Label(details_grid, text="Length:", font=ModernTheme.NORMAL_FONT, bg=ModernTheme.CARD_BG, fg=ModernTheme.TEXT_COLOR).grid(row=1, column=0, sticky='w', pady=ModernTheme.SPACING)
        self.length_label = tk.Label(details_grid, text="", font=ModernTheme.NORMAL_FONT, bg=ModernTheme.CARD_BG, fg=ModernTheme.TEXT_COLOR)
        self.length_label.grid(row=1, column=1, sticky='w', pady=ModernTheme.SPACING)
        
        # Requirements card
        requirements_card = ModernCard(self.main_frame, "Password Requirements")
        requirements_card.pack(fill='x', pady=(0, ModernTheme.PADDING))
        
        # Create grid for requirements
        self.requirement_labels = {}
        requirements = [
            ('min_length', 'Minimum Length (8+)'),
            ('has_lower', 'Contains Lowercase'),
            ('has_upper', 'Contains Uppercase'),
            ('has_digit', 'Contains Digit'),
            ('has_symbol', 'Contains Symbol'),
            ('no_repeats', 'No Repeating Characters'),
            ('no_common_patterns', 'No Common Patterns')
        ]
        
        for i, (key, text) in enumerate(requirements):
            tk.Label(requirements_card.content, text=text, font=ModernTheme.NORMAL_FONT, bg=ModernTheme.CARD_BG, fg=ModernTheme.TEXT_COLOR).grid(
                row=i, column=0, sticky='w', pady=ModernTheme.SPACING
            )
            label = tk.Label(requirements_card.content, text="", font=ModernTheme.NORMAL_FONT, bg=ModernTheme.CARD_BG, fg=ModernTheme.TEXT_COLOR)
            label.grid(row=i, column=1, sticky='w', pady=ModernTheme.SPACING)
            self.requirement_labels[key] = label

    def setup_styles(self):
        """Configure custom styles for the GUI."""
        style = ttk.Style()
        
        # Configure modern progress bar
        style.configure(
            'Modern.Horizontal.TProgressbar',
            troughcolor=ModernTheme.BG_COLOR,
            background=ModernTheme.ACCENT_COLOR,
            thickness=10
        )

    def on_password_change(self, *args):
        """Handle password changes and update analysis."""
        password = self.password_var.get()
        analysis = self.analyzer.analyze_password(password)
        
        # Update strength category and color
        self.category_label.config(
            text=analysis['category'],
            fg=analysis['color']
        )
        
        # Update score
        self.score_label.config(text=f"Score: {analysis['score']:.1f}/100")
        self.progress_var.set(analysis['score'])
        
        # Update details
        self.entropy_label.config(text=f"{analysis['entropy']:.2f} bits")
        self.length_label.config(text=str(analysis['length']))
        
        # Update requirements with modern checkmarks
        for key, label in self.requirement_labels.items():
            if key in analysis['patterns']:
                value = analysis['patterns'][key]
            elif key in analysis['char_sets']:
                value = analysis['char_sets'][key]
            else:
                continue
                
            label.config(
                text="✓" if value else "✗",
                fg=ModernTheme.SUCCESS_COLOR if value else ModernTheme.ERROR_COLOR
            )

def main():
    root = tk.Tk()
    app = PasswordStrengthGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 