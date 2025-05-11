from flask import Flask, render_template, request

app = Flask(__name__)

property_info_steps_text = [ # Step 1 
                            "Schedule a property redemption appointment on the date and time of your choosing using the link below. Appointments must be scheduled within a days advance due to the volume of appointments trying to be made so schedule EARLY. Monday - Friday 10A.M. - 4P.M.. Appointments made after 4P.M. may not be confirmed until the following business day." ,
                            # Step 2
                            "Once you schedule an appointment our office will review it and confirm with you any fees through text. If you are not the registered owner to the vehicle please call our office to assist you in redeeming your belongings." , 
                            # Step 3
                            "If you have any fees they must be paid in cash & must be exact change as the yard personnel are not allowed to carry cash on them." , 
                            # Step 4
                            "Please bring a valid driver's license to your appointment. A passport or militay ID is also acceptable. Contact our office if you are unable to provide a valid form of ID." , 
                            # Step 5
                            "Please arrive at your appointment on time. If you are late, you may have to reschulde your appointment or wait for the next available appointment. If you are unable to make your appointment please call our office to reschedule." ,
                            # Step 6
                            "When you arrive to the yard to redeem your property we will have everything bagged up and ready to go for you when you arrive. We can not allow unauthorized personnel on to our yards for safety purposes.",
                            # Step 7
                            "Lastly, if you wish to surrender your key you can do so with the yard staff."]

property_info_steps_1 = dict( step_name="Contacting your lender (VEHICLES ONLY)" , step_number=1 , step_text=property_info_steps_text[0])
property_info_steps_2 = dict( step_name="Schedule an appointment" , step_number=2 , step_text=property_info_steps_text[1])
property_info_steps_3 = dict( step_name="Include phone and email" , step_number=3 , step_text=property_info_steps_text[2])
property_info_steps_4 = dict( step_name="Payment (CASH ONLY & EXACT CHANGE)" , step_number=4 , step_text=property_info_steps_text[3])
property_info_steps_5 = dict( step_name="Bring valid driver's license" , step_number=5 , step_text=property_info_steps_text[4])
property_info_steps_6 = dict( step_name="Bring your keys" , step_number=6 , step_text=property_info_steps_text[5])
property_info_steps_7 = dict( step_name="Surrender your keys" , step_number=7 , step_text=property_info_steps_text[6])

info_messages = ["message-1" , "message-2" , "message-3" , "message-4" , "message-5" , "message-6", "message-7"]


vehicle_info_steps_text = [ # Step 1 
                            "Contact your finance company to see if a release has been issued to our office. If a release has not been issued please contact your finance company. Please understand that it does take some time for our office to receive the release from your finance comapny and that releases are not instant." ,
                            # Step 2
                            "After you have confirmed a release has been sent to our office you will need to go to the city's police station where your vehicle was repossessed and obtain a repo receipt. It is important you get this before you call to make your appointment as we need the confirmation number on the receipt to be able to schedule you an appointment. If you do not no which police station to go to please call our office." , 
                            # Step 3
                            "Once you have the repo receipt and your release has been received on our end you will need to call our office to schedule an appointment. Appointments must be scheduled within a days advance due to the volume of appointments trying to be made so schedule EARLY. Monday - Friday 10A.M. - 4P.M.. Appointments made after 4P.M. may not be confirmed until the following business day." ,
                            # Step 4
                            "If you have any fees they must be paid in cash & must be exact change as the yard personnel are not allowed to carry cash on them." , 
                            # Step 5
                            "Please bring a valid driver's license to your appointment. A passport or militay ID is also acceptable. Contact our office if you are unable to provide a valid form of ID." , 
                            # Step 6
                            "Please bring a copy of the repo receipt with you to your appointment. A picture or screenshot of the receipt is fine. This is important as we need to verify the vehicle was repossessed by the police department." ,
                            # Step 7
                            "Make sure you bring your key with you to your appointment. Please be aware your finance company may have approved a key to be made for your vehicle.",
                            # Step 8
                            "Please arrive at your appointment on time. If you are late, you may have to reschulde your appointment or wait for the next available appointment. If you are unable to make your appointment please call our office to reschedule", 
                            # Step 9
                            "When you arriive to the yard to redeem your vehicle we will have your vehicle ready to go for you when you arrive. We can not allow unauthorized personnel on to our yards for safety purposes so we will drive your vehicle out for you",
                            # Step 10
                            "Every appointment is 20 minuites long, so you will have time to inspect your vehicle and make sure everything is in order before you sign the paperwork"]

