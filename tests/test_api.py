import pytest

data_for_authorize = [{'name': 'Aladin'}, {'name': 'Patric'}, {'name': 'Alice'}]
positive_data = [{
            "info": {
                "colors": [
                    "green",
                    "black",
                    "white"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            },
            "tags": [
                "fun",
                "yoda"
            ],
            "text": "Only just begun the meme war has",
            "updated_by": "eugene",
            "url": "https://images.theconversation.com/files/177834/original/file-20170712-14488-19lw3sc.jpg?ixlib=rb"
                   "-1.1.0&q=45&auto=format&w=926&fit=clip"
        }

]


@pytest.mark.parametrize('data', data_for_authorize)
def test_make_authorization(create_authorize_endpoint, data):
    create_authorize_endpoint.make_authorization(payload=data)
    create_authorize_endpoint.check_that_status_is_200()


# def test_get_all_memes(create_get_endpoint, getting_a_token):
#     create_get_endpoint.show_all_memes(headers=getting_a_token)
#     create_get_endpoint.check_that_status_is_200()


def test_get_one_meme(create_get_endpoint, getting_a_token):
    create_get_endpoint.show_one_meme(headers=getting_a_token)
    create_get_endpoint.check_that_status_is_200()
    create_get_endpoint.check_that_tittle_is_correct("Only just begun the meme war has")
    print(getting_a_token)


def test_is_alife_a_token(check_token_life, getting_a_token):
    check_token_life.token_is_alive(headers=getting_a_token)
    print(getting_a_token)

#нужно посмотреть почему получаем 404 в ответе. Скорее всего что не подстовляется токен в запросе





