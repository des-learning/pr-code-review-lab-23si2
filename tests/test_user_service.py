from user_service import register_user

def test_register():
    user = register_user("testuser", "test123")

    assert user is not None
    assert user["username"] == "testuser"