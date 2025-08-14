#!/usr/bin/env python3
"""
Advanced Python Code Obfuscator and Encryption System
Main CLI interface for the obfuscation system
"""

import argparse
import os
import sys
import logging
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pyobfuscator.core import PyObfuscatorCore
from pyobfuscator.utils import setup_logging, validate_python_file

def main():
    parser = argparse.ArgumentParser(
        description="Advanced Python Code Obfuscator with Encryption",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s script.py                    # Basic obfuscation
  %(prog)s script.py -o output.py      # Specify output file
  %(prog)s script.py --max-security    # Maximum security mode
  %(prog)s script.py --custom-key mykey # Custom encryption key
  %(prog)s --library script.py         # Generate as importable library
        """
    )
    
    parser.add_argument("input_file", help="Python file to obfuscate")
    parser.add_argument("-o", "--output", help="Output file path (default: input_obfuscated.py)")
    parser.add_argument("--max-security", action="store_true", 
                       help="Enable maximum security mode with all protections")
    parser.add_argument("--custom-key", help="Custom encryption key (optional)")
    parser.add_argument("--library", action="store_true",
                       help="Generate as importable library module")
    parser.add_argument("--iterations", type=int, default=3,
                       help="Number of obfuscation iterations (default: 3)")
    parser.add_argument("--anti-debug", action="store_true",
                       help="Enable anti-debugging mechanisms")
    parser.add_argument("--remove-docstrings", action="store_true",
                       help="Remove all docstrings and comments")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    logger = logging.getLogger(__name__)
    
    try:
        # Validate input file
        if not validate_python_file(args.input_file):
            logger.error(f"Invalid Python file: {args.input_file}")
            sys.exit(1)
        
        # Determine output file
        if args.output:
            output_file = args.output
        else:
            input_path = Path(args.input_file)
            output_file = input_path.parent / f"{input_path.stem}_obfuscated{input_path.suffix}"
        
        # Initialize obfuscator
        obfuscator = PyObfuscatorCore(
            max_security=args.max_security,
            custom_key=args.custom_key,
            iterations=args.iterations,
            anti_debug=args.anti_debug,
            remove_docstrings=args.remove_docstrings,
            library_mode=args.library
        )
        
        logger.info(f"Starting obfuscation of {args.input_file}")
        logger.info(f"Output will be saved to {output_file}")
        
        # Perform obfuscation
        success = obfuscator.obfuscate_file(args.input_file, output_file)
        
        if success:
            logger.info("Obfuscation completed successfully!")
            logger.info(f"Obfuscated file saved: {output_file}")
            
            # Display statistics
            stats = obfuscator.get_statistics()
            logger.info(f"Statistics: {stats}")
        else:
            logger.error("Obfuscation failed!")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
