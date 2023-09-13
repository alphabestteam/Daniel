def main():

    
    def words_length(*words):
        sum = 0
        for i in words:
            sum += len(i)
        print(sum)

    words_length('daniel','chen','moshe')
    # age total function which receive an arguments in dict structor and print all the "keys", and values
    def age_total(**ages):
        total = 0
        for age_name, age_value in ages.items():
            print(f"{age_name}: {age_value}")
            total += age_value
        print(total)

    age_total(aga=10,age=12)

if __name__ == '__main__':
    main()