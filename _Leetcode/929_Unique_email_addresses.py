"""
Every valid email consists of a local name and a domain name,
separated by the '@' sign. Besides lowercase letters,
the email may contain one or more '.' or '+'.

Given an array of strings emails where we send one email to each emails[i],
return the number of different addresses that actually receive mails.
"""


def umUniqueEmails(emails):
    pass


print(
    umUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
)
print(umUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
