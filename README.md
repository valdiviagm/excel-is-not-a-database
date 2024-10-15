# Data Processing Comparison: CSV vs SQLite

This project demonstrates the performance and resource usage differences between processing large datasets using CSV files (simulating Excel) and using a SQLite database.

## Files

- **Makefile**: Automates the data generation, querying, and measurement processes.
- **generate_csv.py**: Generates a large CSV file with fake but realistic data.
- **generate_sqlite.py**: Generates a SQLite database with the same data.
- **query_csv.py**: Performs a query on the CSV file.
- **query_sqlite.py**: Performs the same query on the SQLite database.
- **README.md**: Instructions and information about the project.

## Usage

Run the following command to generate data, perform queries, and measure execution time and resource usage:

\`\`\`bash
make
\`\`\`

This will execute the following steps:

1. **generate_csv**: Generates the CSV file.
2. **generate_sqlite**: Generates the SQLite database.
3. **query_csv**: Performs the query on the CSV file.
4. **query_sqlite**: Performs the query on the SQLite database.

The output will include execution time and resource usage for both methods.

### Cleaning Up

To remove the generated files, run:

\`\`\`bash
make clean
\`\`\`

## Adjusting Data Size

You can adjust the size of the dataset by modifying the \`num_rows\` variable in both \`generate_csv.py\` and \`generate_sqlite.py\`.

## Interpretation

By comparing the execution time and resource usage, you can observe the inefficiencies of using CSV files (simulating Excel) for large datasets compared to using a SQLite database. This demonstrates the practicality of using databases over spreadsheets for handling substantial amounts of data.

