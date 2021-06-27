# NOTE: Generated By HttpRunner v3.1.5
# FROM: har/mubu.har

import pytest
from httprunner import Parameters
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.login_test import TestCaseLoginMubu as CaseLoginMubu


class TestCaseMubuCreateFolder(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "prefix": ["hogwarts1", "hogwarts2"],
                "data_unique_id": "${gen_unique_request_id_list()}",
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("testcase description")
        .verify(False)
        .variables(**{"data_unique_id": "ff03457c-2d57-4234-aab4-ac640f13ed69",})
        .export("folderID")
    )

    teststeps = [
        Step(
            RunTestCase("login mubu")
            .with_variables(
                **{"phone": "18613143458", "password": "qtFrwy$!kt3RTRq@QstF"}
            )
            .call(CaseLoginMubu)
            .export("jwt_token")
        ),
        Step(
            RunRequest("/v3/api/list/create_folder")
            .options("https://api2.mubu.com/v3/api/list/create_folder")
            .with_headers(
                **{
                    "accept": "*/*",
                    "access-control-request-method": "POST",
                    "access-control-request-headers": "content-type,data-unique-id,jwt-token,version,x-request-id",
                    "origin": "https://mubu.com",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/list/create_folder")
            .post("https://api2.mubu.com/v3/api/list/create_folder")
            .with_headers(
                **{
                    "content-length": "39",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "$jwt_token",
                    "x-request-id": "${gen_unique_request_id()}",
                    "version": "3.0.0-2.0.0.1716",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_json({"name": "${gen_random_folder_name($prefix)}", "folderId": "0"})
            .teardown_hook("${sleep_random_seconds()}", "sleep_secs")
            .extract()
            .with_jmespath("body.data.folder.id", "folderID")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/notify/new_tip/get")
            .post("https://api2.mubu.com/v3/api/notify/new_tip/get")
            .with_headers(
                **{
                    "content-length": "10",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "$jwt_token",
                    "x-request-id": "${gen_unique_request_id()}",
                    "version": "3.0.0-2.0.0.1716",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "content-length": "42",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "$jwt_token",
                    "x-request-id": "${gen_unique_request_id()}",
                    "version": "3.0.0-2.0.0.1716",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_json({"folderId": "$folderID", "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuCreateFolder().test_start()
