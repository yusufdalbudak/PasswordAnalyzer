# Password Strength Analyzer

A modern Python application that analyzes password strength with a graphical user interface.

## Features

- Real-time password strength analysis
- Visual strength indicator
- Entropy calculation
- Character set analysis
- Pattern detection
- Modern GUI with scrollable interface

## Requirements

- Python 3.6+
- tkinter (usually comes with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yusufdalbudak/PasswordAnalyzer.git
cd PasswordAnalyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python gui.py
```

## Password Analysis Criteria

The analyzer checks for:
- Password length (minimum 8 characters)
- Character diversity (lowercase, uppercase, numbers, symbols)
- Common patterns
- Repeating characters
- Shannon entropy

## Strength Categories

- Very Weak (0-30): Red
- Weak (30-50): Orange
- Moderate (50-70): Yellow
- Strong (70-85): Green
- Very Strong (85-100): Dark Green

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details. 