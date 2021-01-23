# Remove all of the comments from a Python file
# (Ignoring the where a comment character occurs within a string)

# Read the file name and open the input file
try:
    in_name = input("Enter the name of a Python file: ")
    inf = open(in_name, "r")

except:
    # Display an error message and quit if the file was not opened successfully
    print("A problem was encountered with the input file.")
    print("Quitting...")
    quit()
# Read the file name and open the output file
try:
    out_name = input("Enter the output file name: ")
    outf = open(out_name, "w")

except:
    # Close the input file, display an error message and quit if the file was not opened
    # successfully
    inf.close()
    print("A problem was encountered with the output file.")
    print("Quitting...")
    quit()

try:
    # Read all of the lines from the input file, remove the comments from them, and save the
    # modified lines to a new file
    for line in inf:
        # Find the position of the comment character (-1 if there isn`t one)
        pos = line.find("#")

        # If there is a comment then create a slice of the string that excludes it and store it back
        # into line

        if pos > -1:
            line = line[0 : pos]
            line = line + "\n"

        # Write the (potentially modified) line to the file
        outf.write(line)

    # Close the files
    inf.close()
    outf.close()

except:
    # Display an erorr message if something went wrong while processing file.
    print("A problem was encountered while processing the file.")
    print("Quitting...")
