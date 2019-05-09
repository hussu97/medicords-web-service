import boto3
from boto3.dynamodb.conditions import Key, Attr
from flask import Flask,request
#
# dynamodb= boto3.resource('dynamodb', aws_access_key_id='AKIASUJUOQ5F6574EBND',aws_secret_access_key='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',region_name='eu-west-2')
# table = dynamodb.Table('Patients')
# table2=dynamodb.Table('Insurance')
# table3=dynamodb.Table('Hospitals')
# def get_items():
#     response = table.scan()
#     items = response['Items']
#     return items
#
# def get_item(name):
#     response = table.get_item(Key={'id':name})
#     #print(response)
#     item = response['Item']
#     return item
# def get_insurances():
#     response = table2.scan()
#     items = response['Items']
#     return items
#
# def get_insurance(name):
#     response = table2.get_item(Key={'id':name})
#     print(response)
#     item = response['Item']
#     return item
#
# def add_item(some_json): #additem
#     table.put_item(  Item=some_json)
#
# def add_insurance(some_json): #additem
#     table2.put_item(  Item=some_json)
#
# def verify_patient(name,isVerified):
#     table.update_item(Key={'id': name},UpdateExpression='SET isVerified = :val1',ExpressionAttributeValues={':val1': isVerified})
#
# def verify_insurance(name,isVerified):
#     table2.update_item(Key={'id': name},UpdateExpression='SET isVerified = :val1',ExpressionAttributeValues={':val1': isVerified})
#
# def get_by_country(country):
#     response = table.scan(
#     FilterExpression=Attr('country').eq(country))
#     items = response['Items']
#     return items
#
# def get_insurance_country(country):
#     response = table2.scan(
#     FilterExpression=Attr('country').eq(country))
#     items = response['Items']
#     return items
#
# def removeHospital(name):
#     table.update_item(
#                     Key={'id': name},
#                     UpdateExpression='REMOVE hospitalId')
#
# def addHospital(name,hospitalID):
#         table.update_item(
#                         Key={'id': name},
#                         UpdateExpression='SET hospitalId = :val1',
#                         ExpressionAttributeValues={':val1': hospitalID})
# def removeInsurance(name):
#     table.update_item(
#                     Key={'id': name},
#                     UpdateExpression='REMOVE insuranceId = :val1')
#
#
# def addInsurance(name,insuranceID):
#         table.update_item(
#                         Key={'id': name},
#                         UpdateExpression='SET insuranceId = :val1',
#                         ExpressionAttributeValues={':val1': insuranceID})
#
# def update_item(name,username,expiry,country,city,address,firstName,lastName,isVerified,identificationNumber):
#     table.update_item(
#                     Key={
#                         'id': name
#                     },
#                     UpdateExpression='SET username = :val1, expiry = :val2,country = :val3,city = :val4,address = :val5,firstName = :val6,lastName = :val7,isVerified = :val8,identificationNumber = :val9',
#                     ExpressionAttributeValues={
#                         ':val1': username,
#                         ':val2': expiry,
#                         ':val3': country,
#                         ':val4': city,
#                         ':val5': address,
#                         ':val6': firstName,
#                         ':val7': lastName,
#                         ':val8': isVerified,
#                         ':val9': identificationNumber
#                     }
#                 )
# def update_table(name,billid,status):
#     s="SET #inv["+str(billid)+"].#loc = :locVal"
#     table.update_item(Key={'id': name},UpdateExpression=s,ExpressionAttributeNames={'#inv': 'bills','#loc': 'status'},ExpressionAttributeValues={':locVal': status})
dynamodbtwo= boto3.resource('dynamodb', aws_access_key_id='XXX',aws_secret_access_key='XXX',region_name='XXX')
table = dynamodbtwo.Table('Patients')
def add_bill(name,billId,date,doctor,cost,VAT,total,status):
    table.update_item(
        Key={
            'id': name
        },
        UpdateExpression='SET bills = list_append(bills, :student_obj)',
        ExpressionAttributeValues={
            ":student_obj": [
                # {'myObject':
                    {
                        'billId': billId,
                        'date': date,
                        'doctor':doctor,
                        'cost': cost,
                        'VAT': VAT,
                        'total': total,
                        'status': status
                    }
                #}
            ]
        }
    )
