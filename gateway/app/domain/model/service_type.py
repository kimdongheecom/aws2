from enum import Enum
import os


class ServiceType(str, Enum):
    NEWS = "news"
    SASB = "sasb"
    ISSUEPOOL = "issuepool"

# ✅ 환경 변수에서 서비스 URL 가져오기
NEWS_SERVICE_URL = os.getenv("NEWS_SERVICE_URL")
SASB_SERVICE_URL = os.getenv("SASB_SERVICE_URL")
ISSUEPOOL_SERVICE_URL = os.getenv("ISSUEPOOL_SERVICE_URL")

SERVICE_URLS = {
    ServiceType.NEWS: NEWS_SERVICE_URL,
    ServiceType.SASB: SASB_SERVICE_URL,
    ServiceType.ISSUEPOOL: ISSUEPOOL_SERVICE_URL,
}