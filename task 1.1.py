import sys
import base64

def read_gradually():
    for line in sys.stdin:
        line = line.rstrip("\n")  # Strip trailing newline for cleaner encoding
        encoded_line = base64.b64encode(line.encode()).decode()
        sys.stdout.write(encoded_line + "\n")
        sys.stdout.flush()  # Ensure immediate output

def read_all_at_once():
    data = sys.stdin.read()
    if not data.strip():
        sys.stderr.write("Error: No input received.\n")
        sys.exit(1)
    
    encoded_data = base64.b64encode(data.encode()).decode()
    sys.stdout.write(encoded_data + "\n")

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python script.py [gradual|all-at-once]\n")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "gradual":
        read_gradually()
    elif mode == "all-at-once":
        read_all_at_once()
    else:
        sys.stderr.write("Invalid mode. Use 'gradual' or 'all-at-once'.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
