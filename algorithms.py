import sys
import argparse

def process_stream():
    
    while True:
        chunk = sys.stdin.read(1024)  
        if not chunk:
            break
        sys.stdout.write(chunk)
        sys.stdout.flush()

def process_full():
    
    data = sys.stdin.read()
    sys.stdout.write(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read STDIN and output to STDOUT in different modes.")
    parser.add_argument("--mode", choices=["gradual", "full"], required=True, help="Choose how to process input.")
    args = parser.parse_args()
    
    if args.mode == "gradual":
        process_stream()
    else:
        process_full()
