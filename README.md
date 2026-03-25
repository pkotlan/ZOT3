# ZOT3

> Zpracování a analýza obrazů

1. Digitální obraz, barva a ROI (Region of Interest)
    - Načítání a ukládání dat (io), barevné modely (RGB vs. HSV), separace
    kanálů, ořez obrazu (slicing), změna velikosti (rescale), dávkové
    zpracování souborů (glob).

2. Filtry
    - Lineární filtry (Gauss), nelineární filtry (Medián, Bilaterální filtr),
    ostření (Unsharp mask), Laplacian, odstranění artefaktů (Inpainting).

3. Jasové korekce a práce s histogramem
    - Výpočet a vizualizace histogramu, Gamma korekce, roztažení kontrastu
    (rescaling intensity), lokální adaptivní ekvalizace (CLAHE).

1. Binarizce    
    - Globální prahování (Otsu, Yen, Triangle), lokální adaptivní prahování
    (řešení nerovnoměrného osvětlení), hysterezní prahování.

5. Morfologické operátory
    - Eroze, dilatace, otevření, uzavření, plnění děr (binary fill holes),
    white_tophat (detekce světlých bodů), skeletonizace (kostry objektů).

6. Segmentace
    - Vzdálenostní transformace (Euclidean Distance Transform), hledání lokálních
    maxim (peak_local_max), tvorba markerů, algoritmus Watershed, čištění
    hranic (clear_border).

7. Extrakce příznaků a měření (Feature Extraction)
    - Labeling (číslování propojených komponent), měření vlastností
    (regionprops – plocha, obvod, excentricita, orientace), filtrování objektů
    podle vlastností, export dat do tabulky (pandas).

8. Validace a vyhodnocení přesnosti
    - Tvorba Ground Truth (anotace), Jaccard index (IoU), Dice koeficient,
    matice záměn (pixel-level confusion matrix).



pripravit snimky z zelvusek (i nova videa) a BALu

---

1. filtry - Gauss, Unsharp masking
2. jas, práce s histogramem - rescale intensity, ekvalizace histogramů
3. binarizace (globální/adaptivní) - otsu aj.
4. Morfologické operátory
5. segmentace - vzdálenostní transformace + hledání maxim + watershed
6. feature extraction
7. vyhodnocovací metriky - dice, jaccard
