from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from extrator_dados_abertos.crawling.items.vagas_item import VagasItem


class VagasSpider(CrawlSpider):

    name = 'vagas'
    allowed_domains = ['repositorio.dados.gov.br']
    start_urls = ['https://repositorio.dados.gov.br/segrt/']

    rules = (
        Rule(
            LinkExtractor(
                allow=(
                    r'LotOrgao_DistOcupVagas.*.xlsx|LotOrgao_DistOcupVagas.*.ods',
                    r'cargos%20vagos%20e%20vacancia',
                ),
                deny_extensions=(r''),
            ),
            callback='parse_item',
            follow=True,
        ),
    )

    def parse_item(self, response):
        yield VagasItem(file_urls=[response.url], files=[response])
