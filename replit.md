# PyObfuscator - Advanced Python Code Protection System

## Overview

PyObfuscator is a comprehensive Python code obfuscation and encryption system designed for Linux environments. It provides military-grade protection against reverse engineering, code analysis, and unauthorized access through multiple layers of security including AST manipulation, advanced encryption (AES-256-GCM), anti-tampering protection, anti-debugging mechanisms, and bytecode transformation. The system can be used as a CLI tool, Python library, or to generate standalone executables and importable modules.

## User Preferences

Preferred communication style: Simple, everyday language.

## Project Status (August 2024)

### Current State
- **Ready for Linux deployment**: Core functionality working and tested
- **Basic obfuscation working**: String encoding, variable renaming, fake code injection tested successfully
- **Installation method**: Simple `python3 install.py` script that works without sudo
- **Project structure**: Fully organized in single directory with proper hierarchy
- **GitHub ready**: No sensitive data, proper .gitignore, clean structure

### Recent Changes
- Added simplified installation script (`install.py`) that works on all Linux systems
- Created basic testing framework (`test_basic.py`) that verifies core functionality  
- Implemented simplified obfuscation for immediate use
- Prepared project for GitHub deployment with proper documentation
- Fixed AST manipulation issues for Python 3.8+ compatibility

## System Architecture

### Core Architecture Pattern
The system follows a modular architecture with clear separation of concerns:

- **Core Engine (`PyObfuscatorCore`)**: Orchestrates all protection mechanisms and manages the obfuscation pipeline
- **Obfuscation Layer (`CodeObfuscator`)**: Handles AST manipulation and code transformation
- **Encryption Layer (`AdvancedEncryption`)**: Provides AES-256-GCM encryption with PBKDF2 key derivation  
- **Protection Layer (`AntiTamperProtection`)**: Implements anti-debugging and runtime integrity checks
- **Utilities**: Supporting modules for bytecode management, AST transformation, and helper functions

### AST-Based Code Transformation
The obfuscation engine uses Python's Abstract Syntax Tree (AST) for code manipulation:
- **Variable Renaming**: Systematic renaming of identifiers using random generation
- **String Obfuscation**: Encoding and hiding string literals
- **Control Flow Obfuscation**: Restructuring code logic to obscure execution paths
- **Dead Code Injection**: Adding non-functional code to confuse analysis
- **Function Inlining**: Embedding function calls to reduce structure clarity

### Multi-Layer Security Model
The protection system implements defense in depth:
1. **Code Obfuscation**: Makes source code difficult to understand
2. **Encryption**: Protects code using AES-256-GCM with custom key derivation
3. **Anti-Tampering**: Runtime checks for file modification and debugging attempts
4. **Environment Detection**: Identifies virtual machines and analysis environments
5. **Process Monitoring**: Continuous monitoring for suspicious activities

### Bytecode Management
Low-level bytecode manipulation for additional protection:
- **Compilation**: Direct compilation to bytecode objects
- **Serialization**: Marshal-based bytecode serialization
- **Runtime Loading**: Dynamic bytecode execution with integrity checks

### Usage Modes Architecture
The system supports multiple deployment patterns:
- **CLI Interface**: Command-line tool for batch processing with argparse
- **Library Interface**: Programmatic API for integration into existing projects
- **Standalone Mode**: Self-contained executables with embedded protection
- **Import Mode**: Protected modules that can be imported normally

## External Dependencies

### Core Cryptographic Dependencies
- **cryptography**: Advanced cryptographic operations including AES-256-GCM encryption, PBKDF2 key derivation, and secure random number generation
- **hashlib**: Built-in Python module for cryptographic hashing (SHA-256, MD5)
- **secrets**: Built-in Python module for cryptographically secure random number generation

### System Monitoring Dependencies  
- **psutil**: Cross-platform system and process monitoring for anti-debugging and process detection
- **os/sys**: Built-in modules for operating system interface and system-specific parameters

### Code Processing Dependencies
- **ast**: Built-in Python module for Abstract Syntax Tree manipulation and parsing
- **marshal**: Built-in module for bytecode serialization and deserialization
- **dis**: Built-in module for bytecode disassembly and analysis

### Development and Logging
- **logging**: Built-in module for structured logging and debugging
- **pathlib**: Built-in module for object-oriented filesystem path handling
- **argparse**: Built-in module for command-line argument parsing

### Runtime Dependencies
- **base64**: Built-in module for binary data encoding
- **random/string**: Built-in modules for random generation and string manipulation
- **time**: Built-in module for timing operations and performance measurement
- **threading**: Built-in module for concurrent execution in anti-tamper protection

Note: The system is designed to work with minimal external dependencies, relying primarily on Python's standard library for maximum compatibility and reduced attack surface.