def test_get_all_memes(create_get_endpoint):
    create_get_endpoint.show_all_memes()
    create_get_endpoint.response()
