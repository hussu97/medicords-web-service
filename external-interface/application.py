from flask import Flask,request,jsonify,abort
from flask_restful import Resource, Api
import aws_controller
from flask_restful import reqparse
from functools import wraps

application=app=Flask(__name__)
api=Api(app)
def doctorkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        #if request.args.get('key') and request.args.get('key') == key:
        #print(aws_controller.getAPI(request.headers.get('email')))
        if request.headers.get('id'):
            if request.headers.get('apikey') and aws_controller.getAPI(request.headers.get('id'),table="Doctors") == {'S':request.headers.get('apikey')}:
                return view_function(*args, **kwargs)
            else:
                abort(401)
        else:
            abort(401)
    return decorated_function

def hospitalkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        #if request.args.get('key') and request.args.get('key') == key:
        #print(aws_controller.getAPI(request.headers.get('email')))
        if request.headers.get('id'):
            if request.headers.get('apikey') and aws_controller.getAPI(request.headers.get('id'),table="Hospitals") == {'S':request.headers.get('apikey')}:
                return view_function(*args, **kwargs)
            else:
                abort(401)
        else:
            abort(401)
    return decorated_function

def insurancekey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        #if request.args.get('key') and request.args.get('key') == key:
        #print(aws_controller.getAPI(request.headers.get('email')))
        if request.headers.get('id'):
            if request.headers.get('apikey') and aws_controller.getAPI(request.headers.get('id'),table="Insurance") == {'S':request.headers.get('apikey')}:
                return view_function(*args, **kwargs)
            else:
                abort(401)
        else:
            abort(401)
    return decorated_function

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World!'}
    def post(self):
        some_json = request.get_json()
        aws_controller.add_item(some_json)

class Multi(Resource):
    def get(self):
        return aws_controller.get_items()
    def post(self):
        some_json = request.get_json()
        aws_controller.add_item(some_json)

class insurance(Resource):
    def get(self):
        return aws_controller.get_insurances()
    def post(self):
        some_json = request.get_json()
        aws_controller.add_insurance(some_json)

class singleInsurance(Resource):
    def get(self,ID):
        return aws_controller.get_insurance(ID)
    def put(self,ID):
        some_json = request.get_json(force=True)
        username=some_json['username'] #11111
        expiry=some_json['expiry']
        country=some_json['country']
        city=some_json['city']
        address=some_json['address']
        InsuranceName=some_json['Iname']
        identificationNumber=some_json['identificationNumber']
        aws_controller.update_insurance(ID,username,expiry,country,city,address,InsuranceName,identificationNumber)

class Single(Resource):
    def get(self,name):
        return aws_controller.get_item(name)
        #return {'you sent':name}
    def put(self,name):
        some_json = request.get_json(force=True)
        username=some_json['username']
        expiry=some_json['expiry']
        country=some_json['country']
        city=some_json['city']
        address=some_json['address']
        firstName=some_json['firstName']
        lastName=some_json['lastName']
        isVerified=some_json['isVerified']
        identificationNumber=some_json['identificationNumber']
        aws_controller.update_item(name,username,expiry,country,city,address,firstName,lastName,isVerified,identificationNumber)

class verify(Resource):
    def put(self,name):
        some_json = request.get_json()
        verifyValue=some_json['isVerified']
        aws_controller.verify_patient(name,verifyValue)


class get_by_country(Resource):
    def get(self,country):
        return aws_controller.get_by_country(country)

class update(Resource):
    def put(self,name):
        some_json = request.get_json(force=True)
        username=some_json['username']
        expiry=some_json['expiry']
        country=some_json['country']
        city=some_json['city']
        address=some_json['address']
        firstName=some_json['firstName']
        lastName=some_json['lastName']
        isVerified=some_json['isVerified']
        identificationNumber=some_json['identificationNumber']
        aws_controller.update_item(name,username,expiry,country,city,address,firstName,lastName,isVerified,identificationNumber)

# class remove(Resource):
#     def delete(self,what):

# class addbill(Resource):
#     def post(self,name):
#         some_json = request.get_json()
#         aws_controller.add_bill(name,some_json)
#         return some_json

class hospital(Resource):
    @hospitalkey
    def post(self,name):
        some_json = request.get_json()
        hospitalID=some_json['hospitalId']
        aws_controller.addHospital(name,hospitalID)
    @hospitalkey
    def delete(self,name):
        aws_controller.removeHospital(name)

class Patientinsurance(Resource):
    @insurancekey
    def post(self,name):
        some_json = request.get_json()
        insuranceID=some_json['insuranceId']
        aws_controller.addInsurance(name,insuranceID)
    @insurancekey
    def delete(self,name):
        aws_controller.removeInsurance(name)

