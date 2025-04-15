from typing import Callable, Any, Optional, TypeVar, cast
from functools import wraps

# создаём универсальный тип для обёрнутой функции
F = TypeVar("F", bound=Callable[..., Any])

# функция log — декоратор, принимает имя файла или None
def log(filename: Optional[str] = None) -> Callable[[F], F]:

    # возвращает настоящий декоратор
    def decorator(func: F) -> F:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # пробуем вызвать оригинальную функцию
                result = func(*args, **kwargs)

                # логируем успешное выполнение
                message = f"{func.__name__} ok\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)

                return result

            except Exception as e:
                # логируем ошибку
                error_type = type(e).__name__
                message = (
                    f"{func.__name__} error: {error_type}. "
                    f"Inputs: {args}, {kwargs}\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)

                raise

        # возвращаем обёртку с приведённым типом
        return cast(F, wrapper)

    return decorator
