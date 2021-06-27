import time
import uuid
import random

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def sleep_random_seconds() -> int:
    secs = random.randint(1, 5)
    time.sleep(secs)
    print("sleep_random_seconds: ", secs)
    return secs


def gen_unique_request_id():
    request_id = str(uuid.uuid4())
    # print("request_id: ", request_id)
    return request_id


def gen_random_folder_name(prefix: str) -> str:
    return prefix + "-" + str(int(time.time() * 1000))[-3:]
