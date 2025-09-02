# process_data.py

try:
    # Access inputs, outputs, and parameters from the snakemake object
    input_file = snakemake.input[0]  # Assuming a single input file
    output_file = snakemake.output[0]  # Assuming a single output file
    threshold = snakemake.params.threshold
    mode = snakemake.params.mode
except ModuleNotFoundError:
    # define input and output files manually for testing
    input_file = "raw/sample1.txt"
    output_file = "processed/sample1.processed.txt"
    threshold = 0.5
    mode = "complex"

# Rest of the script ...

