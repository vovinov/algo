def valid_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    def make_dict(data):
        result = {}
        for i in range(len(data)):
            if data[i] in result:
                result[data[i]] += 1
            else:
                result[data[i]] = 1
        return result

    return make_dict(str1) == make_dict(str2)