class updateBill(Resource):
    def put(self,name,billid):
        some_json = request.get_json()
        status=some_json['status']
        aws_controller.update_table(name,billid,status)


class addBill(Resource):
    @doctorkey
    def post(self,name):
        some_json = request.get_json()
        billId=some_json['billId']
        date=some_json['date']
        doctor=some_json['doctor']
        cost=some_json['cost']
        VAT=some_json['VAT']
        total=some_json['total']
        status=some_json['status']
        aws_controller.add_bill(name,billId,date,doctor,cost,VAT,total,status)

class addDisease(Resource):
    @doctorkey
    def post(self,name):
        some_json = request.get_json()
        date=some_json['date']
        diseasename=some_json['name']
        doctor=some_json['doctor']
        symptomes= some_json['symptomes']
        medication=some_json['medication']
        aws_controller.add_disease(name,date,diseasename,doctor,symptomes,medication)

class addAllergy(Resource):
    @doctorkey
    def post(self,name):
        some_json = request.get_json()
        allergyName=some_json['name']
        doctor=some_json['doctor']
        date=some_json['date']
        severity= some_json['severity']
        medication=some_json['medication']
        aws_controller.add_allergy(name,allergyName,doctor,date,severity,medication)

class addOperation(Resource):
    @doctorkey
    def post(self,name):
        some_json = request.get_json()
        date=some_json['date']
        operationName=some_json['name']
        doctor=some_json['doctor']
        dischargeDate= some_json['dischargeDate']
        daysInHospital=some_json['daysInHospital']
        comment=some_json['comment']
        aws_controller.add_operation(name,date,operationName,doctor,dischargeDate,daysInHospital,comment)

class addDisablity(Resource):
    @doctorkey
    def post(self,name):
        some_json = request.get_json()
        date=some_json['date']
        disablityName=some_json['name']

        doctor=some_json['doctor']
        sideEffects= some_json['sideEffects']
        medication=some_json['medication']
        aws_controller.add_disablity(name,date,disablityName,doctor,sideEffects,medication)
class insuranceByCountry(Resource):
    def get(self,country):
        return aws_controller.get_insurance_country(country)

class verifyInsurance(Resource):
    def put(self,name):
        some_json = request.get_json()
        verifyValue=some_json['isVerified']
        keyValue=some_json['apikey']
        if(verifyValue=={'BOOL':True}):
            aws_controller.verify_insurance(name,verifyValue,keyValue)
        else:
            aws_controller.verify_insurancenokey(name,verifyValue)

class InsurancePatient(Resource):
    @insurancekey
    def post(self,name,patientID):
        aws_controller.addPatient(name,patientID)
    @insurancekey
    def delete(self,name,patientID):
        aws_controller.removePatient(name,patientID)
#---------------------------------------------------------------------------------------------------
#Hospital
class mainHosptial(Resource):
    def post(self):
        some_json = request.get_json()
        aws_controller.add_Hospital(some_json)

class singleHosptial(Resource):
    @hospitalkey
    def get(self,ID):
        return aws_controller.get_hospital(ID)
    @hospitalkey
    def put(self,ID):
        some_json = request.get_json()
        username=some_json['username']
        expiry=some_json['expiry']
        country=some_json['country']
        city=some_json['city']
        address= some_json['address']
        hospitalName=some_json['Hname']
        identificationNumber=some_json['identificationNumber']
        aws_controller.update_hospital(ID,username,expiry,country,city,address,hospitalName,identificationNumber)

class verifyHosptial(Resource):
    def put(self,name):
        some_json = request.get_json()
        verifyValue=some_json['isVerified']
        keyValue=some_json['apikey']
        if(verifyValue=={'BOOL':True}):
            aws_controller.verify_hospital(name,verifyValue,keyValue)
        else:
            aws_controller.verify_hospitalnokey(name,verifyValue)
class hospitalbyCountry(Resource):
    def get(self,country):
        return aws_controller.hospital_by_country(country)

class doctorHosptial(Resource):
    @hospitalkey
    def post(self,name,DoctorID):
        return aws_controller.addDoctorToHospital(name,DoctorID)
    @hospitalkey
    def delete(self,name,DoctorID):
        return aws_controller.removeDoctorToHospital(name,DoctorID)

class patientHosptial(Resource):
    @hospitalkey
    def post(self,name,patientID):
        return aws_controller.addPatientToHospital(name,patientID)
    @hospitalkey
    def delete(self,name,patientID):
        return aws_controller.removePatientToHospital(name,patientID)
#-----------------------------------------------------

class mainDoctor(Resource):
    def post(self):
        some_json = request.get_json()
        aws_controller.add_Doctor(some_json)

