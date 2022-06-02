import csv
import json


def main():
    # read config from config.json
    with open("../files/config.json", "r") as f:
        config = json.load(f)

    # read from input.csv and output to output.csv
    with open("../files/input.csv", "r") as f:
        reader = csv.reader(f, **config["input"])

        with open("../files/output.csv", "w", newline="") as f:
            writer = csv.writer(f, **config["output"])

            for row in reader:
                writer.writerow([ele.strip() for ele in row])


if __name__ == "__main__":
    main()
