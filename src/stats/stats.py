class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.

        Args:
            numeros (list): Lista de números

        Returns:
            float: La media aritmética de los números

        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.

        Args:
            numeros (list): Lista de números

        Returns:
            float: El valor mediano

        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        if not numeros:
            return 0
        numeros_ord = sorted(numeros)
        n = len(numeros_ord)
        if n % 2 == 1:
            return numeros_ord[n // 2]
        else:
            return (numeros_ord[n // 2 - 1] + numeros_ord[n // 2]) / 2

    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.

        Args:
            numeros (list): Lista de números

        Returns:
            number: El valor más frecuente

        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        if not numeros:
            return None
        conteo = {}
        for num in numeros:
            conteo[num] = conteo.get(num, 0) + 1
        max_frecuencia = max(conteo.values())
        for num in numeros:
            if conteo[num] == max_frecuencia:
                return num
        return None

    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.

        Args:
            numeros (list): Lista de números

        Returns:
            float: La desviación estándar

        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        if not numeros:
            return 0
        media = sum(numeros) / len(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza**0.5

    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.

        Args:
            numeros (list): Lista de números

        Returns:
            float: La varianza

        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        if not numeros:
            return 0
        media = sum(numeros) / len(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)

    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).

        Args:
            numeros (list): Lista de números

        Returns:
            number: La diferencia entre max y min

        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