# def add_allergy(name,allergyName,doctor,date,severity,medication):
#     table.update_item(
#         Key={
#             'id': name
#         },
#         UpdateExpression='SET allergies = list_append(allergies, :student_obj)',
#         ExpressionAttributeValues={
#             ":student_obj": [
#                 # {'myObject':
#                     {
#                         'name':allergyName,
#                         'doctor': doctor,
#                         'date':date,
#                         'severity': severity,
#                         'medication': medication
#                     }
#                 #}
#             ]
#         }
#     )
# def add_disease(name,date,diseasename,doctor,symptomes,medication):
#     table.update_item(
#         Key={
#             'id': name
#         },
#         UpdateExpression='SET diseases = list_append(diseases, :student_obj)',
#         ExpressionAttributeValues={
#             ":student_obj": [
#                 # {'myObject':
#                     {
#                         'date': date,
#                         'name': diseasename,
#                         'doctor':doctor,
#                         'symptomes': symptomes,
#                         'medication':medication
#                     }
#                 #}
#             ]
#         }
#     )
# def add_operation(name,date,operationName,doctor,dischargeDate,daysInHospital,comment):
#     table.update_item(
#         Key={
#             'id': name
#         },
#         UpdateExpression='SET operations = list_append(operations, :student_obj)',
#         ExpressionAttributeValues={
#             ":student_obj": [
#                 # {'myObject':
#                     {
#                         'date': date,
#                         'name':operationName,
#                         'doctor':doctor,
#                         'dischargeDate': dischargeDate,
#                         'daysInHospital': daysInHospital,
#                         'comment': comment
#                     }
#                 #}
#             ]
#         }
#     )
#
# def addPatient(name,patientId):
#     table2.update_item(
#         Key={
#             'id': name
#         },
#         UpdateExpression='SET patientIds = list_append(patientIds, :student_obj)',
#         ExpressionAttributeValues={
#             ":student_obj":[ patientId]
#         }
#     )
# def removePatient(name,patientId): #do something about it
#     table2.update_item(
#         Key={
#             'id': name
#         },
#         UpdateExpression='DELETE patientIds :student_obj',
#         ExpressionAttributeValues={
#             ":student_obj":{patientId}
#         }
#     )
# def update_insurance(name,username,expiry,country,city,address,InsuranceName,identificationNumber):
#     table2.update_item(
#                     Key={
#                         'id': name
#                     },
#                     UpdateExpression='SET username = :val1, expiry = :val2,country = :val3,city = :val4,address = :val5,name = :val6,isVerified = :val8,identificationNumber = :val9',
#                     ExpressionAttributeValues={
#                         ':val1': username,
#                         ':val2': expiry,
#                         ':val3': country,
#                         ':val4': city,
#                         ':val5': address,
#                         ':val6': InsuranceName,
#                         ':val8': False,
#                         ':val9': identificationNumber
#                     }
#                 )
# #---------------------------------------------------------------------------------------
# #hospital
# def add_Hospital(some_json): #additem
#     table3.put_item(Item=some_json)
# def get_hospital(name):
#     response = table3.get_item(Key={'id':name})
#     #print(response)
#     item = response['Item']
#     return item
# def update_hospital(name,username,expiry,country,city,address,hospitalName,identificationNumber):
#     table3.update_item(
#                     Key={
#                         'id': name
#                     },
#                     UpdateExpression='SET username = :val1, expiry = :val2,country=:val3,city = :val4,address = :val5,hospitalName = :val6,isVerified = :val7,identificationNumber = :val8',
#                     ExpressionAttributeValues={
#                         ':val1': username,
#                         ':val2': expiry,
#                         ':val3': country,
#                         ':val4': city,
#                         ':val5': address,
#                         ':val6': hospitalName,
#                         ':val7': False,
#                         ':val8': identificationNumber
#                     }
#                 )
# def verify_hospital(name,isVerified):
#     table3.update_item(Key={'id': name},UpdateExpression='SET isVerified = :val1',ExpressionAttributeValues={':val1': isVerified})
#
# def hospital_by_country(country):
#     response = table3.scan(
#     FilterExpression=Attr('country').eq(country))
#     items = response['Items']
#     return items
# #--------------------------------------------------------
# #doctorz
# def get_Doctor(name):
#     response = table4.get_item(Key={'id':name})
#     #print(response)
#     item = response['Item']
#     return item
#
# def verify_Doctor(name,isVerified):
#     table4.update_item(Key={'id': name},UpdateExpression='SET isVerified = :val1',ExpressionAttributeValues={':val1': isVerified})
#
# def doctor_by_country(country):
#     response = table4.scan(
#     FilterExpression=Attr('country').eq(country))
#     items = response['Items']
#     return items
# def update_Doctor(name,username,expiry,country,city,address,firstName,lastName,hospitalId,isVerified,identificationNumber,speciality):
#     table4.update_item(
#                     Key={
#                         'id': name
#                     },
#                     UpdateExpression='SET username = :val1, expiry = :val2,country=:val3,city = :val4,address = :val5,firstName = :val6,lastName = :val7,hospitalId= :val8,isVerified = :val9,identificationNumber = :val10,speciality = :val11',
#                     ExpressionAttributeValues={
#                         ':val1': username,
#                         ':val2': expiry,
#                         ':val3': country,
#                         ':val4': city,
#                         ':val5': address,
#                         ':val6': firstName,
#                         ':val7': lastName,
#                         ':val8': hospitalId,
#                         ':val9': isVerified,
#                         ':val10': identificationNumber,
#                         ':val11':speciality
#                     }
#                 )
#----------------------------------------------TESTING



