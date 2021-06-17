import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

def txfanyi(input,st1,st2):
    try:
        cred = credential.Credential(st1, st2)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

        req = models.TextTranslateBatchRequest()
        params = {
            "Source": "auto",
            "Target": "zh",
            "ProjectId": 0,
            "SourceTextList": [input]
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextTranslateBatch(req)
        output=json.loads(resp.to_json_string())["TargetTextList"][0]
        return output

    except TencentCloudSDKException as err:
        print(err)
