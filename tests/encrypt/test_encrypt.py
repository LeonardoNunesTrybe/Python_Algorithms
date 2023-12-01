from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("hello", 1) == "h_olle"
    assert encrypt_message("hello", 2) == "oll_eh"
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("hello", 4) == "o_lleh"
    assert encrypt_message("hello", 0) == "olleh"

    with pytest.raises(TypeError):
        encrypt_message("hello", -1) == "hello"
        encrypt_message("hello", "5") == "hello"
        encrypt_message(5, "hello") == "hello"
