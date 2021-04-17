import requests


class RawgRequests:
    @staticmethod
    def creator_roles_request(rawg_key, header):
        link_to_creator_roles = f"https://api.rawg.io/api/creator-roles?key={rawg_key}"

        creator_roles_data = requests.get(link_to_creator_roles, header)

        if creator_roles_data.status_code == requests.codes.ok:
            return creator_roles_data
        else:
            return creator_roles_data.status_code

    @staticmethod
    def creator_list_request(rawg_key, header):
        link_to_creator_list = f"https://api.rawg.io/api/creators?key={rawg_key}"

        creator_list_data = requests.get(link_to_creator_list, header)

        if creator_list_data.status_code == requests.codes.ok:
            return creator_list_data
        else:
            return creator_list_data.status_code

    @staticmethod
    def creator_request(creator_id, rawg_key, header):
        link_to_creator_list = f"https://api.rawg.io/api/creators/{creator_id}?key={rawg_key}"

        creator_list_data = requests.get(link_to_creator_list, header)

        if creator_list_data.status_code == requests.codes.ok:
            return creator_list_data
        else:
            return creator_list_data.status_code
