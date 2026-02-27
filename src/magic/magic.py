class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """

    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.

        Args:
            n (int): Posición en la secuencia (empezando desde 0)

        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.

        Args:
            n (int): Cantidad de números a generar

        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n <= 0:
            return []
        secuencia = [0]
        if n == 1:
            return secuencia
        secuencia.append(1)
        for i in range(2, n):
            secuencia.append(secuencia[i - 1] + secuencia[i - 2])
        return secuencia

    def es_primo(self, n):
        """
        Verifica si un número es primo.

        Args:
            n (int): Número a verificar

        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.

        Args:
            n (int): Límite superior para generar primos

        Returns:
            list: Lista de números primos hasta n
        """
        primos = []
        for num in range(2, n + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos

    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).

        Args:
            n (int): Número a verificar

        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n <= 1:
            return False
        suma_divisores = 0
        for i in range(1, n):
            if n % i == 0:
                suma_divisores += i
        return suma_divisores == n

    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.

        Args:
            filas (int): Número de filas a generar

        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        """
        Calcula el factorial de un número.

        Args:
            n (int): Número para calcular su factorial

        Returns:
            int: El factorial de n
        """
        if n < 0:
            return None
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.

        Args:
            a (int): Primer número
            b (int): Segundo número

        Returns:
            int: El máximo común divisor de a y b
        """
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.

        Args:
            a (int): Primer número
            b (int): Segundo número

        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.

        Args:
            n (int): Número para sumar sus dígitos

        Returns:
            int: La suma de los dígitos de n
        """
        if n == 0:
            return 0
        n = abs(n)
        suma = 0
        while n > 0:
            suma += n % 10
            n //= 10
        return suma

    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).

        Args:
            n (int): Número a verificar

        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        if n < 0:
            return False
        digitos = []
        temp = n
        while temp > 0:
            digitos.append(temp % 10)
            temp //= 10
        num_digitos = len(digitos)
        suma = sum(d**num_digitos for d in digitos)
        return suma == n

    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).

        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada

        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        if not matriz:
            return False
        n = len(matriz)
        suma_magica = sum(matriz[0])

        for i in range(n):
            if sum(matriz[i]) != suma_magica:
                return False

        for j in range(n):
            suma_col = sum(matriz[i][j] for i in range(n))
            if suma_col != suma_magica:
                return False

        suma_diag1 = sum(matriz[i][i] for i in range(n))
        if suma_diag1 != suma_magica:
            return False

        suma_diag2 = sum(matriz[i][n - 1 - i] for i in range(n))
        if suma_diag2 != suma_magica:
            return False

        return True
