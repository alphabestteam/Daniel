import json


def main():
    read_json = open("intermediate-pdf4/config.json", 'r')
    data_content = json.load(read_json)
    read_json.close()

    data_value = data_content["data"].upper()

    if data_content["silent"] == "True":
        print(data_value)

    data_content["data"] = data_value

    write_json = open('intermediate-pdf4/config.json', 'w')
    json.dump(data_content, write_json)
    write_json.close()


if __name__ == '__main__':
    main()
