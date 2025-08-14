#!/usr/bin/env python3
"""
Basic test to verify PyObfuscator imports work
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if PyObfuscator modules can be imported"""
    print("Testing PyObfuscator module imports...")
    
    try:
        from pyobfuscator import utils
        print("✓ utils module imported successfully")
    except Exception as e:
        print(f"✗ utils import failed: {e}")
        return False
    
    try:
        from pyobfuscator.utils import generate_random_name, encode_string
        print("✓ utility functions imported successfully")
        
        # Test utility functions
        random_name = generate_random_name()
        print(f"✓ Generated random name: {random_name}")
        
        encoded = encode_string("Hello World")
        print(f"✓ String encoding works: {encoded[:20]}...")
        
    except Exception as e:
        print(f"✗ Utility functions failed: {e}")
        return False
    
    try:
        from pyobfuscator.encryption import AdvancedEncryption
        enc = AdvancedEncryption()
        print("✓ Encryption module works")
    except Exception as e:
        print(f"✗ Encryption module failed: {e}")
        return False
    
    return True

def test_basic_obfuscation_manual():
    """Test basic manual obfuscation"""
    from pyobfuscator.utils import generate_random_name, encode_string
    
    original_code = '''
def hello():
    print("Hello World")
    
hello()
'''
    
    print("\nOriginal code:")
    print(original_code)
    
    # Manual simple obfuscation
    obfuscated_parts = []
    
    # Add fake imports
    obfuscated_parts.append("import os as _OS_MODULE_8834")
    obfuscated_parts.append("import sys as _SYS_MODULE_9922") 
    
    # Add fake variables
    fake_var1 = generate_random_name()
    fake_var2 = generate_random_name()
    obfuscated_parts.append(f"{fake_var1} = 7743")
    obfuscated_parts.append(f"{fake_var2} = 'decoy_string_data'")
    
    # Simple function renaming and string obfuscation
    func_name = generate_random_name()
    hello_encoded = encode_string("Hello World")
    
    obfuscated_parts.append(f"""
def {func_name}():
    exec(__import__('base64').b64decode('{hello_encoded}').decode())
    
{func_name}()
""")
    
    obfuscated_code = "\n".join(obfuscated_parts)
    
    print("\nObfuscated code:")
    print(obfuscated_code)
    
    # Save to file
    with open('basic_obfuscated.py', 'w') as f:
        f.write(obfuscated_code)
    
    print("\n✓ Basic manual obfuscation completed")
    print("✓ Saved to basic_obfuscated.py")
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("PyObfuscator Basic Tests")
    print("=" * 50)
    
    success1 = test_imports()
    success2 = test_basic_obfuscation_manual()
    
    if success1 and success2:
        print("\n✓ All basic tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)