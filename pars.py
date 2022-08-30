import csv

with open('C:/Users/i.Reznikov/Desktop/test_data.csv', encoding='utf8') as file_csv:
    finput = csv.reader(file_csv)
    foutput = open('test.csv', 'w', encoding='utf8')
    farray = []
    HelloWords = ['добрый день', 'здравствуйте', 'привет', 'доброе утро']
    NameWords = ['меня']
    ByeWords = ['до свидания', 'всего доброго']
    writer = csv.writer(foutput)
    for i in finput:
        farray.append(i)
    farray[0].append('insight')
    stroka = 0
    for i in farray:
        for j in HelloWords:
            if j in i[3].lower() and 'manager' in i[2]:
                farray[stroka].append('True')
                print(i[3])
        for j in NameWords:
            if j in i[3].lower() and 'manager' in i[2]:
                print(i[3])
                if 'меня зовут' in i[3].lower() and 'manager' in i[2]:
                    print("Имя менеджера: " + i[3][i[3].lower().find('зовут') + 6: i[3].find('компания')])
                elif 'меня' in i[3].lower() and 'manager' in i[2]:
                    print("Имя менеджера: " + i[3][i[3].lower().find('меня') + 5: i[3].find('зовут')])
                elif 'это' in i[3].lower() and 'manager' in i[2]:
                    print("Имя менеджера: " + i)
                print("Компания: " + i[3][i[3].lower().find('компания') + 9: i[3].find('бизнес')+6])
        for j in ByeWords:
            if j in i[3].lower() and 'manager' in i[2]:
                print(i[3])
        stroka += 1
    for i in farray:
        writer.writerow(i)
    foutput.close()