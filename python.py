from flask import Flask, render_template, request

app = Flask(__name__)

property_info_steps_text = [ # Step 1 
                            "If you’re redeeming a vehicle, contact your lender and confirm that a “Vehicle Release” has been issued directly to Paramount Recovery Service. This vehicle release MUST be issued to Paramount Recovery Service, directly. Otherwise, we cannot release the vehicle. No release is required for a property redemption appointment." ,
                            # Step 2
                            "Schedule a vehicle or property redemption appointment on the date and time of your choosing using the button below. Once scheduled, we review your file, confirm fees, and anything else needed to book your release. Availability varies based on the volume of other appointments, so book early. Scheduling the appointment is not a confirmation. The confirmation response will take up to 3 hours, Monday through Friday. All appointments are confirmed or denied with an explanation by 5pm Monday through Friday. Appointments made after 5pm may not be confirmed until the following business day." , 
                            # Step 3
                            "Please make sure to include your cell phone number or email. We need your preferred contact method to communicate with you and provide the address, fees, and all other needed items. Once your appointment is scheduled, we start by reviewing your file and confirming your appointment by email or text message (based on your preference). Next, we confirm any fees owed, provide you with the address of the appointment, and provide you with the police department to contact to obtain your Police Release." , 
                            # Step 4
                            "For the security and safety and of our customers, visitors and employees, and in compliance with CDC recommendations, that encourage contactless payments to help curb the spread of COVID-19, we can not accept any cash payments at any of our facilities. Payments made at the time of your appointment will require a MICROCHIPPED card bearing either a “VISA”, “DISCOVER”, “MASTERCARD,” or “AMERICAN EXPRESS” logo. If you do not have a microchipped card with one of these logos you can purchase one at many major retailers prior to your arrival at our facility" , 
                            # Step 5
                            "A government issued photo ID is acceptable in place of a Drivers license for a property redemption appointment. If you do not have a valid driver's license or a government issued photo ID, please call for assistance." ,
                            # Step 6
                            "If you are only picking up your property, please bring your keys so not to incur any additional fees from your lender."]

property_info_steps_1 = dict( step_name="Contacting your lender (VEHICLES ONLY)" , step_number=1 , step_text=property_info_steps_text[0])
property_info_steps_2 = dict( step_name="Schedule an appointment" , step_number=2 , step_text=property_info_steps_text[1])
property_info_steps_3 = dict( step_name="Include phone and email" , step_number=3 , step_text=property_info_steps_text[2])
property_info_steps_4 = dict( step_name="Payment (CASH ONLY & EXACT CHANGE)" , step_number=4 , step_text=property_info_steps_text[3])
property_info_steps_5 = dict( step_name="Bring valid driver's license" , step_number=5 , step_text=property_info_steps_text[4])
property_info_steps_6 = dict( step_name="Bring your keys" , step_number=6 , step_text=property_info_steps_text[5])

messages = ["message-1" , "message-2" , "message-3" , "message-4" , "message-5" , "message-6"]

@app.route('/')
def index():
    title = "Nations Recovery Services"
    header = "Nations Recovery Services Home"

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

    prop_url = "https://jasonnationsrecovery.wixsite.com/mysite/general-4"


    return render_template('property_information.html', message=info_message, title=title, header=header, message_1=messages[0], message_2=messages[1], message_3=messages[2], message_4=messages[3], message_5=messages[4], message_6=messages[5], prop_url=prop_url)

"""
DUMMY PROP REDEMPTION FORM

@app.route('/property-release', methods=['GET', 'POST'])
def property_release():
    if request.method == 'POST':
        # Process the form data here (e.g., save to database, send email)
        property_address = request.form['propertyAddress']
        owner_name = request.form['ownerName']
        owner_contact = request.form['ownerContact']
        property_description = request.form['propertyDescription']
        photographer_name = request.form['photographerName']
        photographer_contact = request.form['photographerContact']
        client_name = request.form['clientName']
        client_contact = request.form['clientContact']

        # For demonstration purposes, print the data
        print(f"Property Address: {property_address}")
        print(f"Owner Name: {owner_name}")
        # ... print other form data ...

        # You can add logic to handle the form submission (e.g., save to a file)
        return "Form submitted successfully!"  # Or redirect to a success page

    return render_template('property_release.html')"
"""

if __name__ == '__main__':
    app.run(debug=True)