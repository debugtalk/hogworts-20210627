# NOTE: Generated By HttpRunner v3.1.5
# FROM: har/mubu.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginMubu(HttpRunner):

    config = (
        Config("testcase description")
        .verify(False)
        .variables(
            **{
                "data_unique_id": "ff03457c-2d57-4234-aab4-ac640f13ed69",
                "csrf_token": "6b496110-0494-4893-9465-2940d370b514",
                "SESSION": "a3a50348-a6fd-487c-aab0-7de988897ad3",
                "phone": "18613143458",
                "password": "qtFrwy$!kt3RTRq@QstF",
            }
        )
        .export("jwt_token")
    )

    teststeps = [
        Step(
            RunRequest("/")
            .get("https://mubu.com/")
            .with_headers(
                **{
                    "cache-control": "max-age=0",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "$data_unique_id",
                    "csrf_token": "$csrf_token",
                    "SESSION": "$SESSION",
                    "language": "en-US",
                    "country": "US",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1624774035",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1624774035",
                    "SLARDAR_WEB_ID": "5d11ee80-1660-4067-8987-8250201733a8",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "_ga": "GA1.2.317427957.1624774036",
                    "_gid": "GA1.2.452646006.1624774036",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("//static/img/flow.gif")
            .get("https://mubu.com//static/img/flow.gif")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "no-cors",
                    "sec-fetch-dest": "image",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "$data_unique_id",
                    "csrf_token": "$csrf_token",
                    "SESSION": "$SESSION",
                    "language": "en-US",
                    "country": "US",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1624774035",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1624774035",
                    "SLARDAR_WEB_ID": "5d11ee80-1660-4067-8987-8250201733a8",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "_ga": "GA1.2.317427957.1624774036",
                    "_gid": "GA1.2.452646006.1624774036",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login")
            .get("https://mubu.com/login")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "$data_unique_id",
                    "csrf_token": "$csrf_token",
                    "SESSION": "$SESSION",
                    "language": "en-US",
                    "country": "US",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1624774035",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "_ga": "GA1.2.317427957.1624774036",
                    "_gid": "GA1.2.452646006.1624774036",
                    "_gat": "1",
                    "SLARDAR_WEB_ID": "428622dd-24fb-45b9-bdd0-23d7e4657f02",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1624774137",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
            .options("https://api2.mubu.com/v3/api/user/profile")
            .with_headers(
                **{
                    "accept": "*/*",
                    "access-control-request-method": "POST",
                    "access-control-request-headers": "data-unique-id,jwt-token,version,x-request-id",
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
            RunRequest("/v3/api/user/profile")
            .post("https://api2.mubu.com/v3/api/user/profile")
            .with_headers(
                **{
                    "content-length": "0",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "",
                    "x-request-id": "${gen_unique_request_id()}",
                    "version": "3.0.0-2.0.0.1717",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 2)
            .assert_equal("body.msg", "Login Expired")
        ),
        Step(
            RunRequest("/v3/api/user/phone_login")
            .options("https://api2.mubu.com/v3/api/user/phone_login")
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
            RunRequest("/v3/api/user/phone_login")
            .post("https://api2.mubu.com/v3/api/user/phone_login")
            .with_headers(
                **{
                    "content-length": "74",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "",
                    "x-request-id": "${gen_unique_request_id()}",
                    "version": "3.0.0-2.0.0.1717",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_json({"phone": "$phone", "password": "$password", "callbackType": 0,})
            .extract()
            .with_jmespath('cookies."Jwt-Token"', "jwt_token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/app")
            .get("https://mubu.com/app")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/login",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "$data_unique_id",
                    "csrf_token": "$csrf_token",
                    "SESSION": "$SESSION",
                    "language": "en-US",
                    "country": "US",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1624774035",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "_ga": "GA1.2.317427957.1624774036",
                    "_gid": "GA1.2.452646006.1624774036",
                    "_gat": "1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1624774145",
                    "SLARDAR_WEB_ID": "fe647568-13ec-48f8-9922-584a3d3d8385",
                    "_gat_UA-77727571-3": "1",
                    "Jwt-Token": "$jwt_token",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
            .post("https://api2.mubu.com/v3/api/user/profile")
            .with_headers(
                **{
                    "content-length": "0",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
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
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/activity/five_years/participation")
            .options("https://api2.mubu.com/v3/api/activity/five_years/participation")
            .with_headers(
                **{
                    "accept": "*/*",
                    "access-control-request-method": "POST",
                    "access-control-request-headers": "data-unique-id,jwt-token,version,x-request-id",
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
            RunRequest("/v3/api/list/star_relation/get")
            .options("https://api2.mubu.com/v3/api/list/star_relation/get")
            .with_headers(
                **{
                    "accept": "*/*",
                    "access-control-request-method": "GET",
                    "access-control-request-headers": "data-unique-id,jwt-token,version,x-request-id",
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
            RunRequest("/v3/api/list/get_all_documents_page")
            .options("https://api2.mubu.com/v3/api/list/get_all_documents_page")
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
            RunRequest("/v3/api/user/get_user_params")
            .options("https://api2.mubu.com/v3/api/user/get_user_params")
            .with_headers(
                **{
                    "accept": "*/*",
                    "access-control-request-method": "POST",
                    "access-control-request-headers": "data-unique-id,jwt-token,version,x-request-id",
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
            RunRequest("/v3/api/activity/five_years/participation")
            .post("https://api2.mubu.com/v3/api/activity/five_years/participation")
            .with_headers(
                **{
                    "content-length": "0",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
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
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 4011)
            .assert_equal("body.msg", "unknown error")
        ),
        Step(
            RunRequest("/v3/api/list/star_relation/get")
            .get("https://api2.mubu.com/v3/api/list/star_relation/get")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
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
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/get_all_documents_page")
            .post("https://api2.mubu.com/v3/api/list/get_all_documents_page")
            .with_headers(
                **{
                    "content-length": "12",
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
            .with_json({"start": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
            .post("https://api2.mubu.com/v3/api/user/get_user_params")
            .with_headers(
                **{
                    "content-length": "0",
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
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
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_onboard_state")
            .options("https://api2.mubu.com/v3/api/user/get_onboard_state")
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
            RunRequest("/v3/photo/f46a9b70-5b7f-4942-88f1-5437314377a7.jpg")
            .get(
                "https://api2.mubu.com/v3/photo/f46a9b70-5b7f-4942-88f1-5437314377a7.jpg"
            )
            .with_headers(
                **{
                    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "no-cors",
                    "sec-fetch-dest": "image",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1624774035",
                    "_ga": "GA1.2.317427957.1624774036",
                    "_gid": "GA1.2.452646006.1624774036",
                    "_gat": "1",
                    "_gat_UA-77727571-3": "1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1624774152",
                    "SLARDAR_WEB_ID": "27d2b71d-b9a0-42a7-af5d-77884aacc193",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/message/get_message_unread")
            .options("https://api2.mubu.com/v3/api/message/get_message_unread")
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
            RunRequest("/v3/api/user/get_onboard_state")
            .post("https://api2.mubu.com/v3/api/user/get_onboard_state")
            .with_headers(
                **{
                    "content-length": "2",
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
            .with_json({})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/message/get_message_unread")
            .post("https://api2.mubu.com/v3/api/message/get_message_unread")
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
            .with_json({"page": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
            .options("https://api2.mubu.com/v3/api/advertisement/get")
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
            RunRequest("/v3/api/list/item_count")
            .options("https://api2.mubu.com/v3/api/list/item_count")
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
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "content-length": "30",
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
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
            .post("https://api2.mubu.com/v3/api/advertisement/get")
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
            RunRequest("/v3/api/notify/new_tip/get")
            .options("https://api2.mubu.com/v3/api/notify/new_tip/get")
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
    ]


if __name__ == "__main__":
    TestCaseLoginMubu().test_start()
