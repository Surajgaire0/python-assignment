import json

import requests


def main():
    response = requests.get("https://jsonplaceholder.typicode.com/todos", verify=False).json()

    # printing first 2 data
    for data in response[:2]:
        for k, v in data.items():
            print(k, " : ", v)
        print()

    # save response in file
    with open("../files/response.json", "w+") as f:
        json.dump(response[:2], f, indent=4)

        # read from file
        f.seek(0)
        data_in_file = json.load(f)
        print(data_in_file)


if __name__ == "__main__":
    main()
