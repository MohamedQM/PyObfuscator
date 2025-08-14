#!/usr/bin/env python3
"""
Sample Python code to demonstrate the obfuscation system
This file will be obfuscated using the PyObfuscator
"""

import os
import sys
import time
import hashlib

def fibonacci(n):
    """Calculate fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

class Calculator:
    """Simple calculator class"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history.copy()

def process_data(data_list):
    """Process a list of data"""
    if not data_list:
        return []
    
    processed = []
    for item in data_list:
        if isinstance(item, str):
            # Hash string values
            hashed = hashlib.md5(item.encode()).hexdigest()
            processed.append(hashed)
        elif isinstance(item, (int, float)):
            # Double numeric values
            processed.append(item * 2)
        else:
            processed.append(str(item))
    
    return processed

def main():
    """Main function"""
    print("Python Code Obfuscation Demo")
    print("=" * 30)
    
    # Test fibonacci
    print(f"Fibonacci of 10: {fibonacci(10)}")
    
    # Test factorial
    print(f"Factorial of 5: {factorial(5)}")
    
    # Test calculator
    calc = Calculator()
    result1 = calc.add(15, 25)
    result2 = calc.multiply(7, 8)
    
    print(f"Calculator results: {result1}, {result2}")
    print("Calculator history:")
    for entry in calc.get_history():
        print(f"  {entry}")
    
    # Test data processing
    test_data = ["hello", "world", 42, 3.14, [1, 2, 3]]
    processed = process_data(test_data)
    print(f"Processed data: {processed}")
    
    # Environment information
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"Current directory: {os.getcwd()}")
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()
