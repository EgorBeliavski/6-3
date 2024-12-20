
#Написать программу, которая:
#Запрашивает у пользователя количество строк. (должно быть проверка)

#Затем сами строки.

#Определяет, сколько различных слов содержится в этом тексте, и выводит из количество

#Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

x = int(input("Введите кол-во строк: ")) #ввод кол-ва строк

if x<0 : #проверка
    print("Количество строк введено неверно.")
    quit()

text = [[str(input("Введите сроку: "))] for i in range(x)] #создание двумерного массива со строками

sum = 0 # переменная для суммы слов

for i in text: #подсчет кол-ва слов
    for j in i:
        words = j.split()
        sum+=len(words)
    
print("Количество слов: ",sum)
