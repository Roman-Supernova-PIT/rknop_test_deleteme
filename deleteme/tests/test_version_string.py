def test_version_is_string():
    from deleteme import __version__
    assert isinstance(__version__, str)
