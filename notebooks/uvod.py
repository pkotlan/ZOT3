import marimo

__generated_with = "0.20.2"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Úvod do Pythonu

    **Doporučené zdroje (na doma):**
    - [W3Schools Python Tutorial](https://www.w3schools.com/python/)
    - [W3Schools Python Exercises](https://www.w3schools.com/python/python_exercises.asp)
    """)
    return


@app.cell
def _():
    print("Hello World!")  # tuto funkci si zapamatuj
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Proměnné a datové typy

    Proměnná je pojmenované místo v paměti, do kterého uložíme hodnotu. Python **nevyžaduje deklaraci typu** – typ se určí automaticky podle přiřazené hodnoty.

    Základní datové typy:

    | Typ | Popis | Příklad |
    |-----|-------|---------|
    | `int` | celé číslo | `42` |
    | `float` | desetinné číslo | `3.14` |
    | `str` | řetězec (text) | `"ahoj"`,`'ahoj'` |
    | `bool` | pravdivostní hodnota | `True`, `False` |

    Pro názvy proměnných používej malá písmena a podtržítka (`snake_case`), např. `pocet_studentu`.
    """)
    return


@app.cell
def _():
    cislo = 42
    des_cislo = 3.14
    retezec = "ahoj"
    pravda = True

    print("cislo:", cislo)
    print("des_cislo:", des_cislo)
    print("retezec:", retezec)
    print("pravda:", pravda)
    return cislo, des_cislo, pravda, retezec


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funkce `type` slouží k zjištění typu proměnné.
    """)
    return


@app.cell
def _(cislo, des_cislo, pravda, retezec):
    print("Typ cislo:", type(cislo))
    print("Typ des_cislo:", type(des_cislo))
    print("Typ retezec:", type(retezec))
    print("Typ pravda:", type(pravda))

    # vyzkoušej změnit hodnotu proměnné val
    val = 10
    print("Typ val:", type(val))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Seznamy

    Seznam je **uspořádaná kolekce** hodnot. Hodnoty mohou být libovolného typu. Indexuje se od **nuly**.

    Nejčastější operace:
    - přístup k prvku: `seznam[0]`
    - přidání prvku: `seznam.append(hodnota)`
    - délka seznamu: `len(seznam)`

    - [👉 Metody](https://www.w3schools.com/python/python_lists_methods.asp)
    """)
    return


@app.cell
def _():
    values = [12, 55, 130, 255]

    print("Původní seznam:", values)
    print("První prvek:", values[0])
    print("Poslední prvek:", values[-1])

    values.append(80)
    print("Po append:", values)
    print("Počet prvků:", len(values))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Základní aritmetické operace

    Aritmetika je potřeba prakticky všude: od jednoduchých výpočtů až po zpracování dat.
    """)
    return


@app.cell
def _():
    a = 15
    b = 4

    print("Sčítání:", a + b)
    print("Odčítání:", a - b)
    print("Násobení:", a * b)
    print("Dělení:", a / b)
    print("Celočíselné dělení:", a // b)
    print("Zbytek po dělení:", a % b)
    print("Mocnina:", a**b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Funkce

    Funkce je **pojmenovaný blok kódu**, který můžeme opakovaně volat. Pomáhá organizovat kód a předcházet opakování.

    Základní struktura:

    ```python
    def nazev_funkce(parametr):
        # tělo funkce
        return vysledek
    ```
    """)
    return


@app.cell
def _():
    def secti_cisla(cislo1, cislo2):
        return cislo1 + cislo2


    def je_svetly_pixel(hodnota):
        "Jednoduché pravidlo: cokoliv nad 127 bereme jako 'světlé'"
        return hodnota > 127


    print("3 + 5 =", secti_cisla(3, 5))
    print("Pixel 200 je světlý?", je_svetly_pixel(200))  # zkus změnit hodnotu
    return (je_svetly_pixel,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Podmínky

    Podmínky rozhodují, **který kód se provede**.

    ```python
    if podminka:
        ...
    elif jina_podminka:
        ...
    else:
        ...
    ```
    """)
    return


@app.cell
def _(je_svetly_pixel):
    hodnota_pixelu = 90

    if je_svetly_pixel(hodnota_pixelu):
        print("Pixel je světlý")
    else:
        print("Pixel je tmavší")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cykly

    Cykly slouží k opakování.

    - `for` používáme, když procházíme kolekci nebo rozsah.
    - `while` používáme, když opakujeme, dokud platí podmínka.
    """)
    return


@app.cell
def _():
    print("for cyklus přes seznam:")
    for hodnota in [5, 10, 15]:
        print("-", hodnota)

    print("\nfor cyklus přes range(5):")
    for i in range(5):
        print("i =", i)

    print("\nwhile cyklus:")
    pocitadlo = 0
    while pocitadlo < 3:
        print("pocitadlo =", pocitadlo)
        pocitadlo += 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Samostatná cvičení

    Cíl: procvičit stejné principy, které jsme viděli výš, ale na smysluplnějších mini-úlohách.

    1. **Vizitka studenta**
       Vytvoř proměnné `jmeno`, `obor`, `rocnik` a vypiš větu např. `Jmenuji se ... studuji ... a jsem v ... ročníku.`
       - Bonus: přidej proměnnou `ma_zajem_o_obraz = True/False` a vypiš i tuto informaci.

    2. **Práce se seznamem měření**
       Vytvoř seznam `teploty = [18.5, 19.0, 21.3, 20.1, 17.8]` a vypiš první a poslední.
       - Bonus: přidej nové měření `22.0` a znovu vypiš délku seznamu.

    3. **Průměr ze tří hodnot**
       Napiš funkci `prumer(a, b, c)`, která vrátí aritmetický průměr tří čísel.
       - Bonus: zobecni funkci na `prumer_seznamu(hodnoty)`, která přijme seznam.

    4. **Jednoduchá klasifikace hodnoty**
       Pro číslo `x` vypiš, zda je `kladné`, `záporné` nebo `nula`.
       - Bonus: přidej variantu, která navíc vypíše, jestli je číslo sudé/liché (pro nenulové celé číslo).

    5. **Sudá a lichá čísla**
       Pomocí `for` vypiš čísla od 1 do 10 a ke každému text `sudé` / `liché`.
       - Bonus: spočítej, kolik sudých a kolik lichých čísel v rozsahu je.

    6. **Světlé pixely nad prahem**
       Máš seznam jasů pixelů `[10, 120, 200, 30, 255]`. Spočítej, kolik hodnot je větších než `127`.
       - Bonus: napiš funkci `pocet_svetlych(hodnoty, prah)`.
       - Bonus: uprav funkci tak, aby vracela seznam světlých hodnot místo jejich počtu.
    """)
    return


if __name__ == "__main__":
    app.run()
