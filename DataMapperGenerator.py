""" EXAMPLE """

#@Input
"""
    @Attr1 int,
    @Attr2 bit,
    @Attr3 varchar(50),
    @Attr4 varchar(50),
"""
#@Output
"""
    Attr1 = sqloutput["Attr1"].toString(), 
    Attr2 = sqloutput["Attr2"].toString(),
    Attr3 = sqlobject["Attr3"].toString(),
    Attr4 = sqlobject["Attr4"].toString(),
"""

