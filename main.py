
from lib.triangulo import get_area as get_area_triangulo
lado = 6
area_cuadrado = get_area(lado)
print(f"El área del cuadrado de lado {lado} es {area_cuadrado}")

# Código para el triángulo
base_triangulo = 4
altura_triangulo = 3
area_triangulo = get_area_triangulo(base_triangulo, altura_triangulo)
print(f"El área del triángulo de base {base_triangulo} y altura {altura_triangulo} es {area_triangulo}")

# Nuevo código para el rectángulo
base = 4
altura = 3
area_rectangulo = get_area(base, altura)
print(f"El área del rectángulo de base {base} y altura {altura} es {area_rectangulo}")

