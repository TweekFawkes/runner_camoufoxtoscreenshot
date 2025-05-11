import browserforge
from browserforge.fingerprints import FingerprintGenerator
from browserforge.headers import HeaderGenerator
import os
from importlib import resources

# Initialize the FingerprintGenerator (triggers download of fingerprint-network.zip)
print("Initializing FingerprintGenerator...")
fingerprint_gen = FingerprintGenerator()
print("FingerprintGenerator initialized.")

# Initialize the HeaderGenerator (triggers download of input-network.zip)
print("Initializing HeaderGenerator...")
header_gen = HeaderGenerator()
print("HeaderGenerator initialized.")

# Use importlib.resources to locate the data directories
with resources.as_file(resources.files('browserforge.fingerprints').joinpath('data')) as fingerprint_dir:
    fingerprint_path = os.path.join(fingerprint_dir, 'fingerprint-network.zip')

with resources.as_file(resources.files('browserforge.headers').joinpath('data')) as header_dir:
    header_path = os.path.join(header_dir, 'input-network.zip')

# Verify the files are downloaded
print(f"Checking for fingerprint-network.zip at: {fingerprint_path}")
if os.path.exists(fingerprint_path):
    print("fingerprint-network.zip found!")
else:
    print("fingerprint-network.zip not found.")

print(f"Checking for input-network.zip at: {header_path}")
if os.path.exists(header_path):
    print("input-network.zip found!")
else:
    print("input-network.zip not found.")