from extrator_dados_abertos.crawling.pipelines.vagas_pipeline import (
    VagasPipeline,
)


class TestVagasPipeline:
    @classmethod
    def setup_class(cls):
        cls.urls_test = [
            'https://localhost.com/segrt/cargos%20vagos%20e%20vacancia/CargosVagosVacancias_202210.ods',
            'https://localhost.com/segrt/cargos%20vagos%20e%20vacancia/CargosVagosVacancias_202210.xlsx',
            'https://localhost.com/segrt/LotOrgao_DistOcupVagas%20-%20201909.xlsx',
            'https://localhost.com/segrt/LotOrgao_DistOcupVagas%20-%20201909.ods',
        ]
        cls.vagas_pipeline = VagasPipeline(store_uri='data')

    def test_renomeacao_de_planilhas_de_vagas_por_data_de_criacao(self):
        results_test = [
            ('202210', '.ods'),
            ('202210', '.xlsx'),
            ('201909', '.xlsx'),
            ('201909', '.ods'),
        ]

        for index, url_test in enumerate(self.urls_test):
            assert results_test[index] == self.vagas_pipeline._rename(url_test)

    def test_padrao_nome_planilhas_vagas(self):
        results_test = [
            '202210.ods',
            '202210.xlsx',
            '201909.xlsx',
            '201909.ods',
        ]

        for index, url_test in enumerate(self.urls_test):
            self.url = url_test
            assert results_test[index] == self.vagas_pipeline.file_path(self)