dynamodb= boto3.client('dynamodb', aws_access_key_id='AKIASUJUOQ5F6574EBND',aws_secret_access_key='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',region_name='eu-west-2')
#table = dynamodb.Table('Patients')
#table2=dynamodb.Table('Insurance')
#table3=dynamodb.Table('Hospitals')
def get_items():
    response = dynamodb.scan(TableName="Patients")
    items = response['Items']
    return items

def get_item(name):
    response = dynamodb.get_item(TableName="Patients",Key={'id':{'S':name}})
    #print(response)
    item = response['Item']
    return item

def get_insurances():
    response = dynamodb.scan(TableName="Insurance")
    items = response['Items']
    return items

def get_insurance(name):
    response = dynamodb.get_item(TableName="Insurance",Key={'id':{'S':name}})
    print(response)
    item = response['Item']
    return item

def add_item(some_json): #additem
    dynamodb.put_item(TableName="Patients",Item=some_json)

def add_insurance(some_json): #additem
    dynamodb.put_item(TableName="Insurance", Item=some_json)

def verify_patient(name,isVerified,keyValue):#good
    dynamodb.update_item(TableName="Patients",Key={'id': {'S':name}},UpdateExpression='SET isVerified = :val1',ExpressionAttributeValues={':val1': isVerified})
def verify_insurance(name,isVerified,keyValue):#good
    dynamodb.update_item(TableName="Insurance",Key={'id': {'S':name}},UpdateExpression='SET isVerified = :val1 , apikey = :val2',ExpressionAttributeValues={':val1': isVerified, ':val2': keyValue})
def verify_insurancenokey(name,isVerified):#good
    dynamodb.update_item(TableName="Insurance",Key={'id': {'S':name}},UpdateExpression='SET isVerified = :val1 ',ExpressionAttributeValues={':val1': isVerified})
    dynamodb.update_item(TableName="Insurance",
                    Key={'id': {'S':name}},
                    UpdateExpression='REMOVE apikey ')

def get_by_country(country):
    response = dynamodb.scan(TableName="Patients",
    FilterExpression='country = :id',
    ExpressionAttributeValues={':id': {'S':country}})
    items = response['Items']
    return items

def get_insurance_country(country):
    response = dynamodb.scan(TableName="Insurance",
    FilterExpression='country = :id',
    ExpressionAttributeValues={':id': {'S':country}})
    items = response['Items']
    return items

def removeHospital(name):
    dynamodb.update_item(TableName="Patients",
                    Key={'id': {'S':name}},
                    UpdateExpression='REMOVE hospitalId')

