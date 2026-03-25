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
    # Úvod do NumPy

    **NumPy** je knihovna pro vědecké výpočty v Pythonu. Poskytuje:
    - Multidimenzionální pole (`ndarray`) – mnohem rychlejší než seznamy
    - Matematické a statistické funkce
    - Lineární algebru, Fourierovu transformaci a náhodná čísla

    **Zdroje:**
    - [NumPy Documentation](https://numpy.org/doc/)
    - [NumPy Tutorials](https://numpy.org/learn/)
    - [NumPy Cheat Sheet](https://numpy.org/devdocs/user/basics.broadcasting.html)
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vytváření polí (arrays)

    NumPy pole jsou homogenní – všechny prvky mají stejný typ. Na rozdíl od Pythonových seznamů jsou **mnohem rychlejší**.

    Nejčastější způsoby vytvoření:
    - `np.array([...])` – z seznamu
    - `np.zeros(shape)` – všechny nuly
    - `np.ones(shape)` – všechny jedničky
    - `np.arange(start, stop, step)` – sekvence
    - `np.linspace(start, stop, n)` – n bodů mezi startem a stopem
    """)
    return


@app.cell
def _(np):
    arr1 = np.array([1, 2, 3, 4, 5])
    print("Array:", arr1)
    print("Tvar (shape):", arr1.shape)
    print("Datový typ:", arr1.dtype)
    print("Počet dimenzí:", arr1.ndim)
    return


@app.cell
def _(np):
    nuly = np.zeros(5)
    print("Nuly:", nuly)

    jednicky = np.ones(3)
    print("Jedničky:", jednicky)

    postupnost = np.arange(0, 10, 2)
    print("Sekvence 0 do 10 s krokem 2:", postupnost)

    linspace_arr = np.linspace(0, 1, 5)
    print("5 bodů lineárně od 0 do 1:", linspace_arr)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Multidimenzionální pole (matice)

    NumPy snadno pracuje s maticemi a vícedimenzionálními poli. Tvar pole určuje `shape`.
    """)
    return


@app.cell
def _(np):
    matice_2d = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    print("Matice:")
    print(matice_2d)
    print("Tvar:", matice_2d.shape)  # (3, 3)

    # Vytvoření matice nul
    nuly_2d = np.zeros((2, 4))
    print("\nMatice nul (2x4):")
    print(nuly_2d)
    return (matice_2d,)


@app.cell
def _(matice_2d):
    matice_2d[:1,:]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Indexování a krájení (slicing)

    Přístup k prvkům pole je podobný jako u seznamů, ale NumPy umožňuje multidimenzionální indexování. __Indexuje se od 0.__
    """)
    return


@app.cell
def _(matice_2d):
    print("Třetí řádek:", matice_2d[2])
    print("Prvek v řádku 2, sloupci 3:", matice_2d[1, 2])

    print("Podmatice (řádky 0-2, sloupce 1-3):")
    print(matice_2d[0:2, 1:3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Logické indexování
    """)
    return


@app.cell
def _(matice_2d):
    mask = matice_2d > 2
    print("Prvky větší než 2:", matice_2d[mask])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vektorové operace

    Jedna z největších výhod NumPy je **vektorizace** – operace se aplikují na celé pole bez explicitního cyklu.
    """)
    return


@app.cell
def _(np):
    arr2 = np.array([1, 2, 3, 4, 5])

    # Aritmetika
    print("Původní pole:", arr2)
    print("Pole + 10:", arr2 + 10)
    print("Pole * 2:", arr2 * 2)
    print("Pole ** 2:", arr2 ** 2)

    # Porovnání
    print("\nPrvky > 2:", arr2 > 2)
    print("Prvky == 3:", arr2 == 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Operace mezi poli

    NumPy automaticky provádí **broadcasting** – rozšíření menšího pole na tvar větší.
    """)
    return


