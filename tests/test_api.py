import pytest

data_for_authorize = [{'name': 'Aladin'}, {'name': 'Patric'}, {'name': 'Alice'}]
positive_data = [{
            "id": 1,
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



def test_get_all_memes(create_get_endpoint, getting_a_token):
    create_get_endpoint.show_all_memes(headers=getting_a_token)


def test_get_one_meme(create_get_endpoint, getting_a_token):
    create_get_endpoint.show_one_meme(headers=getting_a_token)

