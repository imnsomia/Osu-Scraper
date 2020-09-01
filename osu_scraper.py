from scrape import Scraper

class User():
    def __init__(self, user):
        self.username = user
        self.scrape = Scraper()

    def api(self, method:str) -> str:
        return self.scrape.methods(method, self.username)

    def dict_user_rank(self) -> str:
        return self.scrape.user_rank_dict(self.username)

    def dict_user_info(self) -> str:
        return self.scrape.user_info_dict(self.username)
