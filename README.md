# Password Strength Analyzer

A professional password strength analyzer application built with Python and tkinter. This tool provides real-time analysis of password strength based on various criteria including entropy, character diversity, and pattern matching.

## Features

- Real-time password strength analysis
- Visual strength indicator with color coding
- Comprehensive password requirements checking
- Entropy calculation using Shannon entropy formula
- Character set diversity analysis
- Pattern matching and validation
- Modern and user-friendly GUI

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- numpy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/password-strength-analyzer.git
cd password-strength-analyzer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python gui.py
```

## Password Analysis Criteria

The password strength is evaluated based on the following criteria:

1. **Length**: Minimum 8 characters
2. **Character Diversity**:
   - Lowercase letters
   - Uppercase letters
   - Digits
   - Special symbols
3. **Pattern Analysis**:
   - No repeating characters
   - No common patterns (e.g., "123", "abc", "qwerty")
4. **Entropy**: Calculated using Shannon entropy formula

## Strength Categories

- Very Weak (0-30): Red
- Weak (30-50): Orange
- Moderate (50-70): Yellow
- Strong (70-85): Green
- Very Strong (85-100): Dark Green

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 