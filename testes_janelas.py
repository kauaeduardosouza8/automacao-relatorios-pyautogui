import pygetwindow as gw
import pyautogui


ordenar_cliente = [136,38]
periodo_inicial = [27,267]


janelas = gw.getWindowsWithTitle('conferência de venda por cupom')


x_mouse = 561
y_mouse = 488


left = janelas[0].left
top = janelas[0].top


x_relativo = left - x_mouse 
y_relativo = top - y_mouse 


print(x_relativo, y_relativo)