def addHospital(name,hospitalID):
        dynamodb.update_item(TableName="Patients",
                        Key={'id': {'S':name}},
                        UpdateExpression='SET hospitalId = :val1',
                        ExpressionAttributeValues={':val1': hospitalID})
def removeInsurance(name):
    dynamodb.update_item(TableName="Patients",
                    Key={'id': {'S':name}},
                    UpdateExpression='REMOVE insuranceId ')


def addInsurance(name,insuranceID):
        dynamodb.update_item(TableName="Patients",
                        Key={'id': {'S':name}},
                        UpdateExpression='SET insuranceId = :val1',
                        ExpressionAttributeValues={':val1': insuranceID})

def update_item(name,username,expiry,country,city,address,firstName,lastName,isVerified,identificationNumber):
    dynamodb.update_item(TableName="Patients",
                    Key={
                        'id': {'S':name}
                    },
                    UpdateExpression='SET username = :val1, expiry = :val2,country = :val3,city = :val4,address = :val5,firstName = :val6,lastName = :val7,isVerified = :val8,identificationNumber = :val9',
                    ExpressionAttributeValues={
                        ':val1': username,
                        ':val2': expiry,
                        ':val3': country,
                        ':val4': city,
                        ':val5': address,
                        ':val6': firstName,
                        ':val7': lastName,
                        ':val8': isVerified,
                        ':val9': identificationNumber
                    }
                )
def update_table(name,billid,status):
    s="SET #inv["+str(billid)+"].#loc = :locVal"
    dynamodb.update_item(TableName="Patients",Key={'id': {'S':name}},UpdateExpression=s,ExpressionAttributeNames={'#inv': 'bills','#loc': 'status'},ExpressionAttributeValues={':locVal': status})
# def add_bill(name,billId,date,doctor,cost,VAT,total,status):
#     dynamodb.update_item(TableName="Patients",
#         Key={
#             'id': {'S':name}
#         },
#         UpdateExpression='SET bills = list_append(bills, :student_obj)',
#         ExpressionAttributeValues={
#             ":student_obj": [
#                 # {'myObject':
#                     {
#                         'billId': billId,
#                         'date': date,
#                         'doctor':doctor,
#                         'cost': cost,
#                         'VAT': VAT,
#                         'total': total,
#                         'status': status
#                     }
#                 #}
#             ]
#         }
#     )
def add_allergy(name,allergyName,doctor,date,severity,medication):
    table.update_item(TableName="Patients",
        Key={
            'id': name
        },
        UpdateExpression='SET allergies = list_append(allergies, :student_obj)',
        ExpressionAttributeValues={
            ":student_obj": [
                # {'myObject':
                    {
                        'name':allergyName,
                        'doctor': doctor,
                        'date':date,
                        'severity': severity,
                        'medication': medication
                    }
                #}
            ]
        }
    )
def add_disease(name,date,diseasename,doctor,symptomes,medication):
    table.update_item(TableName="Patients",
        Key={
            'id': name
        },
        UpdateExpression='SET diseases = list_append(diseases, :student_obj)',
        ExpressionAttributeValues={
            ":student_obj": [
                # {'myObject':
                    {
                        'date': date,
                        'name': diseasename,
                        'doctor':doctor,
                        'symptomes': symptomes,
                        'medication':medication
                    }
                #}
            ]
        }
    )
def add_disablity(name,date,disablityName,doctor,sideEffects,medication):
    print(date)
    table.update_item(TableName="Patients",
        Key={
            'id': name
        },
        UpdateExpression='SET diseases = list_append(diseases, :student_obj)',
        ExpressionAttributeValues={
            ":student_obj": [
                # {'myObject':
                    {
                        'date': date,
                        'name': disablityName,
                        'doctor':doctor,
                        'sideEffects':sideEffects,
                        'medication':medication
                    }
                #}
            ]
        }
    )
