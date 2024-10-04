import cv2
import smtplib
import numpy as np
from ultralytics import YOLO
import random
import os
# image_path = '/content/drive/MyDrive/kmihackathon/konsberg_results/snapshots/snapshot_0.jpg'
video_path = r'C:\Konsberg techathon\final_submission\model_folder\WhatsApp Video 2024-09-03 at 10.42.29 AM.mp4'

no_classes = ['no_boots','no_gloves','no_goggles','no_helmet','no_mask','no_vest']

model = YOLO(r'C:\Konsberg techathon\final_submission\model_folder\best.pt')

output_dir = r'C:\Konsberg techathon\final_submission\model_folder\snapshots'
os.makedirs(output_dir, exist_ok=True)


# Capture interval in seconds
capture_interval = 120  # Change as needed

# Open video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot open video.")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Check if it's time to capture a snapshot
    if frame_count % int(fps * capture_interval) == 0:
        # Save the snapshot
        snapshot_path = os.path.join(output_dir, f'snapshot_{frame_count}.jpg')
        cv2.imwrite(snapshot_path, frame)
        print(f"Snapshot saved: {snapshot_path}")

        # Perform object detection on the snapshot
        detect_params = model.predict(source=[snapshot_path], conf=0.5, save=False)
        # Initialize flag for alerts
        alert_triggered = False





        for result in detect_params:
          
          for box in result.boxes:
            cls_id = int(box.cls)       
            print(cls_id)
            label = result.names[cls_id]
            print(label)
            # Check if the label is in the "no" classes list
            if label in no_classes:
                print(f"ALERT: {label} detected!")
                alert_triggered = True

            if not alert_triggered:
                print("No ALERT.")


   # If an alert was triggered, send an email
        if alert_triggered:
            # Email configuration
            HOST = "smtp-mail.outlook.com"
            PORT = 587
            FROM_EMAIL = "prajwaldecs121@gst.sies.edu.in"
            TO_EMAIL = "prajwaldabhekar2003@gmail.com"
            PASSWORD = "Helloworld@123"

            # Create the email message with attachment
            MESSAGE = f"""Subject: ALERT MESSAGE\n\nAn alert has been triggered based on the detection results in the snapshot."""
            attachment_path = snapshot_path

            try:
                # Connect to the SMTP server
                smtp = smtplib.SMTP(HOST, PORT)
                smtp.ehlo()
                smtp.starttls()
                smtp.login(FROM_EMAIL, PASSWORD)

                # Send the email with attachment
                with open(attachment_path, 'rb') as file:
                    attachment_data = file.read()

                # Prepare the email
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                from email.mime.base import MIMEBase
                from email import encoders

                msg = MIMEMultipart()
                msg['From'] = FROM_EMAIL
                msg['To'] = TO_EMAIL
                msg['Subject'] = "ALERT MESSAGE"

                body = MIMEText("An alert has been triggered based on the detection results in the snapshot.", 'plain')
                msg.attach(body)

                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(attachment_data)
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
                msg.attach(attachment)

                smtp.send_message(msg)
                print("ALERT EMAIL SENT SUCCESSFULLY")

            except Exception as e:
                print(f"Error sending email: {str(e)}")

            finally:
                smtp.quit()

    frame_count += 1

# Release the video capture
cap.release()
cv2.destroyAllWindows()

