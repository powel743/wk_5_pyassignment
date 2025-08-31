#Python assignment: File handling and exceptional handling
def modify_line(line):
    """
Modify the line from file.
Example: convert to uppercase
    """
    return line.upper() 
def process_files(input_file, output_file):
    try:
        #open and read the input file
        with open(input_file, 'r') as infile:
            for line in lines:
                outfile.write(modify_line(line))
        print(f"Modified content has been written to '{output_file}'.")
        # Open and write modified lines to the output file
        with open(output_file, 'w') as outfile:
            for line in lines:
                outfile.write(modify_line(line))
        print(f"Modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError:
        print(f"Error: Cannot read/write file '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    # Ask the user for filenames
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    
    process_files(input_file, output_file)

if __name__ == "__main__":
    main()       
