#!/usr/bin/env python3
"""
Usage examples for the PyObfuscator library
Demonstrates both CLI and programmatic usage
"""

import sys
import os

# Add the parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyobfuscator import PyObfuscatorCore, obfuscate_code, obfuscate_file

def example_programmatic_usage():
    """Example of using PyObfuscator programmatically"""
    print("=== Programmatic Usage Example ===")
    
    # Simple code to obfuscate
    sample_code = """
def greet(name):
    return f"Hello, {name}!"

def calculate(x, y):
    return x * 2 + y * 3

if __name__ == "__main__":
    print(greet("World"))
    print(calculate(5, 10))
"""
    
    print("Original code:")
    print(sample_code)
    print("\n" + "="*50 + "\n")
    
    # Method 1: Using convenience function
    print("Method 1: Using obfuscate_code() function")
    try:
        obfuscated = obfuscate_code(
            sample_code,
            max_security=True,
            iterations=2,
            anti_debug=True
        )
        print("✓ Obfuscation successful using convenience function")
        print(f"Original size: {len(sample_code)} characters")
        print(f"Obfuscated size: {len(obfuscated)} characters")
    except Exception as e:
        print(f"✗ Obfuscation failed: {str(e)}")
    
    print("\n" + "-"*50 + "\n")
    
    # Method 2: Using core class directly
    print("Method 2: Using PyObfuscatorCore class")
    try:
        obfuscator = PyObfuscatorCore(
            max_security=True,
            iterations=3,
            anti_debug=True,
            remove_docstrings=True,
            library_mode=False
        )
        
        obfuscated = obfuscator.obfuscate_string(sample_code)
        stats = obfuscator.get_statistics()
        
        print("✓ Obfuscation successful using core class")
        print(f"Statistics: {stats}")
        
        # Save obfuscated code to file
        with open('examples/obfuscated_example.py', 'w') as f:
            f.write(obfuscated)
        print("✓ Obfuscated code saved to examples/obfuscated_example.py")
        
    except Exception as e:
        print(f"✗ Obfuscation failed: {str(e)}")

def example_file_obfuscation():
    """Example of obfuscating files"""
    print("\n=== File Obfuscation Example ===")
    
    input_file = "examples/sample_code.py"
    output_file = "examples/sample_code_obfuscated.py"
    
    if not os.path.exists(input_file):
        print(f"✗ Input file not found: {input_file}")
        return
    
    print(f"Obfuscating file: {input_file}")
    
    # Method 1: Using convenience function
    try:
        success = obfuscate_file(
            input_file,
            output_file,
            max_security=True,
            custom_key="my_secret_key_2023",
            iterations=4
        )
        
        if success:
            print(f"✓ File obfuscation successful: {output_file}")
            
            # Check file sizes
            original_size = os.path.getsize(input_file)
            obfuscated_size = os.path.getsize(output_file)
            print(f"Original size: {original_size} bytes")
            print(f"Obfuscated size: {obfuscated_size} bytes")
            print(f"Size ratio: {obfuscated_size/original_size:.2f}x")
        else:
            print("✗ File obfuscation failed")
            
    except Exception as e:
        print(f"✗ File obfuscation error: {str(e)}")

def example_library_mode():
    """Example of creating obfuscated library"""
    print("\n=== Library Mode Example ===")
    
    library_code = """
def encrypt_text(text, key):
    \"\"\"Simple encryption function\"\"\"
    result = ""
    for i, char in enumerate(text):
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result

def decrypt_text(encrypted, key):
    \"\"\"Simple decryption function\"\"\"
    return encrypt_text(encrypted, key)  # XOR is self-inverse

class SecureStorage:
    \"\"\"Secure storage class\"\"\"
    
    def __init__(self, password):
        self.password = password
        self.data = {}
    
    def store(self, key, value):
        encrypted_value = encrypt_text(str(value), self.password)
        self.data[key] = encrypted_value
    
    def retrieve(self, key):
        if key in self.data:
            return decrypt_text(self.data[key], self.password)
        return None
"""
    
    try:
        obfuscator = PyObfuscatorCore(
            library_mode=True,
            max_security=True,
            iterations=3
        )
        
        obfuscated_library = obfuscator.obfuscate_string(library_code)
        
        # Save as library
        library_file = "examples/obfuscated_library.py"
        with open(library_file, 'w') as f:
            f.write(obfuscated_library)
        
        print(f"✓ Obfuscated library created: {library_file}")
        print("✓ Library can be imported and used normally")
        
    except Exception as e:
        print(f"✗ Library obfuscation failed: {str(e)}")

def example_advanced_configuration():
    """Example of advanced configuration options"""
    print("\n=== Advanced Configuration Example ===")
    
    test_code = """
import json
import requests

def fetch_data(url):
    response = requests.get(url)
    return json.loads(response.text)

def process_api_data(endpoint, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'success': True,
            'data': data,
            'count': len(data) if isinstance(data, list) else 1
        }
    else:
        return {'success': False, 'error': response.status_code}
"""
    
    # Different configuration examples
    configurations = [
        {
            'name': 'Basic Protection',
            'config': {
                'max_security': False,
                'iterations': 1,
                'anti_debug': False,
                'remove_docstrings': True
            }
        },
        {
            'name': 'Balanced Protection',
            'config': {
                'max_security': False,
                'iterations': 3,
                'anti_debug': True,
                'remove_docstrings': True,
                'custom_key': 'balanced_key'
            }
        },
        {
            'name': 'Maximum Security',
            'config': {
                'max_security': True,
                'iterations': 5,
                'anti_debug': True,
                'remove_docstrings': True,
                'custom_key': 'maximum_security_key_2023'
            }
        }
    ]
    
    for config_info in configurations:
        print(f"\n--- {config_info['name']} ---")
        
        try:
            obfuscator = PyObfuscatorCore(**config_info['config'])
            obfuscated = obfuscator.obfuscate_string(test_code)
            stats = obfuscator.get_statistics()
            
            print(f"✓ Configuration applied successfully")
            print(f"  - Execution time: {stats.get('execution_time', 0):.3f}s")
            print(f"  - Obfuscation passes: {stats.get('obfuscation_passes', 0)}")
            print(f"  - Size ratio: {stats.get('compression_ratio', 0):.2f}x")
            print(f"  - Security features: {', '.join(stats.get('security_features', []))}")
            
        except Exception as e:
            print(f"✗ Configuration failed: {str(e)}")

def main():
    """Run all examples"""
    print("PyObfuscator Usage Examples")
    print("=" * 50)
    
    # Ensure examples directory exists
    os.makedirs('examples', exist_ok=True)
    
    try:
        example_programmatic_usage()
        example_file_obfuscation()
        example_library_mode()
        example_advanced_configuration()
        
        print("\n" + "=" * 50)
        print("All examples completed!")
        print("\nGenerated files:")
        
        generated_files = [
            'examples/obfuscated_example.py',
            'examples/sample_code_obfuscated.py',
            'examples/obfuscated_library.py'
        ]
        
        for file_path in generated_files:
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                print(f"  - {file_path} ({size} bytes)")
        
        print("\nYou can now:")
        print("1. Run the obfuscated files directly")
        print("2. Import obfuscated libraries in your projects")
        print("3. Analyze the protection effectiveness")
        
    except Exception as e:
        print(f"Examples failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
