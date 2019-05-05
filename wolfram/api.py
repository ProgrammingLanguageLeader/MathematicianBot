from collections import OrderedDict
from typing import Optional

import requests
import xmltodict


class WolframResult(OrderedDict):
    def __init__(self, parsed_answer: OrderedDict):
        parsed_answer = parsed_answer['queryresult']
        super().__init__(parsed_answer)
        self.success = True if parsed_answer['@success'] == 'true' else False
        self.error = True if parsed_answer['@error'] == 'true' else False
        if self.success and not self.error:
            self.numpods = int(parsed_answer['@numpods'])
            pods = parsed_answer['pod']
            if self.numpods == 1:
                self.pods = [WolframPod(pods)]
            else:
                self.pods = [WolframPod(pod) for pod in pods]


class WolframPod(OrderedDict):
    def __init__(self, parsed_pod: OrderedDict):
        super().__init__(parsed_pod)
        self.title = parsed_pod['@title']
        self.numsubpods = int(parsed_pod['@numsubpods'])
        subpods = parsed_pod['subpod']
        if self.numsubpods == 1:
            self.subpods = [WolframSubpod(subpods)]
        else:
            self.subpods = [WolframSubpod(sub) for sub in subpods]


class WolframSubpod(OrderedDict):
    def __init__(self, parsed_subpod: OrderedDict):
        super().__init__(parsed_subpod)
        self.img = WolframImage(parsed_subpod['img'])
        self.plaintext = parsed_subpod['plaintext']


class WolframImage(OrderedDict):
    def __init__(self, parsed_img: OrderedDict):
        super().__init__(parsed_img)
        self.src = parsed_img['@src']


def make_wolfram_request(
        request: str,
        app_id: str,
        timeout: float = 5
) -> Optional[WolframResult]:
    params = {
        'input': request,
        'appid': app_id
    }
    try:
        answer = requests.get(
            url='https://api.wolframalpha.com/v2/query',
            params=params,
            timeout=timeout
        )
        return WolframResult(xmltodict.parse(answer.content))
    except requests.exceptions.Timeout:
        return


def make_simple_wolfram_request(
        request: str,
        app_id: str,
        timeout: float = 5
) -> Optional[bytes]:
    params = {
        'input': request,
        'appid': app_id
    }
    try:
        answer = requests.get(
            url='https://api.wolframalpha.com/v2/simple',
            params=params,
            timeout=timeout
        )
        return answer.content
    except requests.exceptions.Timeout:
        return
