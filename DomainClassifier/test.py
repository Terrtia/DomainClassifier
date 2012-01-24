import domainclassifier

c = domainclassifier.Extract( rawtext = "this is a text with a domain called test@foo.lu another test abc.lu something a.b.c.d.e end of 1.2.3.4 foo.be www.belnet.be http://www.cert.be/ www.public.lu www.allo.lu quuxtest www.eurodns.com something-broken-www.google.com www.google.lu trailing test")

print c.domain()
print c.validdomain(extended=True)
print "US:"
print c.localizedomain(cc='US')
print "LU:"
print c.localizedomain(cc='LU')
print "BE:"
print c.localizedomain(cc='BE')
