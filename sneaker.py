from pprint import pprint


def file_readin():
    with open('sneakers.csv', 'r', encoding='utf-8') as sneakers:
        sneakers.readline()
        keys = ['title', 'color', 'full_price', 'current_price', 'publish_date']
        data = []
        for line in sneakers:
            unsorted_data = line.strip().split(',')
            unsorted_data[2] = float(unsorted_data[2])
            unsorted_data[3] = float(unsorted_data[3])
            unsorted_data[4] = unsorted_data[4].split('T')[0]
            dictionary = dict(zip(keys, unsorted_data))
            data.append(dictionary)
        return data


def sorting(sneaker_list, number):
    choice = {1: 'title',
              2: 'color',
              3: 'full_price',
              4: 'current_price',
              5: 'publish_date'}
    pprint(sorted(sneaker_list, key=lambda shoe: shoe[choice[number]]))


def main():
    print('Válassz, melyik szempont alapján rendezzem a cipőket?')
    print('1 - title \n2 - color \n3 - full price \n4 - current price \n5 - publish date')
    choosen_number = int(input('Add meg a lehetőség számát: '))
    sorting(file_readin(), choosen_number)


main()
