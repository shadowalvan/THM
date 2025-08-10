import re
import base64
import zlib

# Path to your radius.ps1
ps1_file = "radius.ps1"

# Read the file
with open(ps1_file, "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Extract the Base64 string inside [Convert]::FromBase64String('...')
match = re.search(r"FromBase64String\('([^']+)'\)", content)
if not match:
    raise ValueError("Base64 string not found in PowerShell script.")
b64_data = match.group(1)

# Step 2: Decode from Base64
compressed_data = base64.b64decode(b64_data)

# Step 3: Decompress (Deflate)
# In .NET DeflateStream = raw zlib DEFLATE without zlib headers in some cases.
# The 'wbits=-15' tells zlib to expect raw DEFLATE data.
decompressed_data = zlib.decompress(compressed_data, wbits=-15)

# Step 4: Save the decompressed .NET assembly to disk
output_file = "radius_payload.exe"
with open(output_file, "wb") as f:
    f.write(decompressed_data)

print(f"[+] Extracted payload saved to {output_file}")
