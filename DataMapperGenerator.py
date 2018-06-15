

#Toolkit!
#Pass in a SQL "insert" stored procedure, and DMG will output DataMapper format in C#. 
#Copy and paste the params into Google Search bar or anything that will de-format, then throw it in as a parameter 
#and enjoy your instantaenously generated beautiful DataMapper code. 

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

def DataMapperGenerator(add_attribute_stored_procedure_parameters):
    data = add_attribute_stored_procedure_parameters.replace("'", "").replace(",", "").split("@")[1:]
    output = '{0} = reader["{0}"].toString(),'
    for x in range(len(data)):
        data[x] = output.format(data[x].strip().split(" ")[0])
        print(data[x])
    print(data[x][0:-1])  #To print the last attribute without aforementioned pesky comma

