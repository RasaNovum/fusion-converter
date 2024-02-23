import os
import shutil
import subprocess
import time

auto_import_dir = "./auto_import/"
auto_export_dir = "./auto_export/"
import_dir = "./import/automation/"
export_dir = "./export/automation/"
conv_script = "./MT-Fusion-Converter.py"

# Add neccecary folders
if os.path.exists(auto_import_dir) == False:
    os.makedirs(auto_import_dir)
if os.path.exists(auto_export_dir) == False:
    os.makedirs(auto_export_dir)
if os.path.exists(import_dir) == False:
    os.makedirs(import_dir)

while os.listdir(auto_import_dir):
    original_name = os.listdir(auto_import_dir)[0]
    print(original_name)

    # Move [original_name].png from /auto_import/ into /import/automation/
    shutil.copy(os.path.join(auto_import_dir, original_name), os.path.join(import_dir, original_name))

    # Delete 1.png in /import/automation/
    if os.path.exists(os.path.join(import_dir, "1.png")):
        os.remove(os.path.join(import_dir, "1.png"))
    
    # Move [original_name].png from /export/automation/ into /auto_export/
    shutil.move(os.path.join(auto_import_dir, original_name), os.path.join(import_dir, original_name))

    # Rename [original_name].png to 1.png
    os.rename(os.path.join(import_dir, original_name), os.path.join(import_dir, "1.png"))

    # Run conv.py
    subprocess.run(["python", conv_script])

    # Wait until 1.png appears in /export/automation/
    while not os.path.exists(os.path.join(export_dir, "1.png")):
        time.sleep(1)

    # Move 1.png from /export/automation/ into /auto_export/
    shutil.move(os.path.join(export_dir, "1.png"), os.path.join(auto_export_dir, "1.png"))

    # Rename 1.png to [original_name].png name
    os.rename(os.path.join(auto_export_dir, "1.png"), os.path.join(auto_export_dir, original_name))

    # Delete 1.png in /import/automation/
    if os.path.exists(os.path.join(import_dir, "1.png")):
        os.remove(os.path.join(import_dir, "1.png"))
