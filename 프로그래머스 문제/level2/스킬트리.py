def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        if len(skill) > len(skill_tree):
            continue
        a = ''
        for s in skill_tree:
            if s in skill:
                a += s
        if skill[:len(a)] == a:
            answer += 1
    return answer