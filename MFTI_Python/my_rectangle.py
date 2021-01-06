import graphics as graphics

window = gr.GraphWin("Russian Game", 300, 300)
alpha = 0.2

def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)) .draw(window)   #M ссылка на А, N ссылка на В
    # gr.Line(gr.Point(*B), gr.Point(*C)) .draw(window)  Создадим вместо этого цикл
    # gr.Line(gr.Point(*C), gr.Point(*D)) .draw(window)
    # gr.Line(gr.Point(*D), gr.Point(*A)) .draw(window)
    A1 = (A[0])*(1-alpha) + B[0]*alpha, (A[1])*(1-alpha) + B[1]*alpha
    B1 = (B[0])*(1-alpha) + C[0]*alpha, (B[1])*(1-alpha) + C[1]*alpha
    C1 = (C[0])*(1-alpha) + D[0]*alpha, (C[1])*(1-alpha) + D[1]*alpha
    D1 = (D[0])*(1-alpha) + A[0]*alpha, (D[1])*(1-alpha) + A[1]*alpha
    fractal_rectangle(A1, B1, C1, D1, deep-1)

my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))
my_rectangle.draw(window)