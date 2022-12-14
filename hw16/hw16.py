# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. 
# У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. 

# Необязательное
# Также класс должен считать количество подсчетов температуры и возвращать это значение с помощью статического метода.

cel = float(input("Введите градусі в цельсиях: "))
far = float(input("Введите градусі в фаренгейтах: "))

class Temperature:
    @staticmethod
    def Celcii(Farengeit):
        celcii = cel
        return celcii * 9 / 5 + 32

    @staticmethod
    def Farengeit(Celcii):
        farengeit = far
        return (farengeit - 32) * 5 / 9

t = Temperature()
tem = t.Celcii(cel)
tem1 = t.Farengeit(far)
print(f"Температура в Фаренгейтах {tem}")
print(f"Температура в Цельсиях {tem1}")