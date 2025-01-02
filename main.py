from api_manager import ApiManager
from bot_manager import BotManager
import unicodedata

STOCK = "TSLA"

api_manager = ApiManager()
bot_manager = BotManager()

if api_manager.is_change_signif():
    top_3_news = api_manager.get_top_3_news_data()
    icon = "🔺"
    if api_manager.stock_change < 0:
        icon = "🔻"
    for each_news in top_3_news:
        message = f"""
        {STOCK}: {icon} {api_manager.stock_change}\nHeadline: {unicodedata.normalize('NFKC', each_news["title"])}\nBrief: {unicodedata.normalize('NFKC', each_news["description"])}
        """
        bot_manager.send_message(message)

