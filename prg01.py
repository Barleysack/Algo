participant = ["mislav","stanko",""].sort();


def solution(participant, completion):
    k = [x for x in participant if x not in completion]
    answer = k[0]

    return answer