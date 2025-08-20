import os
import shutil

dir1 = os.path.expanduser('/home/kali/.local/nuclei-templates')
dir2 = '/home/kali/clustered_templates'

for root, dirs, files in os.walk(dir1):
    # Compute path relative to dir1, to replicate structure
    rel_root = os.path.relpath(root, dir1)
    target_root = os.path.join(dir2, rel_root) if rel_root != '.' else dir2

    # Copy missing directories
    for d in dirs:
        src_dir = os.path.join(root, d)
        target_dir = os.path.join(target_root, d)
        if not os.path.exists(target_dir):
            try:
                os.makedirs(target_dir, exist_ok=True)
            except Exception as e:
                print(f"Failed to create directory {target_dir}: {e}")

    # Copy missing files
    for f in files:
        src_file = os.path.join(root, f)
        target_file = os.path.join(target_root, f)
        if not os.path.exists(target_file):
            try:
                shutil.copy2(src_file, target_file)
            except Exception as e:
                print(f"Failed to copy {src_file} to {target_file}: {e}")

print("Copy complete: Missing files and folders from directory 1 now in directory 2.")

