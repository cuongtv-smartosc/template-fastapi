from typing import Tuple, List, Any

from pydantic import parse_obj_as

from app.models.charger_model import ChargerModel, ChargerResponse


class ChargerModelCrud:

    async def get_all_charger_model(self) -> Tuple[List[ChargerResponse], Any]:
        data, page = ChargerModel.fetch_all()
        results = [parse_obj_as(ChargerResponse, result) for result in data]
        return results, page
