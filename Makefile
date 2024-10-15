.PHONY: all generate_csv generate_sqlite query_csv query_sqlite measure_csv measure_sqlite clean

all: measure_csv measure_sqlite

generate_csv:
python generate_csv.py

generate_sqlite:
python generate_sqlite.py

query_csv:
/usr/bin/time -l python query_csv.py

query_sqlite:
/usr/bin/time -l python query_sqlite.py

measure_csv: generate_csv query_csv

measure_sqlite: generate_sqlite query_sqlite

clean:
rm -f large_data.csv large_data.db
