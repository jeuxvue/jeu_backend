import json
import requests

from apigateway.rawg import RawgRequests
from rest_framework.views import APIView
from rest_framework.response import Response
from jeu_backend.settings import RAWG_KEY, HEADER_FOR_RAWG


class GameDetailss(APIView):
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

    def get(self, request, game_id):
        game_additions = self.get_game_addition(game_id, RAWG_KEY, HEADER_FOR_RAWG)

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

        game = self.get_game(game_id, RAWG_KEY, HEADER_FOR_RAWG)

        game_data = json.loads(game.content)

        game_data.update(json.loads(game_additions_data_filtered))

        return Response(game_data)


class CreatorRoles(APIView):
    @staticmethod
    def get(request):
        creator_roles_data = RawgRequests.creator_roles_request(RAWG_KEY, HEADER_FOR_RAWG)

        if type(creator_roles_data) == str:
            creator_roles_data_json_format = json.loads(creator_roles_data.content)
        else:
            creator_roles_data_json_format = json.loads(creator_roles_data.content)

        return Response(creator_roles_data_json_format)


class CreatorsList(APIView):
    @staticmethod
    def get(request):
        page_number = request.GET.get("page")
        creator_list_data = RawgRequests.creators_list_request(RAWG_KEY, HEADER_FOR_RAWG, page_number)

        if type(creator_list_data) == str:
            creators_list_data_json_format = json.loads(creator_list_data.content)
        else:
            creators_list_data_json_format = json.loads(creator_list_data.content)

        return Response(creators_list_data_json_format)


class CreatorDetails(APIView):
    @staticmethod
    def get(request, creator_id):
        creator_data = RawgRequests.creator_request(creator_id, RAWG_KEY, HEADER_FOR_RAWG)

        if type(creator_data) == str:
            creator_data_json_format = json.loads(creator_data.content)
        else:
            creator_data_json_format = json.loads(creator_data.content)

        return Response(creator_data_json_format)


class DevelopersList(APIView):
    @staticmethod
    def get(request):
        page_number = request.GET.get("page")
        developers_list_data = RawgRequests.developers_list_request(RAWG_KEY, HEADER_FOR_RAWG, page_number)

        if type(developers_list_data) == str:
            developers_list_data_json_format = json.loads(developers_list_data)
        else:
            developers_list_data_json_format = json.loads(developers_list_data.content)

        return Response(developers_list_data_json_format)


class DeveloperDetails(APIView):
    @staticmethod
    def get(request, developer_id):
        developer_data = RawgRequests.developer_request(developer_id, RAWG_KEY, HEADER_FOR_RAWG)

        if type(developer_data) == str:
            developer_data_json_format = json.loads(developer_data)
        else:
            developer_data_json_format = json.loads(developer_data.content)

        return Response(developer_data_json_format)


class GamesList(APIView):
    @staticmethod
    def get(request):
        page_number = request.GET.get("page")
        games_list_data = RawgRequests.games_list_request(RAWG_KEY, HEADER_FOR_RAWG, page_number)

        if type(games_list_data) == str:
            games_list_data_json_format = json.loads(games_list_data)
        else:
            games_list_data_json_format = json.loads(games_list_data.content)

        return Response(games_list_data_json_format)


class GameDetails(APIView):
    @staticmethod
    def get(request, game_id):
        game_data = RawgRequests.game_request(game_id, RAWG_KEY, HEADER_FOR_RAWG)

        if type(game_data) == str:
            developer_data_json_format = json.loads(game_data)
        else:
            developer_data_json_format = json.loads(game_data.content)

        return Response(developer_data_json_format)
