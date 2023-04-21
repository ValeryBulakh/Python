# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа

def test(s, p, step):
    if p%(s-step) == 0:
        x = p//(s-step)
        y = s - x
        if y * x == p:
            return True
        else:
            return False
    else:
        return False

while True:
    try:
        S = int(input("Введите сумму чисел: "))
        P = int(input("Введите произведение двух чисел: "))
        out = False
        for n in range(1,S-1):
            if test(S,P,n):
                print(f"{S} {P} -> {n} {S-n}")
                out = True
                break
        if out:
            break
        else:
            print(f"Числа {S} и {P} не соответствуют условиям задачи")
    except:
        print(f"Числа {S} и {P} не соответствуют условиям задачи")