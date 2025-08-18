import os


def process_any_files(root_dir):
    """
    """
    for subdir, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '.pixi']]
        for filename in files:
            if filename.lower().endswith((".cpp", ".c++", "cc", ".c", ".h", ".h++", ".hpp", ".cxx", ".py", ".yaml", ".yml", "bat", ".md", ".py", ".csv", ".jinja")):
            #if filename.lower().endswith(("bat")):
                filepath = os.path.join(subdir, filename)
                print(f"Processing file: {filepath}")
                try:
                    # Read lines and strip trailing whitespace from each
                    try: 
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except UnicodeDecodeError:
                        with open(filepath, 'r') as f:
                            content = f.read()

                    # Write back with lf line endings
                    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
                        f.write(content)
                    
                    print(f"Successfully processed: {filepath}")
                except Exception as e:
                    print(f"Error processing file {filepath}: {e}")

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Starting processing in directory: {script_dir}")
    process_any_files(script_dir)
    print("Processing complete.")
