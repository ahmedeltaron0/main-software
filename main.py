# ALL IMOPRTS GO HERE 

from functions.get_audio import get_audio
from functions.gemini import get_keyword_for_query
from functions.check_keyword import check_keyword


# ALL FUNCTION CALLS GO HERE

captured_voice = get_audio()
response_keyword = get_keyword_for_query(captured_voice)
result = check_keyword(response_keyword)

