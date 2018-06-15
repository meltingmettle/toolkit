#Toolkit!
#Take in a block of SQL stored procedure parameter declaration and return a neatly formatted JSON conversion code block in C#.

@Input
"""
        @RetrievalID int,
        @PrimaryAddress bit,
        @StreetAddress varchar(50),
        @City varchar(50),
        @State varchar(50),
        @ZIP varchar(50)
        
"""

@Output
"""
        StringBuilder builder = new StringBuilder();
        builder.Append("\"RetrievalID\":\"" + RetrievalID + "\",");
        builder.Append("\"PrimaryAddress\":\"" + PrimaryAddress + "\",");
        builder.Append("\"StreetAddress\":\"" + StreetAddress + "\",");
        builder.Append("\"City\":\"" + City + "\",");
        builder.Append("\"State\":\"" + State + "\",");
        builder.Append("\"ZIP\":\"" + ZIP + "\",");
        builder.Append("}");
        return builder.ToString();
        
"""
    
def ToJSONGenerator(add_attribute_stored_procedure_parameters):
    data = add_attribute_stored_procedure_parameters.replace("'", "").replace(",", "").split("@")[1:]
    output = 'builder.Append("\\"{0}\\":\\"" + {0} + "\\",");'
    print("StringBuilder builder = new StringBuilder();")
    for i in range(len(data)):
        data[i] = output.format(data[i].strip().split(" ")[0])
        print(data[i])
    print('builder.Append("}");')
    print('return builder.ToString();')
 
