import sys
from enum import Enum

from dataclasses import dataclass
from pymonad import Either, Right, Left

long_description = {400: "Error: Number is negative",
                    430: "Error: Not found two number"}


class ErrorFindTwo(Enum):
    ERROR_NEGATIVE = 400
    ERROR_NOT_TWO = 430


def find_number_two(num) -> Either:
    if num < 0:
        return Left(ErrorFindTwo.ERROR_NEGATIVE)

    if num == 2:
        return Right(num)
    else:
        return Left(ErrorFindTwo.ERROR_NOT_TWO)


@dataclass
class Response:
    code: int
    message: str


def is_success(result):
    return isinstance(result, Right)


def select_your_response(result):
    if is_success(result):
        return Response(code=200, message="Yeah! We found it")
    else:
        code = result.value.value
        return Response(code=result.value.value, message=long_description[code])


def do_something_with_valid_value(result):
    result.fmap(lambda x: print('Jibiri {}'.format(x)))


if __name__ == '__main__':
    number = int(sys.argv[1])
    print("Number:", number)

    result = find_number_two(number)
    # print(result)
    # print('----------------------------------')

    response = select_your_response(result)
    print(response)
    print('-----------------')

    #
    # do_something_with_valid_value(result)
