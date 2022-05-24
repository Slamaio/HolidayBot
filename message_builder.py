from parser import Parser
from config import importance

class MessageBuilder:
    def __init__(self) -> None:
        pass

    def date(self, url: str):
        date = Parser(url).getDate()
        return date

    def message(self, url: str, level: int = 0) -> str:
        date = self.date(url)
        holidays = self.holidays(url)
        answer_text = f"{date}\n\n{holidays}"

        return answer_text
    
    def holidays(self, url: str, level: int = 0) -> str:
        holidays = ""
        for holiday in Parser(url).getHolidays(level):
            holidays += f"{importance[level][0]} {holiday}\n"

        return holidays