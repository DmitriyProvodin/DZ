import pytest
from decorators import log

# тест успешного выполнения функции, лог в консоль
def test_log_success_console(capsys):
    # создаём простую функцию с декоратором log
    @log()
    def add(a, b):
        return a + b

    # вызываем функцию
    result = add(2, 3)

    # перехватываем консольный вывод
    captured = capsys.readouterr()

    # проверяем, что результат правильный
    assert result == 5

    # проверяем, что сообщение об успехе есть в консоли
    assert "add ok" in captured.out


# тест ошибки внутри функции, лог в консоль
def test_log_error_console(capsys):
    # создаём функцию, которая вызывает ошибку
    @log()
    def divide(a, b):
        return a / b

    # вызываем функцию с нулём и ловим исключение
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # перехватываем вывод в консоль
    captured = capsys.readouterr()

    # проверяем, что сообщение об ошибке присутствует
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0), {}" in captured.out


# тест логирования в файл при успешном выполнении
def test_log_success_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def say_hello():
        return "Hello"

    say_hello()

    content = log_file.read_text(encoding="utf-8")

    assert "say_hello ok" in content


# тест логирования ошибки в файл
def test_log_error_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def fail():
        raise ValueError("test error")

    with pytest.raises(ValueError):
        fail()

    content = log_file.read_text(encoding="utf-8")

    assert "fail error: ValueError" in content
    assert "Inputs: (), {}" in content
