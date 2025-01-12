from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(to_email, subject, content):
    print('hey')
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response)
        return response
    except Exception as e:
        print(str(e))
        return None


def send_change_room_request_created(request, student_email, staff_email):
    student_subject = "Change Room Request Submitted"
    student_content = f"""
    <h2>Your Change Room Request has been submitted</h2>
    <p>Request Details:</p>
    <ul>
        <li>Room Number: {request.room_number}</li>
        <li>Reason: {request.reason}</li>
        <li>Status: {request.status}</li>
    </ul>
    """

    staff_subject = "New Change Room Request"
    staff_content = f"""
    <h2>New Change Room Request Submitted</h2>
    <p>Student Details:</p>
    <ul>
        <li>Student ID: {request.student_id}</li>
        <li>Name: {request.student}</li>
        <li>Room Number: {request.room_number}</li>
        <li>Reason: {request.reason}</li>
    </ul>
    """

    send_email(student_email, student_subject, student_content)
    send_email(staff_email, staff_subject, staff_content)


def send_change_room_request_update(request, student_email):
    subject = "Change Room Request Updated"
    content = f"""
    <h2>Your Change Room Request has been updated</h2>
    <p>New Status: {request.status}</p>
    """

    send_email(student_email, subject, content)


def send_maintenance_request_created(request, student_email, staff_email, ppk_email):
    student_subject = "Maintenance Request Submitted"
    student_content = f"""
    <h2>Your Maintenance Request has been submitted</h2>
    <p>Request Details:</p>
    <ul>
        <li>Room Number: {request.room_number}</li>
        <li>Issue: {request.issue}</li>
        <li>Status: {request.status}</li>
    </ul>
    """

    staff_subject = "New Maintenance Request"
    staff_content = f"""
    <h2>New Maintenance Request Submitted</h2>
    <p>Details:</p>
    <ul>
        <li>Student ID: {request.student_id}</li>
        <li>Room Number: {request.room_number}</li>
        <li>Issue: {request.issue}</li>
    </ul>
    """

    send_email(student_email, student_subject, student_content)
    send_email(staff_email, staff_subject, staff_content)
    send_email(ppk_email, staff_subject, staff_content)


def send_maintenance_request_update(request, student_email, staff_email):
    subject = "Maintenance Request Updated"
    content = f"""
    <h2>Maintenance Request Status Updated</h2>
    <p>New Status: {request.status}</p>
    """

    send_email(student_email, subject, content)
    send_email(staff_email, subject, content)


def send_student_welcome_email(student):
    subject = "Welcome to Student Housing"
    content = f"""
    <h2>Welcome {student.name}!</h2>
    <p>Your student housing account has been created successfully.</p>
    <p>Details:</p>
    <ul>
        <li>Student ID: {student.student_id}</li>
        <li>Email: {student.email}</li>
    </ul>
    """

    send_email(student.email, subject, content)
