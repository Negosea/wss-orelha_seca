from .models import Material

def calcular_quantidade_montantes(comprimento, altura, tipo_parede):
    """
    Calcula a quantidade de montantes para uma parede de Drywall.

    Args:
        comprimento (float): Comprimento da parede em metros.
        altura (float): Altura da parede em metros.
        tipo_parede (str): Tipo da parede ("40", "70" ou "90").

    Returns:
        int: Quantidade de montantes necessários.
    """

    ESPACAMENTO_MONTANTES = 0.60  # Espaçamento padrão em metros

    # Calcula a quantidade de montantes na horizontal
    montantes_horizontais = int(comprimento / ESPACAMENTO_MONTANTES) + 1

    # Calcula a quantidade de montantes na vertical (se a altura for maior que 3m)
    montantes_verticais = 0
    if altura > 3:
        montantes_verticais = int(altura / 3) + 1

    # Ajusta a quantidade de montantes de acordo com o tipo de parede
    if tipo_parede == "70":
        montantes_horizontais += 1
    elif tipo_parede == "90":
        montantes_horizontais += 2

    # Calcula a quantidade total de montantes
    total_montantes = montantes_horizontais * (montantes_verticais + 1)

    return total_montantes


def calcular_quantidade_placas(comprimento, altura, tipo_parede, lados_plaqueados):
    """
    Calcula a quantidade de placas de Drywall para uma parede.

    Args:
        comprimento (float): Comprimento da parede em metros.
        altura (float): Altura da parede em metros.
        tipo_parede (str): Tipo da parede ("40", "70" ou "90").
        lados_plaqueados (int): Quantidade de lados a serem plaqueados (1 ou 2).

    Returns:
        int: Quantidade de placas de Drywall necessárias.
    """

    # Considera a área da placa de Drywall (1.20m x 2.40m)
    AREA_PLACA = 1.20 * 2.40  # Em metros quadrados

    # Calcula a área da parede
    area_parede = calcular_area_parede(comprimento, altura)

    # Calcula a quantidade de placas
    quantidade_placas = int(area_parede / AREA_PLACA) * lados_plaqueados

    # Ajusta a quantidade de placas de acordo com o tipo de parede
    if tipo_parede == "70":
        quantidade_placas += 1
    elif tipo_parede == "90":
        quantidade_placas += 2

    return quantidade_placas


def calcular_materiais(comprimento, altura, tipo_parede, lados_plaqueados):
    """
    Calcula a quantidade de materiais para uma parede de Drywall.

    Args:
        comprimento (float): Comprimento da parede em metros.
        altura (float): Altura da parede em metros.
        tipo_parede (str): Tipo da parede ("40", "70" ou "90").
        lados_plaqueados (int): Quantidade de lados a serem plaqueados (1 ou 2).

    Returns:
        dict: Dicionário com a quantidade de cada material.
    """

    # Calcula a quantidade de montantes
    montantes = calcular_quantidade_montantes(comprimento, altura, tipo_parede)

    # Calcula a quantidade de placas
    placas = calcular_quantidade_placas(comprimento, altura, tipo_parede, lados_plaqueados)

    # TODO: Calcular a quantidade de outros materiais (parafusos, massa corrida, etc.)

    return {
        "montantes": montantes,
        "placas": placas,
        # Outros materiais serão adicionados aqui
    }


from .models import Material

# ... (outras funções)

def calcular_quantidade_parafusos(area_parede, tipo_parede, espacamento_montantes):
    """Calcula a quantidade de parafusos para fixar as placas de drywall nos montantes.

    Args:
      area_parede: Área da parede em metros quadrados.
      tipo_parede: Tipo da parede ("40", "70" ou "90").
      espacamento_montantes: Espaçamento entre os montantes em metros.

    Returns:
      Quantidade de parafusos estimada.
    """

    # Define a quantidade de parafusos por metro quadrado de acordo com o tipo de parede e espaçamento
    if tipo_parede == "40" and espacamento_montantes <= 0.60:
        parafusos_por_m2 = 20  # 20 parafusos por m2 para parede 40 com espaçamento <= 60cm
    elif tipo_parede == "70" or (tipo_parede == "40" and espacamento_montantes > 0.60):
        parafusos_por_m2 = 25  # 25 parafusos por m2 para parede 70 ou parede 40 com espaçamento > 60cm
    elif tipo_parede == "90":
        parafusos_por_m2 = 30  # 30 parafusos por m2 para parede 90
    else:
        parafusos_por_m2 = 20  # Valor padrão caso o tipo de parede não seja reconhecido

    # Calcula a quantidade total de parafusos
    quantidade_parafusos = int(area_parede * parafusos_por_m2)

    return quantidade_parafusos

class Guia:
    def __init__(self, tipo, comprimento):
        """
        Inicializa um objeto Guia.

        Args:
            tipo (str): Tipo da guia ("teto", "parede").
            comprimento (float): Comprimento da guia em metros.
        """
        self.tipo = tipo
        self.comprimento = comprimento

    def calcular_quantidade(self, parede=None, forro=None):
        """
        Calcula a quantidade de guias necessárias, considerando o tipo e as dimensões da parede ou forro.

        Args:
            parede (Parede, optional): Objeto Parede. Defaults to None.
            forro (Forro, optional): Objeto Forro. Defaults to None.

        Returns:
            int: Quantidade de guias em metros.
        """
        quantidade = 0
        if parede:
            if parede.tipo == "40":
                quantidade = (parede.comprimento + parede.altura) * 2  # Guia em cima e embaixo
            elif parede.tipo == "70":
                quantidade = (parede.comprimento + parede.altura) * 3  # Guia em cima, no meio e embaixo
            elif parede.tipo == "90":
                quantidade = (parede.comprimento + parede.altura) * 4  # Guia em cima, no meio e embaixo
        elif forro:
            quantidade = (forro.comprimento + forro.largura) * 2  # Guia no perímetro do forro

        return quantidade
