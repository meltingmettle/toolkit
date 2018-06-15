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

x = "@OID varchar(32),     @EquipmentID varchar(50),     @City varchar(50),   @FirstName varchar(100),     @LastName varchar(100),     @POName varchar(200),     @Timezone varchar(10),      @HomePhoneNumber varchar(20),     @CellPhoneNumber varchar(20),     @WorkPhoneNumber varchar(20),     @InputGroup varchar(100),     @Reason varchar(128),      @Comment varchar(1024),      @StartDate datetime,     @TerminationDate datetime, @StreetAddress varchar(50),     @State varchar(50),     @ZIP varchar(50), @EmergencyContactName varchar(200),     @EmergencyStreetAddress varchar(128),      @EmergencyCity varchar(50),      @EmergencyState varchar(50),      @EmergencyZip varchar(50),     @EmergencyPhone1 varchar(15),     @EmergencyPhone2 varchar(15)"

def DataMapperGeneration(add_attribute_stored_procedure_parameters):
    data = add_attribute_stored_procedure_parameters
    attributelist = data.replace("'", "").replace(",", "").split("@")
    for x in range(len(attributelist)):
        attributelist[x] = attributelist[x].strip()
        attributelist[x] = attributelist[x].split(" ")
        if "varchar" in attributelist[x][1]:
            attributelist[x][1] = "varchar"
    return attributelist

DataMapperGeneration(x)
