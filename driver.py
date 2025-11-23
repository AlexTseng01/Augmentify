# CLI script example 1: python driver.py 
# "C:\path\to\target" 
# --save_path "C:\path\to\saveFGlder" 
# --include_sub True 
# --replace_files False 
# --preview_img "C:\path\to\previewImg.png"

# CLI script example 2: python driver.py C:\path\to\target --include_sub True --replace_files True

import argparse

TARGET_PATH = None
SAVE_PATH = None
INCLUDE_SUB = False
REPLACE_FILES = False
PREVIEW_IMG = None

def main(target, save, include_sub, replace_files, preview_img):
    global TARGET_PATH, SAVE_PATH, INCLUDE_SUB, REPLACE_FILES, PREVIEW_IMG
    TARGET_PATH = target
    SAVE_PATH = save
    INCLUDE_SUB = include_sub
    REPLACE_FILES = replace_files
    PREVIEW_IMG = preview_img

    print("TARGET_PATH =",TARGET_PATH)
    print("SAVE_PATH =", SAVE_PATH)
    print("INCLUDE_SUB =", INCLUDE_SUB)
    print("REPLACE_FILES =", REPLACE_FILES)
    print("PREVIEW_IMG =", PREVIEW_IMG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Augmentify")
    parser.add_argument("target_path", help="Path to target folder")
    parser.add_argument("--save_path", default=None, help="Path to save folder")
    parser.add_argument("--include_sub", type=bool, default=False, help="Include subfolders?")
    parser.add_argument("--replace_files", type=bool, default=False, help="Replace files?")
    parser.add_argument("--preview_img", default=None, help="Path to preview image")
    args = parser.parse_args()
    main(args.target_path, args.save_path, args.include_sub, args.replace_files, args.preview_img)