class singleDoctor(Resource):
    @doctorkey
    def get(self,name):
        return aws_controller.get_Doctor(name)
    @doctorkey
    def put(self,name):
        some_json = request.get_json()
        username=some_json['username']
        expiry=some_json['expiry']
        country=some_json['country']
        city=some_json['city']
        address= some_json['address']
        firstName=some_json['firstName']
        lastName=some_json['lastName']
        hospitalId=some_json['hospitalId']
        isVerified=some_json['isVerified']
        speciality=some_json['speciality']
        identificationNumber=some_json['identificationNumber']
        aws_controller.update_Doctor(name,username,expiry,country,city,address,firstName,lastName,hospitalId,isVerified,identificationNumber,speciality)
class verifyDoctor(Resource):
    def put(self,name):
        some_json = request.get_json()
        verifyValue=some_json['isVerified']
        keyValue=some_json['apikey']
        if(verifyValue=={'BOOL':True}):
            aws_controller.verify_Doctor(name,verifyValue,keyValue)
        else:
            aws_controller.verify_Doctornokey(name,verifyValue)

class countryDoctor(Resource):
    def get(self,country):
        return aws_controller.doctor_by_country(country)

class addPatientToDoctor(Resource):
    @hospitalkey
    def post(self,name):
        some_json = request.get_json()
        patientIds=some_json['patientIds']
        return aws_controller.addPatientToDoctor(name,patientIds)

class hospitalToDoctor(Resource):
    @hospitalkey
    def post(self,name):
        some_json = request.get_json()
        hospitalId=some_json['hospitalId']
        aws_controller.hospitalToDoctor(name,hospitalId)
    @hospitalkey
    def delete(self,name):
        return aws_controller.hospitalawayDoctor(name)
class goverment(Resource):
    def get(self,name):
        return aws_controller.get_government(name)

# class ApiVerify(Resource):
#     def post(self):
#         some_json = request.get_json()
#         return aws_controller.putAPI(some_json)

api.add_resource(HelloWorld,'/')
#api.add_resource(Multi,'/patient')# [get] show all patients, [post] add a patinet
#api.add_resource(get_by_country,'/patient/country/<country>')
api.add_resource(Single,'/patient/<name>')#get and put
api.add_resource(hospital,'/patient/<name>/hospital')#post and delete
api.add_resource(Patientinsurance,'/patient/<name>/insurance') #post and delete
#api.add_resource(verify,'/patient/<name>/verify') #put
#api.add_resource(addbill,'/Patient/<name>/add_bill')
api.add_resource(update,'/updatepatient/<name>') #put
api.add_resource(updateBill,'/patient/<name>/bill/<int:billid>') #put
api.add_resource(addBill,'/patient/<name>/bill')#post
api.add_resource(addDisease,'/patient/<name>/disease')#post
api.add_resource(addAllergy,'/patient/<name>/allergy')#post
api.add_resource(addDisablity,'/patient/<name>/disablity')#post
api.add_resource(addOperation,'/patient/<name>/operation')#post
api.add_resource(insurance,'/insurance')#get and post
api.add_resource(singleInsurance,'/insurance/<ID>')#update and get
#api.add_resource(verifyInsurance,'/insurance/<name>/verify')#put
api.add_resource(InsurancePatient,'/insurance/<name>/patient/<patientID>')#post and delete
api.add_resource(insuranceByCountry,'/insurance/country/<country>')#get
#hospitalroutes--------------------------------------------------
api.add_resource(mainHosptial,'/hospital')#post hostpial
api.add_resource(singleHosptial,'/hospital/<ID>')#get by id and update
api.add_resource(hospitalbyCountry,'/hospital/country/<country>')#get by get_by_country
#api.add_resource(verifyHosptial,'/hospital/<name>/verify')#get by id and update
api.add_resource(patientHosptial,'/hospital/<name>/patient/<patientID>')#Post/delete for patient
api.add_resource(doctorHosptial,'/hospital/<name>/doctor/<DoctorID>')#Post/delete for doctors
#doctorz------------------------------------------------------------------------
api.add_resource(mainDoctor,'/doctor')#add a doctor post
api.add_resource(singleDoctor,'/doctor/<name>')#put update a doctor, get find a doctor
api.add_resource(countryDoctor,'/doctor/country/<country>')#get
#api.add_resource(verifyDoctor,'/doctor/<name>/verify')#put
api.add_resource(addPatientToDoctor,'/doctor/<name>/patient')
api.add_resource(hospitalToDoctor,'/doctor/<name>/hospital')
#-------------------------------------------------------------------------------
api.add_resource(goverment,'/goverment/<name>') #get goverment by id
#-----------------------------------------------------------
# api.add_resource(ApiVerify,'/key')
if __name__=='__main__':
    app.run(debug=True)
