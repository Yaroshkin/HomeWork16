# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. 
# У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. 

# Необязательное
# Также класс должен считать количество подсчетов температуры и возвращать это значение с помощью статического метода.

cel = int(input("Введите градусі в цельсиях: "))
far = int(input("Введите градусі в фаренгейтах: "))

class Temperature:
    def __init__(self, celcii, farengeit):
        self.celcii = celcii
        self.farengeit = farengeit

    @staticmethod
    def Celcii():
        celcii = cel
        return celcii * 9 / 5 + 32

    @staticmethod
    def Farengeit():
        farengeit = far
        return (farengeit - 32) * 5 / 9

t = Temperature(cel,far)
tem = t.Celcii()
tem1 = t.Farengeit()
print(tem)
print(tem1)