import re
from pathlib import Path

from scrapy.pipelines.files import FilesPipeline


class VagasPipeline(FilesPipeline):
    def _rename(self, url: str) -> tuple:
        """
        Descrição:
            Método responsável por receber uma string contendo o endereço da URL
            e posteriormente obter o nome do arquivo e a extensão.
            Após obter o nome da extensão é feito o processo de remover todos os caracteres
            que não sejam numericos de modo a encontrar a data de criação do arquivo.

        args:
            url (str): Endereço do arquivo a ser baixado

        Returns:
            Retorna uma tupla, ao qual terá como parâmetro o nome do arquivo e a extensão
        """
        file_regex = re.compile('/[C,L].*.xlsx$|/[C,L].*.ods$')
        media_ext = Path(url).suffix
        file_name_original = file_regex.findall(url)[0]
        media_guid_digit = ''.join(
            character
            for character in file_name_original
            if character.isdigit()
        )
        size_file_name = len(media_guid_digit)
        media_guid = (
            media_guid_digit[4:] if size_file_name == 10 else media_guid_digit
        )
        return media_guid, media_ext

    def file_path(
        self, request, response=None, info=None, *, item=None
    ) -> str:
        """
        Descrição:
            Método responsável por renomear o arquivo baixado

        args:
            request (Request): request
            response (Response): response
            info (Info): info
            item (VagasItem): Objeto item vagas

        Returns:
            Retorna uma string com o nome do arquivo e extensão
        """
        media_guid, media_ext = self._rename(request.url)
        return f'{media_guid}{media_ext}'
