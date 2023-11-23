import re
from pathlib import Path

from scrapy.pipelines.files import FilesPipeline


class VagasPipeline(FilesPipeline):
    def _rename(self, url) -> tuple:
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
        media_guid, media_ext = self._rename(request.url)
        return f'{media_guid}{media_ext}'
