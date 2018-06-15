

#Toolkit!
#Pass in a SQL "insert" stored procedure, and DMG will output DataMapper format in C#. 
#Copy and paste the params into Google Search bar or anything that will de-format, then throw it in as a parameter 
#and enjoy your instantaenously generated beautiful DataMapper code. 

#Designed to assist in extending software with tens or hundreds of instance attributes and object entities.

""" EXAMPLE """

#@Input
"""
    @Attr1 int,
    @Attr2 bit,
    @Attr3 varchar(50),
    @Attr4 varchar(50),
"""
"""
   #C&P into Google Search Bar to remove formatting.
   #Define and execute program in Jupyter Notebook or similar software.
   >>>input = "@Attr1 int,     @Attr2 bit,     @Attr3 varchar(50),     @Attr4 varchar(50),"
   >>>DataMapperGenerator(input)

"""
#@Output
"""
    Attr1 = sqloutput["Attr1"].toString(), 
    Attr2 = sqloutput["Attr2"].toString(),
    Attr3 = sqlobject["Attr3"].toString(),
    Attr4 = sqlobject["Attr4"].toString()
"""

def DataMapperGeneration(add_attribute_stored_procedure_parameters):
    data = add_attribute_stored_procedure_parameters.replace("'", "").replace(",", "").split("@")[1:]
    output = '{0} = reader["{0}"].toString(),'
    for x in range(len(data)):
        data[x] = output.format(data[x].strip().split(" ")[0])
        if len(data) - 1 == x:          #To print the last attribute without aforementioned pesky comma
            print(data[x][0:-1])
        else:
            print(data[x])  
