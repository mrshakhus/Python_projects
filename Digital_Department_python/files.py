import os

with open('example.txt', 'w', encoding = 'utf-8') as f:
    lyrics = '''Любви, надежды, тихой славы
Недолго нежил нас обман,
Исчезли юные забавы,
Как сон, как утренний туман;
Но в нас горит еще желанье,
Под гнетом власти роковой
Нетерпеливою душой
Отчизны внемлем призыванье.
Мы ждем с томленьем упованья
Минуты вольности святой,
Как ждет любовник молодой
Минуты верного свиданья.
Пока свободою горим,
Пока сердца для чести живы,
Мой друг, отчизне посвятим
Души прекрасные порывы!
Товарищ, верь: взойдет она,
Звезда пленительного счастья,
Россия вспрянет ото сна,
И на обломках самовластья
Напишут наши имена!'''
    f.write(lyrics)

with open('example.txt', 'r', encoding = 'utf-8') as f:
    list = f.readlines()

with open('example.txt', 'r', encoding='utf-8') as f:
    print(f.read(10))
    print(f.read(10))
    f.seek(0)
    print(f.read(10))



if not os.path.exists('something.txt'):
    f = open('something.txt', 'x', encoding='utf-8')
    f.close()
else:
    print('That file already exists!')






