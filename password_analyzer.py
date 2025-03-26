import re
import math
from typing import Dict, Tuple, List

class PasswordAnalyzer:
    def __init__(self):
        # Define character sets
        self.lowercase = set('abcdefghijklmnopqrstuvwxyz')
        self.uppercase = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.digits = set('0123456789')
        self.symbols = set('!@#$%^&*()_+-=[]{}|;:,.<>?')
        
        # Define regex patterns
        self.patterns = {
            'min_length': r'.{8,}',
            'has_lower': r'[a-z]',
            'has_upper': r'[A-Z]',
            'has_digit': r'\d',
            'has_symbol': r'[!@#$%^&*()_+\-=\[\]{};:,.<>?]',
            'no_repeats': r'(.)\1{2,}',
            'no_common_patterns': r'(123|abc|qwerty|password)'
        }
        
        # Define strength categories and their thresholds
        self.strength_categories = {
            'very_weak': (0, 30),
            'weak': (30, 50),
            'moderate': (50, 70),
            'strong': (70, 85),
            'very_strong': (85, 100)
        }

    def calculate_entropy(self, password: str) -> float:
        """Calculate Shannon entropy for the password."""
        if not password:
            return 0.0
            
        # Count frequency of each character
        char_freq = {}
        for char in password:
            char_freq[char] = char_freq.get(char, 0) + 1
            
        # Calculate entropy
        length = len(password)
        entropy = 0.0
        for freq in char_freq.values():
            prob = freq / length
            entropy -= prob * math.log2(prob)
            
        return entropy

    def analyze_character_sets(self, password: str) -> Dict[str, bool]:
        """Analyze which character sets are present in the password."""
        return {
            'lowercase': bool(re.search(self.patterns['has_lower'], password)),
            'uppercase': bool(re.search(self.patterns['has_upper'], password)),
            'digits': bool(re.search(self.patterns['has_digit'], password)),
            'symbols': bool(re.search(self.patterns['has_symbol'], password))
        }

    def check_patterns(self, password: str) -> Dict[str, bool]:
        """Check password against various patterns and rules."""
        return {
            'min_length': bool(re.match(self.patterns['min_length'], password)),
            'no_repeats': not bool(re.search(self.patterns['no_repeats'], password)),
            'no_common_patterns': not bool(re.search(self.patterns['no_common_patterns'], password.lower()))
        }

    def calculate_strength_score(self, password: str) -> float:
        """Calculate overall password strength score (0-100)."""
        if not password:
            return 0.0
            
        # Base score components
        length_score = min(len(password) * 5, 25)  # Up to 25 points for length
        entropy_score = min(self.calculate_entropy(password) * 5, 25)  # Up to 25 points for entropy
        
        # Character set diversity score
        char_sets = self.analyze_character_sets(password)
        diversity_score = sum(5 for present in char_sets.values() if present)  # Up to 20 points
        
        # Pattern compliance score
        patterns = self.check_patterns(password)
        pattern_score = sum(5 for compliant in patterns.values() if compliant)  # Up to 15 points
        
        # Additional complexity score
        complexity_score = 15 if all(char_sets.values()) else 0  # 15 points for using all character sets
        
        return min(length_score + entropy_score + diversity_score + pattern_score + complexity_score, 100)

    def get_strength_category(self, score: float) -> Tuple[str, str]:
        """Get password strength category and color based on score."""
        for category, (min_score, max_score) in self.strength_categories.items():
            if min_score <= score < max_score:
                colors = {
                    'very_weak': '#FF0000',    # Red
                    'weak': '#FFA500',         # Orange
                    'moderate': '#FFFF00',     # Yellow
                    'strong': '#00FF00',       # Green
                    'very_strong': '#008000'   # Dark Green
                }
                return category.replace('_', ' ').title(), colors[category]
        return 'Unknown', '#808080'  # Gray for unknown

    def analyze_password(self, password: str) -> Dict:
        """Perform comprehensive password analysis."""
        score = self.calculate_strength_score(password)
        category, color = self.get_strength_category(score)
        
        return {
            'score': score,
            'category': category,
            'color': color,
            'entropy': self.calculate_entropy(password),
            'length': len(password),
            'char_sets': self.analyze_character_sets(password),
            'patterns': self.check_patterns(password)
        } 