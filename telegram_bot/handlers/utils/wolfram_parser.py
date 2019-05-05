from typing import List

from wolfram.api import WolframResult


def parse_wolfram_answer(
        answer: WolframResult,
        simple_mode: bool = False
) -> List[str]:
    if answer.error or not answer.success:
        return ['Unsuccessful. Check your request and try again']
    simple_mode_pods_number = 3
    answer_pods = answer.pods[:simple_mode_pods_number] if simple_mode \
        else answer.pods
    parsed_answer = []
    for pod in answer_pods:
        parsed_answer.append(pod.title)
        for sub in pod.subpods:
            text = sub.plaintext
            image_src = '[Image]({})'.format(sub.img.src)
            if image_src:
                parsed_answer.append(image_src)
            elif text:
                parsed_answer.append(text)
    return parsed_answer