@app.cell
def _(np):
    a1 = np.array([1, 2, 3])
    b1 = np.array([10, 20, 30])

    print("a:", a1)
    print("b:", b1)
    print("a + b:", a1 + b1)
    print("a * b:", a1 * b1)

    # Broadcasting s skalárem
    print("\na + 5:", a1 + 5)
    print("a * 10:", a1 * 10)

    # Broadcasting s poli různých tvarů
    test_matice = np.array([[1, 2, 3],
                       [4, 5, 6]])
    radek = np.array([10, 20, 30])
    print("\nMatice:\n", test_matice)
    print("Řádek:", radek)
    print("Matice + řádek:\n", test_matice + radek)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Agregační funkce

    NumPy poskytuje efektivní funkce pro výpočet statistik na celém poli nebo po osách.
    """)
    return


@app.cell
def _(np):
    data = np.array([10, 25, 15, 30, 20])

    print("Data:", data)
    print("Součet:", np.sum(data))
    print("Průměr:", np.mean(data))
    print("Medián:", np.median(data))
    print("Standardní odchylka:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))
    return


@app.cell
def _(np):
    # Agregace v multidimenzionálních polích
    mat = np.array([[1, 2, 3],
                    [4, 5, 6]])

    print("Matice:")
    print(mat)
    print("\nSoučet všech prvků:", np.sum(mat))
    print("Součet po sloupcích (axis=0):", np.sum(mat, axis=0))
    print("Součet po řádcích (axis=1):", np.sum(mat, axis=1))
    print("Průměr po sloupcích:", np.mean(mat, axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Náhodná čísla

    NumPy má vstavěný generátor náhodných čísel pro vytváření pseudonáhodných dat.
    """)
    return


@app.cell
def _(np):
    # Náhodná celá čísla
    random_ints = np.random.randint(1, 100, size=10)
    print("10 náhodných celých čísel 1-99:", random_ints)

    # Náhodná reálná čísla z rovnoměrného rozdělení [0, 1)
    random_floats = np.random.random(5)
    print("5 náhodných reálných čísel [0, 1):", random_floats)

    # Náhodná čísla z normálního rozdělení
    normal = np.random.normal(loc=0, scale=1, size=5)
    print("5 čísel z normálního rozdělení:", normal)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tvar a manipulace

    NumPy umožňuje měnit tvar polí bez kopírování dat.
    """)
    return


@app.cell
def _(np):
    arr = np.arange(12)
    print("Původní pole (1D):", arr)

    # Reshape na matici
    matice = arr.reshape(3, 4)
    print("Po reshape(3, 4):")
    print(matice)

    # Vrácení do 1D
    plochý = matice.reshape(-1)
    print("Zpět do 1D:", plochý)

    # Transpose
    print("Transpose:")
    print(matice.T)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Připojení a spojování

    NumPy umožňuje kombinovat pole do větších struktur.
    """)
    return


@app.cell
def _(np):
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    # Připojení (concatenate)
    spojene = np.concatenate([a, b])
    print("np.concatenate([a, b]):", spojene)

    # Stack (vytvoří novou dimenzi)
    zalozene = np.stack([a, b])
    print("np.stack([a, b]):")
    print(zalozene)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Samostatná cvičení

    Cíl: procvičit NumPy koncepty na praktických příkladech.

    1. **Vytvoření a inspekce pole**
       Vytvoř pole čísel od 0 do 19 a vypiš jeho tvar, typ a počet dimenzí.
       - Bonus: Preformuj pole na matici 4×5.

    2. **Indexování matice**
       Vytvoř matici 5×5 s čísly od 1 do 25 a vypiš:
       - Prostřední prvek
       - Poslední řádek
       - První tři sloupce prvních dvou řádků
       - Bonus: Všechny prvky, které jsou větší než 15.

    3. **Vektorové operace**
       Vytvoř dvě pole `x = [1, 2, 3, 4, 5]` a `y = [10, 20, 30, 40, 50]`.
       - Vypočítej součet, rozdíl, součin
       - Vypočítej `x ** 2 + y ** 2`
       - Bonus: Které prvky splňují `x > 2 AND y < 40`?

    4. **Statistika**
       Vytvoř pole 100 náhodných čísel z normálního rozdělení se střední hodnotou 50 a směrodatnou odchylkou 10.
       - Vypočítej průměr, medián, minimum, maximum
       - Spočítej, kolik hodnot je v rozsahu [40, 60]

    5. **Matické operace**
       Vytvoř matici 3×3 s hodnotami 1-9 a matici 3×3 s hodnotami 10-18.
       - Sečti matice
       - Vynásob po prvcích (Hadamardův součin)
       - Vypočítej součet každého řádku a sloupce

    6. **Broadcasting**
       Vytvoř matici 3×3 s náhodnými čísly a přičti její průměr každému prvku.
       - Bonus: Normalizuj matici (odečti průměr, vyděl standardní odchylkou).
    """)
    return


if __name__ == "__main__":
    app.run()
