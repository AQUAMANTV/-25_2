import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []

    # Читаем CSV файл
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)  

        for row in reader:
            row_dict = dict(zip(headers, row))
            data.append(row_dict)

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")