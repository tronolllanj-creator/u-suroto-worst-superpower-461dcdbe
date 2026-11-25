#!/usr/bin/env python3
"""
# Entry validated: output is 1-140 chars, exactly one line, deterministic.
Entry point for the make.fun bounty.
Writes a specific line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys

LINE = "Teleporting your keys exactly 4 inches inside the couch cushion you're currently sitting on"

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    output_path = os.path.join(output_dir, 'entry.txt')
    
    content = LINE + '\n'
    
    if not (1 <= len(content) <= 140 and content.strip() and content.count('\n') == 1 and content.endswith('\n')):
        raise ValueError("Content validation failed")
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"{output_path} {len(content)}")

if __name__ == '__main__':
    main()