vehicle_info_steps_1 = dict( step_name="Contacting your lender" , step_number=1 , step_text=vehicle_info_steps_text[0])
vehicle_info_steps_2 = dict( step_name="Obtain a repo receipt" , step_number=2 , step_text=vehicle_info_steps_text[1])
vehicle_info_steps_3 = dict( step_name="Schedule an appointment" , step_number=3 , step_text=vehicle_info_steps_text[2])
vehicle_info_steps_4 = dict( step_name="Payment (CASH ONLY & EXACT CHANGE)" , step_number=4 , step_text=vehicle_info_steps_text[3])
vehicle_info_steps_5 = dict( step_name="Bring valid driver's license" , step_number=5 , step_text=vehicle_info_steps_text[4])
vehicle_info_steps_6 = dict( step_name="Bring repo receipt" , step_number=6 , step_text=vehicle_info_steps_text[5])
vehicle_info_steps_7 = dict( step_name="Bring your keys" , step_number=7 , step_text=vehicle_info_steps_text[6])
vehicle_info_steps_8 = dict( step_name="Arrive on time" , step_number=8 , step_text=vehicle_info_steps_text[7])
vehicle_info_steps_9 = dict( step_name="Ready to go" , step_number=9 , step_text=vehicle_info_steps_text[8])
vehicle_info_steps_10 = dict( step_name="Paperwork" , step_number=10 , step_text=vehicle_info_steps_text[9])

vehicle_messages = ["message-1" , "message-2" , "message-3" , "message-4" , "message-5" , "message-6", "message-7", "message-8", "message-9", "message-10"]


@app.route('/')
def index():
    title = "Nations Recovery Services"
    header = "Nations Recovery Services Inc."

    prop_url = "https://jasonnationsrecovery.wixsite.com/mysite/general-4"
    vehicle_url = "https://jasonnationsrecovery.wixsite.com/mysite/general-4"
    transport_url = "https://jasonnationsrecovery.wixsite.com/mysite"

    return render_template('index.html', title=title, header=header, prop_url=prop_url, vehicle_url=vehicle_url, transport_url=transport_url)

@app.route('/property-information')
def property_info():
    title = "Property information"
    header = "Property Release Information"
    # You can pass data to the template if needed
    info_message = "Here is some important information about property releases."

    info_messages[0] = property_info_steps_1['step_text']
    info_messages[1] = property_info_steps_2['step_text']
    info_messages[2] = property_info_steps_3['step_text']
    info_messages[3] = property_info_steps_4['step_text']
    info_messages[4] = property_info_steps_5['step_text']
    info_messages[5] = property_info_steps_6['step_text']
    info_messages[6] = property_info_steps_7['step_text']
    # You can add more messages or data as needed

    prop_url = "https://jasonnationsrecovery.wixsite.com/mysite/general-4"


    return render_template('property_information.html', message=info_message, title=title, header=header, message_1=info_messages[0], message_2=info_messages[1], message_3=info_messages[2], message_4=info_messages[3], message_5=info_messages[4], message_6=info_messages[5], message_7=info_messages[6], prop_url=prop_url)

@app.route('/vehicle-redemption-information')
def vehicle_redemption_info():
    title = "Vehicle redemption information"
    header = "Vehicle Release Information"
    # You can pass data to the template if needed
    info_message = "Here is some important information about vehicle releases."

    vehicle_messages[0] = vehicle_info_steps_1['step_text']
    vehicle_messages[1] = vehicle_info_steps_2['step_text']
    vehicle_messages[2] = vehicle_info_steps_3['step_text']
    vehicle_messages[3] = vehicle_info_steps_4['step_text']
    vehicle_messages[4] = vehicle_info_steps_5['step_text']
    vehicle_messages[5] = vehicle_info_steps_6['step_text']
    vehicle_messages[6] = vehicle_info_steps_7['step_text']
    vehicle_messages[7] = vehicle_info_steps_8['step_text']
    vehicle_messages[8] = vehicle_info_steps_9['step_text']
    vehicle_messages[9] = vehicle_info_steps_10['step_text']
    # You can add more messages or data as needed

    prop_url = "https://jasonnationsrecovery.wixsite.com/mysite/general-4"


    return render_template('redemption_information.html', message=info_message, title=title, header=header, message_1=vehicle_messages[0], message_2=vehicle_messages[1], message_3=vehicle_messages[2], message_4=vehicle_messages[3], message_5=vehicle_messages[4], message_6=vehicle_messages[5], message_7=vehicle_messages[6], message_8=vehicle_messages[7], message_9=vehicle_messages[8], message_10=vehicle_messages[9], prop_url=prop_url)


if __name__ == '__main__':
    app.run(debug=True)