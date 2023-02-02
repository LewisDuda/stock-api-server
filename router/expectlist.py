from fastapi import APIRouter
from typing import Optional
from config.database import database_config
import config.util as util

expectlist_router = APIRouter()
expect_collection = database_config('expect')


@expectlist_router.get('/expectlist', status_code=200)
def expectlist(year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None) -> dict:
    datetimestamp = util.date_to_timestamp(year, month, day)
    queries = {"date": datetimestamp}
    search_res = util.db_search(expect_collection, queries)
    if len(search_res) == 0:
        return {"data": []}
    dataList = search_res[0]['list']
    return {"data": dataList}
