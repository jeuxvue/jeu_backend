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
    def creators_list_request(rawg_key, header):
        link_to_creators_list = f"https://api.rawg.io/api/creators?key={rawg_key}"

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
    def developers_list_request(rawg_key, header):
        link_to_developers_list = f"https://api.rawg.io/api/developers?key={rawg_key}"

        developers_list_data = requests.get(link_to_developers_list, header)

        if developers_list_data.status_code == requests.codes.ok:
            return developers_list_data
        else:
            if developers_list_data.status_code == requests.codes.not_found:
                return '{"detail":"Not found."}'
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
