import marimo

__generated_with = "0.20.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import imageio.v3 as iio
    import numpy as np

    return iio, mo


@app.cell
def _(iio, mo):
    img = iio.imread("site/C2.tuns.png")
    img = img.astype(float)
    mo.image(img)
    return (img,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grayscaling

    $$Y = 1/3 \cdot R + 1/3 \cdot G + 1/3 \cdot B$$

    ---

    $$Y = 0.2125 \cdot R + 0.7154 \cdot G + 0.0721 \cdot B$$
    """)
    return


@app.cell
def _(img, mo):
    from skimage.color import rgb2gray

    grayscale = rgb2gray(img)

    mo.image(grayscale)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## HSV (hue, saturation, value)

    Nejprve definujeme pomocné proměnné:

    $$C_{max} = \max(R, G, B)$$
    $$C_{min} = \min(R, G, B)$$
    $$\Delta = C_{max} - C_{min}$$

    **Výpočet Hue (H):**
    $$H = \begin{cases} 0^\circ & \text{pokud } \Delta = 0 \\ 60^\circ \times \left( \frac{G - B}{\Delta} \bmod 6 \right) & \text{pokud } C_{max} = R \\ 60^\circ \times \left( \frac{B - R}{\Delta} + 2 \right) & \text{pokud } C_{max} = G \\ 60^\circ \times \left( \frac{R - G}{\Delta} + 4 \right) & \text{pokud } C_{max} = B \end{cases}$$

    **Výpočet Saturation (S):**
    $$S = \begin{cases} 0 & \text{pokud } C_{max} = 0 \\ \frac{\Delta}{C_{max}} & \text{jinak} \end{cases}$$

    **Výpočet Value (V):**
    $$V = C_{max}$$
    """)
    return


@app.cell
def _(img, mo):
    from skimage.color import rgb2hsv

    hsv = rgb2hsv(img)

    mo.image(hsv)
    mo.carousel(
        [
            mo.image(hsv[:, :, 0], caption="H"),
            mo.image(hsv[:, :, 1], caption="S"),
            mo.image(hsv[:, :, 2], caption="V"),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## HSI (hue, saturation, intensity)

    **Výpočet Intensity (I):**
    $$I = \frac{R + G + B}{3}$$

    **Výpočet Saturation (S):**
    $$S = \begin{cases} 0 & \text{pokud } I = 0 \\ 1 - \frac{\min(R, G, B)}{I} & \text{jinak} \end{cases}$$

    **Výpočet Hue (H):**
    Nejprve si definujeme úhel $\theta$:

    $$\theta = \arccos\left( \frac{\frac{1}{2}((R - G) + (R - B))}{\sqrt{(R - G)^2 + (R - B)(G - B)}} \right)$$

    Z něj pak určíme finální odstín:

    $$H = \begin{cases} \theta & \text{pokud } B \le G \\ 360^\circ - \theta & \text{pokud } B > G \end{cases}$$
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
