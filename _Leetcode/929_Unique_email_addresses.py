def umUniqueEmails(emails):
    res = []
    for email in emails:
        email = email.split("@")
        email[0] = email[0].replace(".", "").split("+")[0]
        res.append("@".join(email))

    return len(set(res))


print(
    umUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
)  # 2
print(umUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))  # 3
