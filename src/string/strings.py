class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """

    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).

        Args:
            texto (str): Cadena a verificar

        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_limpio = ""
        for c in texto.lower():
            if c.isalnum():
                texto_limpio += c
        return texto_limpio == texto_limpio[::-1]

    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().

        Args:
            texto (str): Cadena a invertir

        Returns:
            str: Cadena invertida
        """
        resultado = ""
        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        return resultado

    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.

        Args:
            texto (str): Cadena para contar vocales

        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for c in texto:
            if c in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.

        Args:
            texto (str): Cadena para contar consonantes

        Returns:
            int: Número de consonantes en la cadena
        """
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        contador = 0
        for c in texto:
            if c in consonantes and c.lower() != "y":
                contador += 1
        return contador

    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).

        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena

        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        s1 = ""
        for c in texto1.lower():
            if c.isalnum():
                s1 += c
        s2 = ""
        for c in texto2.lower():
            if c.isalnum():
                s2 += c
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)

    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.

        Args:
            texto (str): Cadena para contar palabras

        Returns:
            int: Número de palabras en la cadena
        """
        if not texto.strip():
            return 0
        contador = 0
        en_palabra = False
        for c in texto:
            if c != " ":
                if not en_palabra:
                    contador += 1
                    en_palabra = True
            else:
                en_palabra = False
        return contador

    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.

        Args:
            texto (str): Cadena

        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        resultado = ""
        en_palabra = False
        for i, c in enumerate(texto):
            if c == " ":
                resultado += c
                en_palabra = False
            elif not en_palabra:
                resultado += c.upper()
                en_palabra = True
            else:
                resultado += c
        return resultado

    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.

        Args:
            texto (str): Cadena con posibles espacios duplicados

        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = ""
        ultimo_espacio = False
        for c in texto:
            if c == " ":
                if not ultimo_espacio:
                    resultado += c
                    ultimo_espacio = True
            else:
                resultado += c
                ultimo_espacio = False
        return resultado

    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().

        Args:
            texto (str): Cadena a verificar

        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if not texto:
            return False
        if texto[0] in "+-":
            texto = texto[1:]
        if not texto:
            return False
        for c in texto:
            if c < "0" or c > "9":
                return False
        return True

    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.

        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra

        Returns:
            str: Cadena cifrada
        """
        resultado = ""
        for c in texto:
            if c.isalpha():
                ascii_inicio = 65 if c.isupper() else 97
                posicion = (ord(c) - ascii_inicio + desplazamiento) % 26
                resultado += chr(ascii_inicio + posicion)
            else:
                resultado += c
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.

        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra

        Returns:
            str: Cadena descifrada
        """
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().

        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar

        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if not subcadena:
            return []
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            if texto[i : i + len_sub] == subcadena:
                posiciones.append(i)
        return posiciones
