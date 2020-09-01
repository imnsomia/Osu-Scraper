import requests, time, json
from bs4 import BeautifulSoup

class Scraper(object):
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language" : "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding" : "gzip, deflate",
        "DNT" : "1",
        }
        self.info_user = ("")
        self.info_rank = ("")

    def req_user(self, user:str) -> str:
        with self.session.get(f"https://osu.ppy.sh/users/{user}", headers=self.headers) as peticion:
            try:
                soup = BeautifulSoup(peticion.content, 'html.parser')
                scuffed_json_info = soup.find_all('script', id="json-user")
                scuffed_json_ranks = soup.find_all('script', id="json-extras")
                scrape_json_ranks = json.loads(scuffed_json_ranks[0].contents[0].split("\n")[1].lstrip())
                scrape_json_info = json.loads(scuffed_json_info[0].contents[0].split("\n")[1].lstrip())
                self.info_user = scrape_json_info
                self.info_rank = scrape_json_ranks
            except IndexError:
                return f"[IndexError] Username {user} does not exist"

    def methods(self, method:str, user:str) -> str:
        try:
            self.req_user(user)
            if method in self.info_user:
                return self.info_user[method]
            else:
                return self.info_rank[method]
        except KeyError:
            return f"[KeyError] The method {method} does not exist"

    def user_rank_dict(self, user:str) -> str:
        self.req_user(user)
        try:
            return dict(
            scoresBest = self.info_rank["scoresBest"],
            scoresFirsts = self.info_rank["scoresFirsts"],
            scoresRecent = self.info_rank["scoresRecent"],
            beatmapPlaycounts = self.info_rank["beatmapPlaycounts"],
            favouriteBeatmapsets = self.info_rank["favouriteBeatmapsets"],
            rankedAndApprovedBeatmapsets = self.info_rank["rankedAndApprovedBeatmapsets"],
            lovedBeatmapsets = self.info_rank["lovedBeatmapsets"],
            unrankedBeatmapsets = self.info_rank["unrankedBeatmapsets"],
            graveyardBeatmapsets = self.info_rank["graveyardBeatmapsets"],
            recentActivity = self.info_rank["recentActivity"],
            recentlyReceivedKudosu = self.info_rank["recentlyReceivedKudosu"],
            )
        except TypeError:
            return f"[TypeError] User {user} not found"

    def user_info_dict(self, user:str) -> str:
        self.req_user(user)
        try:
            return dict(
            avatar_url = self.info_user["avatar_url"],
            country_code =self.info_user["country_code"],
            id = self.info_user["id"],
            is_active = self.info_user["is_active"],
            is_bot = self.info_user["is_bot"],
            is_online = self.info_user["is_online"],
            is_supporter = self.info_user["is_supporter"],
            last_visit = self.info_user["last_visit"],
            pm_friends_only = self.info_user["pm_friends_only"],
            profile_colour = self.info_user["profile_colour"],
            username = self.info_user["username"],
            cover_url = self.info_user["cover_url"],
            discord = self.info_user["discord"],
            has_supported = self.info_user["has_supported"],
            interests = self.info_user["interests"],
            join_date = self.info_user["join_date"],
            kudosu = self.info_user["kudosu"],
            lastfm = self.info_user["lastfm"],
            location = self.info_user["location"],
            max_blocks = self.info_user["max_blocks"],
            max_friends = self.info_user["max_friends"],
            occupation = self.info_user["occupation"],
            playmode = self.info_user["playmode"],
            post_count = self.info_user["post_count"],
            profile_order = self.info_user["profile_order"],
            skype = self.info_user["skype"],
            title = self.info_user["title"],
            twitter = self.info_user["twitter"],
            website = self.info_user["website"],
            country = self.info_user["country"],
            cover = self.info_user["cover"],
            is_admin = self.info_user["is_admin"],
            is_bng = self.info_user["is_bng"],
            is_full_bn = self.info_user["is_full_bn"],
            is_gmt = self.info_user["is_gmt"],
            is_limited_bn = self.info_user["is_limited_bn"],
            is_moderator = self.info_user["is_moderator"],
            active_tournament_banner = self.info_user["active_tournament_banner"],
            badges = self.info_user["badges"],
            favourite_beatmapset_count = self.info_user["favourite_beatmapset_count"],
            follower_count = self.info_user["follower_count"],
            graveyard_beatmapset_count = self.info_user["graveyard_beatmapset_count"],
            groups = self.info_user["groups"],
            loved_beatmapset_count = self.info_user["loved_beatmapset_count"],
            monthly_playcounts = self.info_user["monthly_playcounts"],
            page = self.info_user["page"],
            previous_usernames = self.info_user["previous_usernames"],
            ranked_and_approved_beatmapset_count = self.info_user["ranked_and_approved_beatmapset_count"],
            replays_watched_counts = self.info_user["replays_watched_counts"],
            scores_first_count = self.info_user["scores_first_count"],
            statistics = self.info_user["statistics"],
            support_level = self.info_user["support_level"],
            rankHistory = self.info_user["rankHistory"],
            )
        except TypeError:
            return f"[TypeError] User {user} not found"
