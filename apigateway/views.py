import json

import requests

from rest_framework.views import APIView
from rest_framework.response import Response


class GameDetails(APIView):
    def get_game(self, game_id, rawg_key, header):
        link_to_game = f"https://api.rawg.io/api/games/{game_id}?key={rawg_key}"

        game_data = requests.get(link_to_game, header)

        if game_data.status_code == requests.codes.ok:
            return game_data
        else:
            return game_data.status_code

    def get_game_addition(self, game_id, rawg_key, header):
        link_to_game = f"https://api.rawg.io/api/games/{game_id}/additions?key={rawg_key}"

        game_data = requests.get(link_to_game, header)

        if game_data.status_code == requests.codes.ok:
            return game_data
        else:
            return game_data.status_code

    def get(self, game_id):
        game_additions = self.get_game_addition(game_id,
                               rawg_key='cb0ae82651a940548b08235b486761d4',
                               header="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/"
                                        "537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/"
                                        "20.4.2.150 (beta) Yowser/2.5 Safari/537.36")

        game_additions_data = json.loads(game_additions.content)

        game_additions_data_filtered = '{'

        count = None

        for key, value in game_additions_data.items():
            if key == 'count':
                count = value
            if key == 'count' or key == 'next' or key == 'previous':
                game_additions_data_filtered += f'"{key}":"{value}",'

            if key == 'results':
                if count == 0:
                    game_additions_data_filtered += '"results": []}'
                else:
                    game_additions_data_filtered += '"results": ['
                for i in range(count):
                    game_additions_data_filtered += "{"
                    for key, value in game_additions_data['results'][i].items():
                        if key == 'id' or key == 'slug' or key == 'name':
                            game_additions_data_filtered += f'"{key}":"{value}",'
                        if key == 'background_image':
                            game_additions_data_filtered += f'"{key}":"{value}"'

                    if i != count - 1:
                        game_additions_data_filtered += '},'
                    else:
                        game_additions_data_filtered += '}]}'

        game_additions_data_filtered = '{"additions":' + game_additions_data_filtered + "}"

        game = self.get_game(game_id,
                                      rawg_key='cb0ae82651a940548b08235b486761d4',
                                      header="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/"
                                             "537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/"
                                             "20.4.2.150 (beta) Yowser/2.5 Safari/537.36")

        game_data = json.loads(game.content)

        game_data.update(json.loads(game_additions_data_filtered))

        return Response(game_data)
