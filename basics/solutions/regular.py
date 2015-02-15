pat = re.compile("([\w.-_]+)@([\w.-]+\.[a-z]+)")
email_list = pat.findall(emails)
print email_list[:3]
print "# of emails in the list is", len(email_list)
