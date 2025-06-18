"""
Notebooks package initialization
Automatically sets up project environtment when imported
"""

import os
import sys
from pathlib import Path

# Get project root (parent directory of notebooks folder)
notebooks_dir = Path(__file__).parent
project_root = notebooks_dir.parent

# Change working directory to project root
os.chdir(project_root)

# Add project root to Python path for imports
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Optional: Print confirmation (uncomment if you want output)
# print(f"✓ Working directory: {project_root}")
# print(f"✓ Ready to import project modules")