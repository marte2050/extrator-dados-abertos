import re


class FilterURL:
    def __init__(self) -> None:
        """
        Descrição:
            No construtor definimos os padrões de extensões válidas a serem identificados,
            como: xlsx, txt e ods
        """
        self.xlsx = re.compile('.*xlsx')
        self.txt = re.compile('.*txt')
        self.ods = re.compile('.*ods')

    def filter_urls_by_extensions(self, list_texts: list) -> dict[str]:
        """
        Descrição:
            Transforma uma lista de urls em um dicionário, ao qual
            serão separados com base na extensão que podem ser do tipo xlsx, ods e txt.

        Args:
            list_texts (list): Lista de urls.

        Returns:
            Retorna um dicionário, ao qual terá uma lista de urls separados por tipo.

        Raises:
            TypeError: Caso parâmetro informado seja diferente de uma string é lançado um erro!

        Examples:
            >>> filter_url = FilterURL()
            >>> filter_url.filter_urls_by_extensions(['list_texts'])
            {'xlsx': [], 'ods': [], 'txt': []}
        """

        try:
            list_historical_xlsx = list(filter(self.xlsx.match, list_texts))
            list_historical_ods = list(filter(self.ods.match, list_texts))
            list_historical_txt = list(filter(self.txt.match, list_texts))

            list_historical_xlsx.sort()
            list_historical_ods.sort()
            list_historical_txt.sort()

        except TypeError:
            raise TypeError(
                'Erro o parâmetro list_texts deve ser uma lista de urls!'
            )

        return {
            'xlsx': list_historical_xlsx,
            'ods': list_historical_ods,
            'txt': list_historical_txt,
        }
