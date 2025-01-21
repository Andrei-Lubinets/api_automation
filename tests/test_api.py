import pytest
import allure

positive_data_for_authorize = [{'name': 'Aladin'}, {'name': 'Patric'}, {'name': 'Alice'}]
negative_data_for_authorize = [{'name': 000}, {'name': {123: 'str'}}, {'name': ['robin', 'jack']}]
positive_data_for_create_memes = [{"info": {"colors": ["brown", "grey", "yellow"], "objects": ["picture", "text"]},
                                   "tags": ["fun", "little girl", "fire", "spider"],
                                   "text": "There was a spider. It`s gone now.",
                                   "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                                          ":ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s"},
                                  {"info": {"colors": ["green", "black"], "objects": ["picture", "text"]},
                                   "tags": ["fun", "Frog", "Pepe", "Cry"],
                                   "text": "When friends don`t now Pepe",
                                   "url": "https://i.imgflip.com/1yytwo.jpg"}
                                  ]

data_for_change_meme = {"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                        "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                        "text": "When people ask me. Whats your favorite meme?",
                        "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo-DiCaprio"
                               "-Django-Unchained-drinking-meme.jpg"}

negative_data_for_change_meme = [{"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                                  "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                                  "text": ['When people ask me. Whats your favorite meme?'],
                                  "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo"
                                         "-DiCaprio-Django-Unchained-drinking-meme.jpg"},
                                 {"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                                  "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                                  "text": 'When people ask me. Whats your favorite meme?',
                                  "url": 1243124
                                  },
                                 {"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                                  "tags": {"fun", "Leonardo DiCaprio", "Django Unchained"},
                                  "text": 'When people ask me. Whats your favorite meme?',
                                  "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo"
                                         "-DiCaprio-Django-Unchained-drinking-meme.jpg"
                                  },
                                 {"info": [{"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]}],
                                  "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                                  "text": 'When people ask me. Whats your favorite meme?',
                                  "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo"
                                         "-DiCaprio-Django-Unchained-drinking-meme.jpg"
                                  }
                                 ]


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Authorize on the platform')
@pytest.mark.parametrize('data', positive_data_for_authorize)
def test_make_authorization(create_authorize_endpoint, data):
    create_authorize_endpoint.make_authorization(payload=data)
    create_authorize_endpoint.check_that_status_is_200()


@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Checking authorization with invalid values')
@pytest.mark.parametrize('negative_data', negative_data_for_authorize)
def test_negative_authorization(create_authorize_endpoint, negative_data):
    create_authorize_endpoint.make_authorization(payload=negative_data)
    create_authorize_endpoint.check_bad_request()


@allure.feature('Meme')
@allure.story('Manipulate with meme')
@pytest.mark.smoke
@allure.title('Getting all the memes')
def test_get_all_memes(create_get_endpoint, getting_a_headers):
    create_get_endpoint.show_all_memes(headers=getting_a_headers)
    create_get_endpoint.check_that_status_is_200()


@allure.feature('Meme')
@allure.story('Manipulate with meme')
@pytest.mark.smoke
@allure.title('Getting one meme')
def test_get_one_meme(create_get_endpoint, getting_a_headers):
    create_get_endpoint.show_one_meme(headers=getting_a_headers)
    create_get_endpoint.check_that_status_is_200()
    create_get_endpoint.check_that_text_is_correct("Only just begun the meme war has")


@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Getting one meme by unauthorized user')
def test_get_one_meme_by_unauthorized_user(create_get_endpoint):
    create_get_endpoint.show_one_meme()
    create_get_endpoint.check_no_authorize_request()


@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Getting all memes by unauthorized user')
def test_get_all_memes_by_unauthorized_user(create_get_endpoint):
    create_get_endpoint.show_all_memes()
    create_get_endpoint.check_no_authorize_request()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Checking token validity')
def test_is_alife_a_token(check_authorize_endpoint, getting_a_token):
    check_authorize_endpoint.token_is_alive(token=getting_a_token)
    check_authorize_endpoint.check_that_status_is_200()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.step('Create new meme')
@pytest.mark.parametrize("data", positive_data_for_create_memes)
def test_create_new_meme(create_post_endpoint, getting_a_headers, data):
    create_post_endpoint.add_new_meme(payload=data, headers=getting_a_headers)
    create_post_endpoint.check_that_status_is_200()


@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Create new meme with negative data')
@pytest.mark.parametrize("negative_data", negative_data_for_change_meme)
def test_create_new_meme_with_negative_data(create_post_endpoint, getting_a_headers, negative_data):
    create_post_endpoint.add_new_meme(payload=negative_data, headers=getting_a_headers)
    create_post_endpoint.check_bad_request()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Partial modification of data in the meme')
def test_change_meme_data(create_put_endpoint, getting_a_headers, getting_meme_id):
    data_for_change_meme["id"] = getting_meme_id
    create_put_endpoint.change_meme(meme_id=getting_meme_id,
                                    payload=data_for_change_meme,
                                    headers=getting_a_headers
                                    )
    create_put_endpoint.check_that_status_is_200()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Delete meme')
def test_delete_meme(create_delete_endpoint, getting_meme_id, getting_a_headers):
    create_delete_endpoint.delete_meme(meme_id=getting_meme_id, headers=getting_a_headers)
    create_delete_endpoint.check_that_status_is_200()