def add_operation(name,date,operationName,doctor,dischargeDate,daysInHospital,comment):
    table.update_item(TableName="Patients",
        Key={
            'id': name
        },
        UpdateExpression='SET operations = list_append(operations, :student_obj)',
        ExpressionAttributeValues={
            ":student_obj": [
                # {'myObject':
                    {
                        'date': date,
                        'name':operationName,
                        'doctor':doctor,
                        'dischargeDate': dischargeDate,
                        'daysInHospital': daysInHospital,
                        'comment': comment
                    }
                #}
            ]
        }
    )

def addPatient(name,patientId):
    dynamodb.update_item(TableName="Insurance",
        Key={
            'id': {'S':name}
        },
        UpdateExpression='ADD patientIds :student_obj',
        ExpressionAttributeValues={
            ":student_obj":{"SS": [patientId]}
        }
    )
def removePatient(name,patientId): #do something about it
    dynamodb.update_item(TableName="Insurance",
        Key={
            'id': {'S':name}
        },
        UpdateExpression='DELETE patientIds :student_obj',
        ExpressionAttributeValues={
            ":student_obj":{"SS": [patientId]}
        }
    )
def update_insurance(ID,username,expiry,country,city,address,InsuranceName,identificationNumber):
    dynamodb.update_item(TableName="Insurance",
                    Key={
                        'id': {'S':ID}
                    },
                    UpdateExpression='SET username = :val1, expiry = :val2,country = :val3,city = :val4,address = :val5, Iname = :val6,isVerified = :val7,identificationNumber = :val8',
                    ExpressionAttributeValues={
                        ':val1': username,
                        ':val2': expiry,
                        ':val3': country,
                        ':val4': city,
                        ':val5': address,
                        ':val6': InsuranceName,
                        ':val7': {'BOOL': False},
                        ':val8': identificationNumber
                    }
                )
#---------------------------------------------------------------------------------------
#hospital
def add_Hospital(some_json): #additem #good
    dynamodb.put_item(TableName="Hospitals",Item=some_json)
def get_hospital(name):#good
    response = dynamodb.get_item(TableName="Hospitals",Key={'id':{'S':name}}) #good
    #print(response)
    item = response['Item']
    return item
def update_hospital(ID,username,expiry,country,city,address,hospitalName,identificationNumber): #good
    dynamodb.update_item(TableName="Hospitals",
                    Key={
                        'id': {'S':ID}
                    },
                    UpdateExpression='SET username = :val1, expiry = :val2,country = :val3,city = :val4,address = :val5, Hname = :val6,isVerified = :val7,identificationNumber = :val8',
                    ExpressionAttributeValues={
                        ':val1': username,
                        ':val2': expiry,
                        ':val3': country,
                        ':val4': city,
                        ':val5': address,
                        ':val6': hospitalName,
                        ':val7': {'BOOL': False},
                        ':val8': identificationNumber
                    }
                )

def verify_hospital(name,isVerified,keyValue):#good
    dynamodb.update_item(TableName="Hospitals",Key={'id': {'S':name}},UpdateExpression='SET isVerified = :val1 , apikey = :val2',ExpressionAttributeValues={':val1': isVerified, ':val2': keyValue})
def verify_hospitalnokey(name,isVerified):#good
    dynamodb.update_item(TableName="Hospitals",Key={'id': {'S':name}},UpdateExpression='SET isVerified = :val1',ExpressionAttributeValues={':val1': isVerified})
    dynamodb.update_item(TableName="Hospitals",
                    Key={'id': {'S':name}},
                    UpdateExpression='REMOVE apikey ')

def hospital_by_country(country):#good
    response = dynamodb.scan(TableName="Hospitals",
    FilterExpression='country = :id',
    ExpressionAttributeValues={':id': {'S':country}})
    items = response['Items']
    return items
#doctorz
def get_Doctor(name):#good
    response = dynamodb.get_item(TableName="Doctors",Key={'id':{'S':name}})
    #print(response)
    item = response['Item']
    return item

def verify_Doctor(name,isVerified,keyValue):#good
    dynamodb.update_item(TableName="Doctors",Key={'id': {'S':name}},UpdateExpression='SET isVerified = :val1 , apikey = :val2',ExpressionAttributeValues={':val1': isVerified, ':val2': keyValue})
