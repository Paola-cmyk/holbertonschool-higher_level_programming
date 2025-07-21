#!/usr/bin/python3
import os
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    # Input type checks
    if not isinstance(template, str):
        logging.error("Invalid template type. Expected string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid attendees data. Expected a list of dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):

        filled_template = template
        filled_template = filled_template.replace("{name}", str(attendee.get("name", "N/A") or "N/A"))
        filled_template = filled_template.replace("{event_title}", str(attendee.get("event_title", "N/A") or "N/A"))
        filled_template = filled_template.replace("{event_date}", str(attendee.get("event_date", "N/A") or "N/A"))
        filled_template = filled_template.replace("{event_location}", str(attendee.get("event_location", "N/A") or "N/A"))

        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(filled_template)
            logging.info(f"Generated file: {output_filename}")
        except Exception as e:
            logging.error(f"Failed to write to {output_filename}: {e}")

