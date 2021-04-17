import requests


class RawgRequests:
    @staticmethod
    def creator_roles_request(rawg_key, header):
        link_to_creator_roles = f"https://api.rawg.io/api/creator-roles?key={rawg_key}"

        creator_roles_data = requests.get(link_to_creator_roles, header)

        if creator_roles_data.status_code == requests.codes.ok:
            return creator_roles_data
        else:
            if creator_roles_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return creator_roles_data.status_code

    @staticmethod
    def creators_list_request(rawg_key, header, page_number):
        if page_number is None:
            link_to_creators_list = f"https://api.rawg.io/api/creators?key={rawg_key}"
        else:
            link_to_creators_list = f"https://api.rawg.io/api/creators?key={rawg_key}&page={page_number}"

        creators_list_data = requests.get(link_to_creators_list, header)

        if creators_list_data.status_code == requests.codes.ok:
            return creators_list_data
        else:
            if creators_list_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return creators_list_data.status_code

    @staticmethod
    def creator_request(creator_id, rawg_key, header):
        link_to_creator = f"https://api.rawg.io/api/creators/{creator_id}?key={rawg_key}"

        creator_data = requests.get(link_to_creator, header)

        if creator_data.status_code == requests.codes.ok:
            return creator_data
        else:
            if creator_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return creator_data.status_code

    @staticmethod
    def developers_list_request(rawg_key, header, page_number):
        if page_number is None:
            link_to_developers_list = f"https://api.rawg.io/api/developers?key={rawg_key}"
        else:
            link_to_developers_list = f"https://api.rawg.io/api/developers?key={rawg_key}&page={page_number}"

        developers_list_data = requests.get(link_to_developers_list, header)

        if developers_list_data.status_code == requests.codes.ok:
            return developers_list_data
        else:
            if developers_list_data.status_code == requests.codes.not_found:
                return '{"detail":"Page not found."}'
            else:
                return developers_list_data.status_code

    @staticmethod
    def developer_request(developer_id, rawg_key, header):
        link_to_developer = f"https://api.rawg.io/api/developers/{developer_id}?key={rawg_key}"

        developer_data = requests.get(link_to_developer, header)

        if developer_data.status_code == requests.codes.ok:
            return developer_data
        else:
            if developer_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return developer_data.status_code

    @staticmethod
    def games_list_request(rawg_key, header, page_number):
        if page_number is None:
            link_to_games_list = f"https://api.rawg.io/api/games?key={rawg_key}"
        else:
            link_to_games_list = f"https://api.rawg.io/api/games?key={rawg_key}&page={page_number}"

        games_list_data = requests.get(link_to_games_list, header)

        if games_list_data.status_code == requests.codes.ok:
            return games_list_data
        else:
            if games_list_data.status_code == requests.codes.not_found:
                return '{"detail":"Page not found."}'
            else:
                return games_list_data.status_code

    @staticmethod
    def game_request(game_id, rawg_key, header):
        link_to_game = f"https://api.rawg.io/api/games/{game_id}?key={rawg_key}"

        game_data = requests.get(link_to_game, header)

        if game_data.status_code == requests.codes.ok:
            return game_data
        else:
            if game_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return game_data.status_code

    @staticmethod
    def game_additions_request(game_id, rawg_key, header):
        link_to_game_additions = f"https://api.rawg.io/api/games/{game_id}/additions?key={rawg_key}"

        game_additions_data = requests.get(link_to_game_additions, header)

        if game_additions_data.status_code == requests.codes.ok:
            return game_additions_data
        else:
            if game_additions_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return game_additions_data.status_code

    @staticmethod
    def game_development_team_request(game_id, rawg_key, header):
        link_to_game_development_team = f"https://api.rawg.io/api/games/{game_id}/development-team?key={rawg_key}"

        game_development_team_data = requests.get(link_to_game_development_team, header)

        if game_development_team_data.status_code == requests.codes.ok:
            return game_development_team_data
        else:
            if game_development_team_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return game_development_team_data.status_code

    @staticmethod
    def game_series_request(game_id, rawg_key, header):
        link_to_game_series = f"https://api.rawg.io/api/games/{game_id}/game-series?key={rawg_key}"

        game_series_data = requests.get(link_to_game_series, header)

        if game_series_data.status_code == requests.codes.ok:
            return game_series_data
        else:
            if game_series_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
            else:
                return game_series_data.status_code
