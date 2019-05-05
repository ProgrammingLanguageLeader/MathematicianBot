from typing import List, Optional

from wolfram.api import WolframResult


def parse_wolfram_answer(answer: Optional[WolframResult]) -> List[str]:
    if not answer or answer.error or not answer.success:
        return ['Unsuccessful. Check your request and try again']
    parsed_answer = []
    for pod in answer.pods:
        parsed_answer.append(pod.title)
        for sub in pod.subpods:
            text = sub.plaintext
            image_src = '[Image]({})'.format(sub.img.src)
            if image_src:
                parsed_answer.append(image_src)
            elif text:
                parsed_answer.append(text)
    return parsed_answer
