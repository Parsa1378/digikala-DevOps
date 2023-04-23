#!/bin/bash
mkdir -p out
# Loop through the test cases and process them
for i in $(seq 1 $1); do
  input_file="in/input${i}.txt"
  output_file="out/output${i}.txt"

  # Check if the input file exists
  if [ ! -f "$input_file" ]; then
    echo "Error: Input file '${input_file}' not found."
    exit 1
  fi

  # Run the main.py script with the input file and save the output to the output file
  python3 main.py < "$input_file" > "$output_file"
done