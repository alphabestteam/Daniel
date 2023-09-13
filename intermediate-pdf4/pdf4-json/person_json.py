import json

def main():
    json_file = open('intermediate-pdf4\pdf4-json\person.json', 'r')
    person_data = json.load(json_file)
    json_file.close()

    print(f"Original data: {person_data}")

    person_data['name'] = 'Daniel'
    person_data['age'] = 25
    person_data['city'] = 'Hasmonaim'

    new_json_file = open('intermediate-pdf4/new_person.json', 'w')
    json.dump(person_data, new_json_file, indent=4)
    new_json_file.close()

    print(f"\nModified Data: \n {person_data}")


if __name__ == '__main__':
    main()
