import pytest

from extrator_dados_abertos.utils.filters import FilterURL


class TestFilterURL:
    def test_lanca_um_erro_se_parametro_do_metodo_filter_urls_by_extensions_nao_for_uma_lista(
        self,
    ):

        message = f'Erro o parâmetro list_texts deve ser uma lista de urls!'

        with pytest.raises(TypeError) as excinfo:
            filter_url = FilterURL()
            filter_url.filter_urls_by_extensions(1)

        assert str(excinfo.value) == message

    def test_filter_urls_by_extensions_deve_retornar_um_dicionario(self):

        list_text = [
            'https://localhost.com/example.xlsx',
            'https://localhost.com/example.txt',
            'https://localhost.com/example.odt',
            'https://localhost.com/example.pdf',
        ]

        result_expected = {
            'xlsx': ['https://localhost.com/example.xlsx'],
            'odt': ['https://localhost.com/example.odt'],
            'txt': ['https://localhost.com/example.txt'],
        }

        filter_url = FilterURL()
        result_function = filter_url.filter_urls_by_extensions(list_text)

        assert result_function == result_expected