def verify_Doctornokey(name,isVerified):#good
    dynamodb.update_item(TableName="Doctors",Key={'id': {'S':name}},UpdateExpression='SET isVerified = :val1',ExpressionAttributeValues={':val1': isVerified})
    dynamodb.update_item(TableName="Doctors",
                    Key={'id': {'S':name}},
                    UpdateExpression='REMOVE apikey')
def add_Doctor(some_json):#good
    dynamodb.put_item(TableName="Doctors",Item=some_json)
def doctor_by_country(country):#good
    response = dynamodb.scan(TableName="Doctors",
    FilterExpression='country = :id',
    ExpressionAttributeValues={':id': {'S':country}})
    items = response['Items']
    return items
def update_Doctor(name,username,expiry,country,city,address,firstName,lastName,hospitalId,isVerified,identificationNumber,speciality):#good
    dynamodb.update_item(TableName="Doctors",
                    Key={
                        'id': {'S':name}
                    },
                    UpdateExpression='SET username = :val1, expiry = :val2,country=:val3,city = :val4,address = :val5,firstName = :val6,lastName = :val7,hospitalId= :val8,isVerified = :val9,identificationNumber = :val10,speciality = :val11',
                    ExpressionAttributeValues={
                        ':val1': username,
                        ':val2': expiry,
                        ':val3': country,
                        ':val4': city,
                        ':val5': address,
                        ':val6': firstName,
                        ':val7': lastName,
                        ':val8': hospitalId,
                        ':val9': isVerified,
                        ':val10': identificationNumber,
                        ':val11':speciality
                    }
                )
def addDoctorToHospital(name,DoctorId):#good
    dynamodb.update_item(TableName="Hospitals",
        Key={
            'id': {'S':name}
        },
        UpdateExpression='ADD doctorIds :student_obj',
        ExpressionAttributeValues={
            ":student_obj":{"SS": [DoctorId]}
        }
    )
def removeDoctorToHospital(name,DoctorId): #good
    dynamodb.update_item(TableName="Hospitals",
        Key={
            'id': {'S':name}
        },
        UpdateExpression='DELETE doctorIds :student_obj',
        ExpressionAttributeValues={
            ":student_obj":{"SS": [DoctorId]}
        }
    )
#-----------------------------------------------
def addPatientToHospital(name,PatientId):#good
    dynamodb.update_item(TableName="Hospitals",
        Key={
            'id': {'S':name}
        },
        UpdateExpression='ADD patientIds :student_obj',
        ExpressionAttributeValues={
            ":student_obj":{"SS": [PatientId]}
        }
    )
def removePatientToHospital(name,patientId): #good
    dynamodb.update_item(TableName="Hospitals",
        Key={
            'id': {'S':name}
        },
        UpdateExpression='DELETE patientIds :student_obj',
        ExpressionAttributeValues={
            ":student_obj":{"SS": [patientId]}
        }
    )
def addPatientToDoctor(name,PatientId):#good
    dynamodb.update_item(TableName="Doctors",
        Key={
            'id': {'S':name}
        },
        UpdateExpression='ADD patientIds :student_obj',
        ExpressionAttributeValues={
            ":student_obj":{"SS": [PatientId]}
        }
    )
def hospitalawayDoctor(name):
    dynamodb.update_item(TableName="Doctors",
                    Key={'id': {'S':name}},
                    UpdateExpression='REMOVE hospitalId ')
def hospitalToDoctor(name,hospitalId):
    responose=dynamodb.update_item(TableName="Doctors",
                    Key={
                        'id': {'S':name}
                    },
                    UpdateExpression='SET hospitalId = :val1',ConditionExpression='attribute_not_exists(hospitalId)',
                    ExpressionAttributeValues={
                        ':val1': {"S":hospitalId},
                    }
                )
    return responose
def getAPI(id,table):
    response = dynamodb.get_item(TableName=table,Key={'id':{'S':id}})
    item = response['Item']
    return (item['key'])

def putAPI(some_json):
    dynamodb.put_item(TableName="APIS",Item=some_json)
#-------------------------------------------
def get_government(name):#good
    response = dynamodb.get_item(TableName="Governments",Key={'id':{'S':name}}) #good
    item = response['Item']
    return item
