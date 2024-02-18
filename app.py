import os
import socket
from collections import Counter
from pathlib import Path
# Define the data and output directories
data_dir = Path('./home/data')
output_dir = Path('./home/output')
output_file = os.path.join(output_dir, 'result.txt')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def count_words_in_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return len(words)

def top_3_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    counter = Counter(words)
    return counter.most_common(3)

def write_results(results):
    with open(output_file, 'w') as file:
         for line in results:
            file.write(f"{line}\n")



def main():
    files = list_files(data_dir)
    total_words = 0
    results = [f"Files in {data_dir}: {files}"]
    print(results)

    for file in files:
        path = os.path.join(data_dir, file)
        word_count = count_words_in_file(path)
        results.append(f"{file}: {word_count} words")
        total_words += word_count

    results.append(f"Total words in all files: {total_words}")
    
    # Assuming IF.txt is always present for simplicity
    if_txt_top_3 = top_3_words(os.path.join(data_dir, 'IF.txt'))
    ip_addess = str(socket.gethostbyname(socket.gethostname()))
    results.append(f"Top 3 words in IF.txt: {if_txt_top_3}")
    results.append(f"Ip addess:{ip_addess}")
    
    # IP address part can be complex due to various environments (Docker, VMs, etc.)
    # So, let's keep it simple by not including it unless you have a specific method in mind

    write_results(results)
    print("\n".join(results))

if __name__ == "__main__":
    main()
