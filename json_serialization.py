import json


def save_data(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    data = {
        "laboratory": 2,
        "variant": 6,
        "tasks": [6, 8, 2, 4, 10],
        "completed": True
    }

    save_data(data, "data.json")

    loaded_data = load_data("data.json")

    print("Loaded data:")
    print(loaded_data)