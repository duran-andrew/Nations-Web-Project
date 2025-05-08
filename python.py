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

messages = ["message-1" , "message-2" , "message-3" , "message-4" , "message-5" , "message-6", "message-7"]

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

    messages[0] = property_info_steps_1['step_text']
    messages[1] = property_info_steps_2['step_text']
    messages[2] = property_info_steps_3['step_text']
    messages[3] = property_info_steps_4['step_text']
    messages[4] = property_info_steps_5['step_text']
    messages[5] = property_info_steps_6['step_text']
    messages[6] = property_info_steps_7['step_text']
    # You can add more messages or data as needed

    prop_url = "https://jasonnationsrecovery.wixsite.com/mysite/general-4"


    return render_template('property_information.html', message=info_message, title=title, header=header, message_1=messages[0], message_2=messages[1], message_3=messages[2], message_4=messages[3], message_5=messages[4], message_6=messages[5], message_7=messages[6], prop_url=prop_url)

@app.route('/vehicle-redemption-information')
def vehicle_redemption_info():
    title = "Vehicle redemption information"
    header = "Vehicle Release Information"
    # You can pass data to the template if needed
    info_message = "Here is some important information about vehicle releases."

    messages[0] = property_info_steps_1['step_text']
    messages[1] = property_info_steps_2['step_text']
    messages[2] = property_info_steps_3['step_text']
    messages[3] = property_info_steps_4['step_text']
    messages[4] = property_info_steps_5['step_text']
    messages[5] = property_info_steps_6['step_text']
    messages[6] = property_info_steps_7['step_text']
    # You can add more messages or data as needed

    prop_url = "https://jasonnationsrecovery.wixsite.com/mysite/general-4"


    return render_template('property_information.html', message=info_message, title=title, header=header, message_1=messages[0], message_2=messages[1], message_3=messages[2], message_4=messages[3], message_5=messages[4], message_6=messages[5], message_7=messages[6], prop_url=prop_url)


if __name__ == '__main__':
    app.run(debug=True)