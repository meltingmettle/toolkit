
#Toolkit!
#Pass in the "insert" stored procedure, and DMG will output entity object implenetation. 
#(SQL to C#)

#Designed to assist in extending software with tens or hundreds of instance attributes and object entities.

""" EXAMPLE """

@Input
"""
    @Attr1 int,
    @Attr2 bit,
    @Attr3 varchar(50),
    @Attr4 varchar(50),
"""

"""
   #C&P into Google Search Bar to remove formatting.
   #Define and execute program into Jupyter Notebook or similar software.
   >>>input = "@Attr1 int,     @Attr2 bit,     @Attr3 varchar(50),     @Attr4 varchar(50),"
   >>>EntityGenerator(input)

"""
@Output
"""
    public int Attr1 { get; set; }
    public int Attr2 { get; set; }
    public String Attr3 { get; set; }
    public String Attr4 { get; set; }
"""

#==================================IMPORTANT======================================
#ATTRIBUTES WITH TYPES UNSUPPORTED IN C# OR OTHERWISE WITH SPECIAL NAMES WILL NEED TO BE ADDED OR CHECKED MANUALLY!

#Varchar is default converted to "String".
#Bit is default converted to "int"


def EntityGenerator(add_attribute_stored_procedure_parameters):
    data = add_attribute_stored_procedure_parameters.replace("'", "").replace(",", "").split("@")[1:]
    def UnsupportedTypeRemoval(x):		#Helper function to manage data types which are unsupported in C#.  Not all-inclusive. 
        if "varchar" in x:
            return "String"
        elif "bit" in x:
            return "String"
        elif "datetime" in x:
            return "String"
        else:
            return x
        
    for x in range(len(data)):
		item = data[x].strip().split(" ")
        data[x] = "public " + UnsupportedTypeRemoval(item[1]) + " " + item[0] + "{get; set;}" 
        print(data[x])


#Enjoy!
