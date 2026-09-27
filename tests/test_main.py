from agent_test import main


def test_main_prints_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from agent-test!\n"
